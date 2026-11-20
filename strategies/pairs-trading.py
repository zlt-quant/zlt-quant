# 来源：https://docs.zltquant.com/api/zltquant/api/strategy-examples.html#股票配对交易
# 整理日期：2026-11-20。以下正文保留官方公开示例。

# 股票配对交易

import scipy.stats as stats
import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import statsmodels
from statsmodels.tsa.stattools import coint
from zltquant import *
def initialize(context):
    # 设定上证50作为基准
    set_benchmark('sh000016')
    # 交易量设置  开仓量不超过当前25%
    set_option('order_volume_ratio', 0.25)

    g.threadhold = 0.02        # 阈值
    g.before_high_stock = None    # 之前的股票
    g.before_low_stock = None    # 之前的股票

# 定义计算协整关系的函数
def find_cointegrated_pairs(securities_df, sec_codes):
    n = len(sec_codes)
    # score用来判断股价是否是非平稳的，代表对股价进行单位根检定的t统计量
    # score_matrix = np.zeros((n, n))
    # 原假设是股票间不存在协整关系，如果Pvalue<0.05则拒绝原假设
    pvalue_matrix = np.ones((n, n))
    # 循环，计算两两股票间的协整关系，并将结果保存在矩阵中
    for i in range(n):
        for j in range(i+1, n):
            S1 = securities_df[securities_df["security"] == sec_codes[i]]['close']
            S2 = securities_df[securities_df["security"] == sec_codes[j]]['close']
            if len(S1) != len(S2):
                continue
            result = coint(S1, S2)
            score = abs(result[0])
            pvalue = result[1]
            if score > 3:
                pvalue_matrix[i, j] = pvalue
            else:
                pvalue_matrix[i, j] = 1
    return pvalue_matrix

# 每个单位时间(如果按天回测,则每天调用一次,如果按分钟,则每分钟调用一次)调用一次
def handle_data(context,data):
    log.info(context.current_dt)
    # 取得上证50股票列表
    symbol = get_index_stocks('sh000016')
    symbol_list = []
    for i in range(0, len(symbol)):
        symbol_list.append(symbol[i])

    # 取出上证50股票的价格
    securities_panel = get_price(
        symbol_list, count=100, end_date=context.current_dt, fields=['close'],fq=None, df=True)
    # 取得pvalue矩阵
    pvalues = find_cointegrated_pairs(securities_panel, symbol_list)
    # 找出矩阵pvalue的对角线以上的部分最小值得坐标
    # 由于对称关系，只需找对角线以上的就足够了

    index = (0, 0)
    m = 1
    num = len(symbol)
    for i in range(0, num):
        for j in range(i+1, num):
            if pvalues[i, j] < m:
                index = (i, j)
                m = pvalues[i, j]

    # 找出坐标后，根据坐标设置需要操作的两只股票
    g.security_high = symbol[index[0]]
    g.security_low = symbol[index[1]]

    set_universe([g.security_high, g.security_low])

    # 取出两只股票的价格
    hist_high = get_price(g.security_high, count=100, end_date=context.current_dt,
                          fields=None,fq=None)['close']
    hist_low = get_price(g.security_low, count=100, end_date=context.current_dt,
                         fields=None,fq=None)['close']

    # 计算价值中枢（回测时间内股价比值的均值）
    g.mean = np.mean(hist_high / hist_low)

    data = get_current_data()
    price_high = data[g.security_high].last_price
    price_low = data[g.security_low].last_price

    # 两只股票的股价比值
    price_ration = price_high / price_low

    # 记录换股：
    log.info('换股前', g.before_high_stock, g.security_high,
             g.before_low_stock, g.security_low)

    # 记录换股：
    log.info('换股后', g.before_high_stock, g.security_high,
             g.before_low_stock, g.security_low)

    # 当两股的股价比值超出价值中枢2%(阈值)时，执行卖出估价高的（security_high），买入股价低的（security_low)
    if price_ration > (1 + g.threadhold) * g.mean:
        # 卖出股价高的（security_high）买入股价低的（security_low）
        # 判断选股有没有变动
        if g.before_high_stock is None:
            g.before_high_stock = g.security_high
        else:
            if g.before_high_stock != g.security_high:
                if g.before_high_stock in context.portfolio.positions:
                    order_target(g.before_high_stock, 0)
                    cash = context.portfolio.available_cash
                    number_of_shares = int(cash/price_high)
                    # 下买入单
                    order_value(g.security_high, cash)
                    g.before_high_stock = g.security_high

        # 判断选股有没有变动
        if g.before_low_stock is None:
            g.before_low_stock = g.security_low
        else:
            if g.before_low_stock != g.security_low:
                if g.before_low_stock in context.portfolio.positions:
                    order_target(g.before_low_stock, 0)
                    cash = context.portfolio.available_cash
                    number_of_shares = int(cash/price_low)
                    # 下买入单
                    order_value(g.security_low, cash)
                    g.before_low_stock = g.security_low

        # 卖出股价高的
        if context.portfolio.positions[g.security_high].total_amount > 0:
            # 全部卖出股价高的
            order_target(g.security_high, 0)

        cash = context.portfolio.available_cash
        # 买入股价低的
        if cash > price_low * 100:
            # 得到能够购买的股数
            number_of_shares = int(cash/price_low)
            # 下买入单
            order_value(g.security_low, cash)

    # 当两股的股价比值低于价值中枢2%(阈值)时，执行卖出估价低的（security_low），买入股价高的（security_high）
    elif price_ration < (1-g.threadhold)*g.mean:
        # 判断选股有没有变动
        if g.before_high_stock is None:
            g.before_high_stock = g.security_high
        else:
            if g.before_high_stock != g.security_high:
                if g.before_high_stock in context.portfolio.positions:
                    order_target(g.before_high_stock, 0)
                    cash = context.portfolio.available_cash
                    number_of_shares = int(cash/price_high)
                    # 下买入单
                    order_value(g.security_high, cash)
                    g.before_high_stock = g.security_high

        # 判断选股有没有变动
        if g.before_low_stock is None:
            g.before_low_stock = g.security_low
        else:
            if g.before_low_stock != g.security_low:
                if g.before_low_stock in context.portfolio.positions:
                    order_target(g.before_low_stock, 0)
                    cash = context.portfolio.available_cash
                    number_of_shares = int(cash/price_low)
                    # 下买入单
                    order_value(g.security_low, cash)
                    g.before_low_stock = g.security_low

        # 卖出股价低的（security_low）买入股价高的（security_high）
        # 卖出股价低的
        if context.portfolio.positions[g.security_low].total_amount > 0:
            # 全部卖出股价低的
            order_target(g.security_low, 0)

        # 买入股价高的
        cash = context.portfolio.available_cash
        if cash > price_high*100:
            # 下买入单
            order_value(g.security_high, cash)

if __name__ == '__main__':
    run_main()

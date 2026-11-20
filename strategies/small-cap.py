# 来源：https://docs.zltquant.com/api/zltquant/api/strategy-examples.html#小市值策略
# 整理日期：2026-11-20。以下正文保留官方公开示例。

# 小市值策略

from zltquant import *
import numpy as np
import pandas as pd
from datetime import time,date
def initialize(context):
    # 设定基准
    set_benchmark('sz399102')
    #初始化全局变量 bool
    g.trading_signal = True  # 是否为可交易日
    #全局变量list
    g.hold_list = [] #当前持仓的全部股票
    g.yesterday_HL_list = [] #记录持仓中昨日涨停的股票
    g.target_list = []
    g.limitup_stocks = []   # 记录涨停的股票避免再次买入
    #全局变量float/str
    g.min_mv = 10  # 股票最小市值要求
    g.max_mv = 100  # 股票最大市值要求
    g.stock_num = 4  # 持股数量
    g.stoploss_list = []  # 止损卖出列表
    g.other_sale    = []  # 其他卖出列表
    g.highest = 50  # 股票单价上限设置
    # 设置交易运行时间
    run_daily(prepare_work, '9:05')
    run_daily(trade_afternoon, time='14:20') #检查持仓中的涨停股是否需要卖出
    run_weekly(weekly_adjustment, 3,'09:31') #每周三:31调仓

#准备工作
#每天早上9:05，更新昨日持仓股涨停股列表，更新今日是否可以开仓布尔变量
def prepare_work(context):
    #获取已持有列表
    g.limitup_stocks = []
    g.hold_list = list(context.portfolio.positions)
    #获取昨日涨停列表
    if g.hold_list:
        df = get_price(g.hold_list, end_date=context.current_dt, frequency='daily', fields=['close'], count=2, df=True, fill_suspend=False)
        for stock in g.hold_list:
            if df.loc[df['security']==stock,'close'].iloc[0] >= df.loc[df['security']==stock,'close'].iloc[1] * 1.2: #昨日收盘价大于昨日收盘价的1.2倍，则为涨停股
                g.yesterday_HL_list.append(stock)
    else:
        g.yesterday_HL_list = []

#选股模块
#选股，选出满足筛选条件的买入股票list
def get_stock_list(context):
    final_list = []
    MKT_index = 'sz399102'
    initial_list = get_index_stocks(MKT_index)
    data = get_valuation_indicators(initial_list, ['market_cap'])
    data = data[data['market_cap'] > g.min_mv * 100000000]  # 总市值大于10亿元
    data = data[data['market_cap'] < g.max_mv * 100000000]  # 总市值小于100亿元
    data = data.sort_values(by='market_cap', ascending=True)
    data = data.head(g.stock_num*3)
    stock_list = data['security'].tolist()
    data = get_fundamentals_pit(stock_list, ['is_parent_net_profit','is_net_profit','is_op_rev'])
    data = data[data['is_parent_net_profit'] > 0]
    data = data[data['is_net_profit'] > 0]
    data = data[data['is_op_rev'] > 1e8]
    final_list = data['security'].tolist()
    return final_list

#每周调仓函数
def weekly_adjustment(context):
    if g.trading_signal:#满足开仓条件
        g.target_list = get_stock_list(context)[:g.stock_num]#应买的股票池
        log.info(f"今日股票池:{str(g.target_list)}")
        #首先确定哪些要卖，没在新预买池里的，没涨停的
        sell_list = [stock for stock in g.hold_list if stock not in g.target_list and stock not in g.yesterday_HL_list]
        #持仓表，就是要么涨停了不卖，要么就还在目标股池中
        hold_list = [stock for stock in g.hold_list if stock in g.target_list or stock in g.yesterday_HL_list]
        log.info("卖出[%s]" % (str(sell_list)))
        log.info("已持有[%s]" % (str(hold_list)))
        #先卖
        for stock in sell_list:
            order_target_value(stock, 0)
        #后买
        buy_list = [stock for stock in g.target_list if stock not in g.hold_list]
        buy_security(context, buy_list,len(buy_list))
    else:
        log.info('该月份为空仓月份')

#持仓涨停不卖出模块
def deal_up(context):
    now_time = context.current_dt
    if g.yesterday_HL_list != []:
        #对昨日涨停股票观察到尾盘如不涨停则提前卖出，如果涨停即使不在应买入列表仍暂时持有
        for stock in g.yesterday_HL_list:
            current_data = get_price(stock, end_date=now_time, frequency='1m', fields=['close'], skip_paused=False, fq='pre', count=1, df=True, fill_suspend=True)['close'].iloc[0]
            high_limit = get_price_limit(stock, end_date=now_time, count=1)['high_limit'].iloc[0]
            if current_data < high_limit:#这两个是收盘价<最高价的意思
                log.info("[%s]涨停打开，卖出" % (stock))
                order_target_value(stock, 0)
                g.other_sale.append(stock)
                g.limitup_stocks.append(stock)
            else:
                log.info("[%s]涨停，继续持有" % (stock))

#下午检查交易，把持仓中涨停破板的卖出，继续涨停的继续持有
def trade_afternoon(context):
    if g.trading_signal:#判断今日是否可以开仓
        deal_up(context)  #涨停不卖出模块，把没涨停的持仓就卖了
#买入模块
def buy_security(context,target_list,num):
    #调仓买入
    position_count = len(context.portfolio.positions)
    target_num = num
    if target_num !=0:
        value = context.portfolio.available_cash / target_num
        for stock in target_list:
            order_target_value(stock, value)
            log.info("买入[%s]（%s元）" % (stock,value))
            if len(context.portfolio.positions) == g.stock_num:
                break

if __name__ == '__main__':
    run_main()

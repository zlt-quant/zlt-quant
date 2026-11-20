# 来源：https://docs.zltquant.com/api/zltquant/api/strategy-examples.html#多因子选股
# 整理日期：2026-11-20。以下正文保留官方公开示例。

# 多因子选股

from zltquant import *
import datetime

# 初始化函数，设定策略参数
def initialize(context):
    # 设置选股和交易频率，每天运行一次
    run_daily(select_and_trade, time='every_bar')

# 选股和交易函数
def select_and_trade(context):
    # 1. 选股逻辑
    selected_stocks = select_stocks(context)

    # 2. 更新持仓股票的被选中状态
    buy_list, sell_list = update_order_list(context,selected_stocks)

    # 3. 交易逻辑
    trade(context, buy_list, sell_list)

# 选股函数
def select_stocks(context):
    # 获取所有股票列表(创业板)
    stock_list = get_index_stocks('sz399006',date=context.current_dt)

    # 初始化选股结果
    selected_stocks = []

    # 遍历所有股票
    for stock in stock_list:
        # 获取过去60个交易日的收盘价
        hist = get_price(stock, end_date=context.current_dt, frequency='1d', fields=['close'], count=60, fq='pre',df=True)
        if len(hist) == 0:
            continue
        # log.info(hist)

        # 计算波动率（标准差）
        std_dev = hist['close'].std()

        # 计算价格的均值
        mean_price = hist['close'].mean()

        # 计算归一化波动率
        normalized_volatility = std_dev / mean_price

        # 计算5日均线和20日均线
        short_ma = hist['close'].rolling(window=5).mean().iloc[-1]
        long_ma = hist['close'].rolling(window=20).mean().iloc[-1]

        # 获取过去20个交易日的日均成交额
        hist_volume = get_price(stock, end_date=context.current_dt, frequency='1d', fields=['money'], count=20, fq='pre',df=True)
        avg_turnover = hist_volume['money'].mean()
        # 筛选条件：
        # 1. 归一化波动率大于某个阈值
        # 2. 短期均线大于长期均线
        # 3. 日均成交额大于某个阈值
        if normalized_volatility > 0.2 and short_ma > long_ma and avg_turnover > 100000000:
            selected_stocks.append(stock)
    # 输出选股结果
    log.info('选中的股票列表：{}'.format(selected_stocks))

    return selected_stocks

# 更新持仓股票的被选中状态
def update_order_list(context,selected_stocks):
    buy_list = []
    sell_list = []
    # 获取当前持仓的股票
    long_positions = context.portfolio.positions

    # 遍历当前持仓的股票
    for stock in long_positions:
        if stock not in selected_stocks:
            # 如果持仓股不在选中列表中，标记卖出
            sell_list.append(stock)
    for stock in selected_stocks:
        if stock not in long_positions:
            # 如果选中的股票不在持仓列表中，标记买入
            buy_list.append(stock)
    return buy_list, sell_list

# 交易函数
def trade(context, buy_list, sell_list):
    # 1. 卖出未被选中的持仓股票
    for stock in sell_list:
        order_target(stock, 0)  # 卖出全部持仓

        log.info('卖出股票：{}'.format(stock))

    # 2. 买入新选中的股票
    #  分配资金
    if len(buy_list) != 0:
        cash = context.portfolio.available_cash / len(buy_list)
        for stock in buy_list:
            # 如果股票被选中且未持仓，买入
            order_target_value(stock, cash)  # 等权重买入

            log.info('买入股票：{}'.format(stock))

if __name__ == '__main__':
    run_main()

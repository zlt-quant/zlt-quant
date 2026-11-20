# 来源：https://docs.zltquant.com/api/zltquant/api/strategy-examples.html#均值回复策略
# 整理日期：2026-11-20。以下正文保留官方公开示例。

# 均值回复策略

from zltquant import *
from datetime import *
def initialize(context):
    # 设定基准
    set_benchmark('sz399300')

    # 输出内容到日志 log.info()
    log.info('初始函数开始运行且全局只运行一次')

    run_daily(after_market_close, time='15:30')
    run_monthly(adjust_position, monthday=1, time='10:30')

    g.observe_days = 20       #收益率观察交易日数
    g.target_value = 10000    #每只股票金额
    g.stock_number = 10       #单方向股票数量

# 调仓
def adjust_position(context):
    stocks = get_index_stocks('sz399300')
    stocks = filter_stocks(context, stocks)
    df = get_price(stocks, count=g.observe_days, end_date=context.current_dt, frequency='1d', fields=['close'],fq='pre',df=True)

    #按历史收益率排序
    grouped = df.groupby('security').agg({
        'close': ['first', 'last']
    }).reset_index()
    grouped.columns = ['code', 'start_price', 'end_price']
    grouped['return'] = (grouped['end_price'] - grouped['start_price']) / grouped['start_price']
    grouped_sorted = grouped.sort_values(by='return', ascending=True)

    bad_list = grouped_sorted['code'][:g.stock_number]
    good_list = grouped_sorted['code'][-g.stock_number:]

    log.info('表现差的股票：%s' % bad_list)
    log.info('表现好的股票：%s' % good_list)

    # 均值回复策略
    new_long_list = bad_list
    new_short_list = good_list

    # 当前的组合仓位信息
    portfolio = context.portfolio
    long_positions = list(portfolio.positions.keys())
    log.info("positions", long_positions)

    # 多头平仓
    for stock in long_positions:
        if stock not in new_long_list:
            amount = portfolio.positions[stock].closeable_amount
            log.info("多头平仓，股票：%s" % stock)
            order(stock, -amount)


    # 多头开仓
    for stock in new_long_list:
        if stock not in long_positions:
            log.info("多头开仓，股票：%s" % stock)
            order_target_value(stock, g.target_value)


#过滤各种股票
def filter_stocks(context, stock_list):
    filtered_stocks = []
    for stock in stock_list:
        stock_code = stock[2:]
        if stock_code.startswith('30') or stock_code.startswith('68') or stock_code.startswith('8') or stock_code.startswith('4'):  # 市场类型
            continue
        start_date = get_security_info(stock).start_date
        if context.previous_date - start_date < timedelta(days=375):
            continue
        filtered_stocks.append(stock)
    return filtered_stocks

## 收盘后运行函数
def after_market_close(context):
    p = context.portfolio
    log.info('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    log.info('总资产：', p.total_value)
    log.info('##############################################################')

if __name__ == '__main__':
    run_main()

# 来源：https://docs.zltquant.com/api/zltquant/api/strategy-examples.html#布林线均值回归
# 整理日期：2026-11-20。以下正文保留官方公开示例。

# 布林线均值回归

"""
- 当股票价格触及布林线上轨且有持仓时, 卖出股票.
- 当股票价格触及布林线下轨且无持仓时, 买入股票.
"""

from zltquant import *

# 初始化函数，设定策略参数
def initialize(context):
    # 设置回测频率为每日
    set_benchmark('sz399300')  # 设置基准为沪深300指数
    # 设置股票池
    g.stock = 'sh600000'
    # 设置布林线参数
    g.window = 20  # 布林线的窗口期
    g.num_std = 2  # 标准差倍数
    # 设置定时器，每天开盘时运行
    run_daily(trade, time='09:31')

# 交易函数
def trade(context):
    # 获取股票的历史数据
    dbar1 = get_price(g.stock, end_date=context.current_dt, count=g.window, fq="pre")
    stock_data = pd.Series(dbar1['close'])  # 将 close 数据转换为 pandas.Series

    # 计算布林线
    mean = stock_data.rolling(window=g.window).mean().iloc[-1]  # 中轨（移动平均）
    std = stock_data.rolling(window=g.window).std().iloc[-1]    # 标准差
    upper_band = mean + g.num_std * std  # 上轨
    lower_band = mean - g.num_std * std  # 下轨
    # 获取当前价格
    current_price = stock_data.iloc[-1]
    # 获取当前持仓
    current_position = context.portfolio.positions[g.stock].total_amount

    # 交易逻辑
    if current_price > upper_band and current_position > 0:
        # 如果当前价格高于上轨且有持仓，则卖出
        order_target(g.stock, 0)
        log.info("卖出股票：%s" % g.stock)
    elif current_price < lower_band and current_position == 0:
        # 如果当前价格低于下轨且无持仓，则买入
        order_value(g.stock, context.portfolio.available_cash)
        log.info("买入股票：%s" % g.stock)


# 收盘后运行函数
def after_trading_end(context):
    # 打印每日收盘后的信息
    log.info("每日收盘后运行")
    pass
if __name__ == '__main__':
    run_main()

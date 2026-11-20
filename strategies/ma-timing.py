# 来源：https://docs.zltquant.com/api/zltquant/api/strategy-examples.html#均线择时
# 整理日期：2026-11-20。以下正文保留官方公开示例。

# 均线择时

import pandas as pd
from zltquant import *

def initialize(context):
    # 设置要操作的股票
    g.security = 'sz000001'

def handle_data(context,data):
    short = 12
    long = 26
    mid = 9

    # 获取历史数据
    bar = get_price(g.security, end_date=context.current_dt, count=long + mid, frequency='1d', fq='pre', fill_suspend=True)
    close = pd.Series(bar['close'])

    # 计算EMA
    ema_short = close.ewm(span=short, adjust=False).mean()
    ema_long = close.ewm(span=long, adjust=False).mean()

    # 计算DIFF和DEA
    diff = ema_short - ema_long
    dea = diff.ewm(span=mid, adjust=False).mean()

    # 计算MACD
    macd = (diff - dea) * 2

    # 金叉买入
    if diff.iloc[-1] > dea.iloc[-1] and macd.iloc[-1] > macd.iloc[-2] and g.security not in context.portfolio.positions.keys():
        # 记录这次买入
        order_value(g.security, context.portfolio.available_cash)

    # 死叉卖出
    elif diff.iloc[-1] < dea.iloc[-1] and macd.iloc[-1] < macd.iloc[-2] and g.security in context.portfolio.positions.keys():
        # 记录这次卖出
        order_target(g.security, 0)

if __name__ == '__main__':
    run_main()

# 来源：https://docs.zltquant.com/api/zltquant/api/strategy-examples.html#海龟交易法则
# 整理日期：2026-11-20。以下正文保留官方公开示例。

# 海龟交易法则

from zltquant import *
import pandas as pd
import datetime
import math
from collections import deque

def initialize(context):
    set_order_cost(OrderCost(close_tax=0.001, open_commission=0.0003, close_commission=0.0003, min_commission=5), type='stock')
    g.security = 'sh601012'
    set_benchmark(g.security)
    # 入市的trailing date
    g.in_day = 20
    # 出市的trailing date
    g.out_day = 10
    # 当前持仓的交易单位
    g.current_units = 0
    # 当天交易的交易单位
    g.today_units = 0
    g.current_units = 0
    g.N=deque(maxlen=19)
    g.current_N = 0
    g.last_buy_price = 0

    price = get_price(security=g.security, end_date=context.current_dt,count=g.N.maxlen*2+1,frequency= '1d',fields=['high', 'low', 'close'])
    log.info('ff',g.N.maxlen+1, g.N.maxlen*2+1)
    for i in range(g.N.maxlen+1, g.N.maxlen*2+1):
        li = []
        for j in range(i-19,i+1):
            a = price['high'][j]-price['low'][j]
            b = abs(price['high'][j]-price['close'][j-1])
            c = abs(price['low'][j]-price['close'][j-1])
            li.append(max(a,b,c))
        current_N = np.array(li).mean()
        g.N.append(current_N)

def before_trading_start(context):
    g.current_N = cal_N(context)
    g.today_units = 0

def handle_data(context,data):
    dt = context.current_dt
    data=get_current_data()
    current_price = data[g.security].last_price #上一分钟价格
    value = context.portfolio.total_value
    cash = context.portfolio.available_cash

    unit = math.floor(value * 0.01 / g.current_N)

    if g.current_units == 0:
        buy(context,current_price, cash, unit)
    else:
        if stop_loss(current_price):
            return
        if sell(current_price):
            return
        addin(current_price, cash, unit)

def cal_N(context):
    price = get_price(security=g.security, end_date=context.current_dt,count=2,frequency= '1d',fields=['high', 'low', 'close'])
    a = price['high'][1]-price['low'][1]
    b = abs(price['high'][1]-price['close'][0])
    c = abs(price['low'][1]-price['close'][0])
    current_N = (max(a,b,c) + np.array(g.N).sum())/(g.N.maxlen+1)
    g.N.append(current_N)
    log.info('nnn',g.N)
    return current_N

def buy(context,current_price, cash, unit):
    price = get_price(security=g.security, end_date=context.current_dt, count=g.in_day,frequency= '1d',fields=['close'])
    if current_price > max(price['close']):
        log.info('ppp',current_price ,price['close'])
        shares = cash / current_price
        if shares >= unit:
            log.info("buying %d" % unit)
            o = order(g.security, unit)
            o = get_orders()[o]
            g.last_buy_price = float(o.price)
            g.current_units += 1
            g.today_units += 1
            return True
    return False

def addin(current_price, cash, unit):
    if current_price >= g.last_buy_price + 0.5 * g.current_N:
        shares = cash / current_price
        if shares >= unit:
            log.info("adding %d" % unit)
            o = order(g.security, unit)
            o = get_orders()[o]
            g.last_buy_price = float(o.price)
            g.current_units += 1
            g.today_units += 1
            return True
    return False

def sell(current_price):
    price = attribute_history(g.security, g.out_day, '1d', ('close',))
    if current_price < min(price['close']):
        log.info("selling")
        order_target(g.security, 0)
        g.current_units = g.today_units
        return True
    return False

def stop_loss(current_price):
    if current_price < g.last_buy_price - 2 * g.current_N:
        log.info("stop loss")
        order_target(g.security, 0)
        g.current_units = g.today_units
        return True
    return False
if __name__ == '__main__':
    run_main()

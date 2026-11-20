# 来源：https://docs.zltquant.com/api/zltquant/api/strategy-examples.html#趋势跟踪
# 整理日期：2026-11-20。以下正文保留官方公开示例。

# 趋势跟踪

import pandas as pd
from zltquant import *
import numpy as np

# 初始化函数，设定策略参数
def initialize(context):
    # 设置标的
    g.symbol = 'sz000001'
    #set_benchmark(g.symbol)
    # 储存前一个所处区间
    g.last_grid = 0
    # 以前一交易日的收盘价为中枢价格
    g.center = get_previous_close_price(context)
    # 记录上一次交易时区间的变化情况
    g.grid_change_last = [0, 0]
    # 设置价格区间
    g.band_width = update_band_width(context)
    g.band = [g.center + i * g.band_width for i in range(-3, 4)]
    # 定时运行，每分钟判断一次
    run_daily(cut_loss, time='every_bar')
    run_daily(check_grid, time='every_bar')
# 获取前一交易日的收盘价
def get_previous_close_price(context):
    # 获取前一个交易日的收盘价
    hist = get_price(security=g.symbol, end_date=context.current_dt.strftime("%Y-%m-%d %H:%M:%S"), frequency='1d',fields=['close'], count=1, fq='pre')

    log.info(hist)
    return hist['close'][0]

def update_band_width(context):
    hist = get_price(security=g.symbol, end_date=context.current_dt.strftime("%Y-%m-%d %H:%M:%S"), frequency='1d',
                     fields=['close'], count=60, fq='pre')
    std_dev = hist['close'].std()
    return round(std_dev, 2)

# 交易逻辑
def check_grid(context):
    # 获取当前价格
    current_price = get_price(security=g.symbol, end_date=context.current_dt.strftime("%Y-%m-%d %H:%M:%S"),
                              frequency='1m', fields=['close'], count=1, fq='pre')['close'][0]
    # 获取当前持仓

    position = context.portfolio.positions[g.symbol].total_amount if g.symbol in context.portfolio.positions else 0
    # 判断当前价格所处的价格区间
    grid = pd.cut([current_price], g.band, labels=[-3, -2, -1, 1, 2, 3])[0]

    # 止损

    # 如果价格超出价格区间，重置区间相关参数
    if np.isnan(grid):
        log.info('价格波动超过价格区间，可适当调节价格区间宽度和数量')
        # 储存前一个所处区间
        g.last_grid = 0
        # 以前一交易日的收盘价为中枢价格
        g.center = get_previous_close_price(context)
        # 记录上一次交易时区间范围的变化情况
        g.grid_change_last = [0, 0]
        # 设置价格区间
        g.band_width = update_band_width(context)
        g.band = [g.center + i * g.band_width for i in range(-3, 4)]

        return

    # 如果新的价格所处区间和前一个价格所处的区间不同，说明触碰到了辅助线，需要进行交易
    # 如果新区间大于前区间，全部卖出
    if g.last_grid < grid:
        if g.last_grid == 0:
            g.last_grid = grid
            g.grid_change_last = [g.last_grid, grid]
            return
        if g.last_grid != 0 and position > 0:
            current_price = get_price(security=g.symbol, end_date=context.current_dt.strftime("%Y-%m-%d %H:%M:%S"),
                                      frequency='1m', fields=['close'], count=1, fq='pre')['close'][0]
            order_target(g.symbol, 0, MarketOrderStyle(current_price * 0.98))
            log.info('以市价单卖出{}股'.format(position))
            log.info('上一个grid：{}，当前grid：{}，当前价格：{}'.format(g.last_grid, grid, current_price))
            g.last_grid = grid
            g.grid_change_last = [g.last_grid, grid]


    # 如果新区间小于当前区间，买入
    if g.last_grid > grid:
        if g.last_grid == 0:
            g.last_grid = grid
            g.grid_change_last = [g.last_grid, grid]
            return
        if g.last_grid != 0 and position == 0:
            current_price = get_price(security=g.symbol, end_date=context.current_dt.strftime("%Y-%m-%d %H:%M:%S"),
                                      frequency='1m', fields=['close'], count=1, fq='pre')['close'][0]
            order_target_value(g.symbol, context.portfolio.available_cash * 0.9, MarketOrderStyle(current_price * 1.02))
            log.info('以市价单买入{} 元'.format(context.portfolio.available_cash * 0.9))
            log.info('上一个grid：{}，当前grid：{}，当前价格：{}'.format(g.last_grid, grid, current_price))
            g.last_grid = grid
            g.grid_change_last = [g.last_grid, grid]


def cut_loss(context):
    # 当最新价*90%大于成本价，止损
    avg_cost = context.portfolio.positions[g.symbol].avg_cost if g.symbol in context.portfolio.positions else 0
    price = context.portfolio.positions[g.symbol].price if g.symbol in context.portfolio.positions else 0

    if avg_cost < price * 0.9:
        position = context.portfolio.positions[g.symbol].total_amount if g.symbol in context.portfolio.positions else 0
        order_target(g.symbol, 0, MarketOrderStyle(price * 0.98))
        log.info('触发止损线，以市价单卖出{}股'.format(position))


if __name__ == '__main__':
    run_main()

# 来源：https://docs.zltquant.com/api/zltquant/api/functions/getting-started.html#多账号策略模版
# 整理日期：2026-11-20。以下正文保留官方公开示例。

"""
多账号策略模板

使用前请先在界面配置多个账号。策略中通过 pindex 指定账号：
pindex=0 表示界面账号列表中的第 1 个账号；
pindex=1 表示界面账号列表中的第 2 个账号。
"""
from zltquant import *

# 必须
def initialize(context):
    g.stock = 'sh600000'
    g.account0_index = 0
    g.account1_index = 1

def handle_data(context, data):
    # context.portfolio 是汇总账号，聚合所有账号的资金、持仓和收益
    total_portfolio = context.portfolio
    log.info('汇总账号可用资金:', total_portfolio.available_cash)
    log.info('汇总账号总资产:', total_portfolio.total_value)

    # context.portfolios 是单账号列表，顺序与界面账号列表一致
    account0 = context.portfolios[g.account0_index]
    account1 = context.portfolios[g.account1_index]

    log.info('第1个账号可用资金:', account0.available_cash)
    log.info('第2个账号可用资金:', account1.available_cash)

    # 读取指定账号的持仓。没有持仓时返回 None，避免直接索引导致报错
    account0_pos = account0.positions.get(g.stock)
    if account0_pos is not None:
        log.info('第1个账号持仓数量:', account0_pos.total_amount)
        log.info('第1个账号可卖数量:', account0_pos.closeable_amount)

    # 使用第1个账号按数量下单
    oid0 = order(g.stock, 100, pindex=g.account0_index)
    log.info('第1个账号订单ID:', oid0)

    # 使用第2个账号按金额下单
    oid1 = order_value(g.stock, 10000, pindex=g.account1_index)
    log.info('第2个账号订单ID:', oid1)

    # 将第2个账号目标持仓数量调整为 1000 股
    oid2 = order_target(g.stock, 1000, pindex=g.account1_index)
    log.info('第2个账号调仓订单ID:', oid2)

# 必须
if __name__ == '__main__':
    run_main()

# 来源：https://docs.zltquant.com/api/zltquant/api/functions/getting-started.html#期货策略模版
# 整理日期：2026-11-20。以下正文保留官方公开示例。

"""
期货策略模板
"""
from zltquant import *

# 必须
def initialize(context):
    # 期货类每笔交易时的手续费是：买入时万分之0.23，卖出时万分之0.23，平今仓为万分之23
    set_order_cost(OrderCost(open_commission=0.000023,
                             close_commission=0.000023,
                             close_today_commission=0.0023),
                   type='futures')

    # 为全部交易品种设定固定值滑点
    set_slippage(FixedSlippage(0.002))

    # 设置主连，在期货策略中建议使用对应品种的主连作为参考标的（仅用于确定时间基准，不能用于查询持仓）
    run_daily(func, time='open', reference_security='zjIFL8')

def func(context):
    # 获取可交易合约列表
    future01 = get_future_contracts('IF')

    # 开空1手
    oid = order(security=future01[0], amount=1, side='short')
    log.info(oid)

# 必须
if __name__ == '__main__':
    run_main()

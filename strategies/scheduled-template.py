# 来源：https://docs.zltquant.com/api/zltquant/api/functions/getting-started.html#基础模版2
# 整理日期：2026-11-20。以下正文保留官方公开示例。

from zltquant import *
# 必须
def initialize(context):
    g.security = 'sz000001'  # 初始化持仓标的为平安银行
    # 示例：每天 09:30 固定时间执行
    run_daily(trade_at_fixed_time, time='09:30')

def trade_at_fixed_time(context):
    # 具体策略逻辑：开盘买入持仓标的至满仓
    oid = order(g.security, 100)
    log.info(oid)  # 输出：ZLT-0000000-000001

if __name__=='__main__': 
    run_main()

# 来源：https://docs.zltquant.com/api/zltquant/api/functions/getting-started.html#tick回测策略模版
# 整理日期：2026-11-20。以下正文保留官方公开示例。

"""
tick策略回测
"""
from zltquant import *

# 必须
def initialize(context):
    pass

def handle_tick(context, tick):
    data = get_ticks('sz000001', context.current_dt, count=10)
    data = get_ticks('sz000001', context.current_dt, count=10, df=True)
    data = get_ticks(['sz000001', 'sh600000'], context.current_dt, count=10, df=True)
    data = get_ticks(['sz000001', 'sh600000'],
                     start_date='2025-05-12',
                     end_date='2025-05-12',
                     df=True)
    log.info(data)
    order('sz000001', 400)

# 必须
if __name__ == '__main__':
    run_main()

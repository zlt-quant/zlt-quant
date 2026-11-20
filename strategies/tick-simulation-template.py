# 来源：https://docs.zltquant.com/api/zltquant/api/functions/getting-started.html#tick仿真策略模版
# 整理日期：2026-11-20。以下正文保留官方公开示例。

"""
tick仿真策略，tick策略执行仿真时，需要先订阅
"""
from zltquant import *

# 必须
def initialize(context):
    subscribe('sz000001')

def handle_tick(context, tick):
    order('sz000001', 500)
    print(tick)

# 必须
if __name__ == '__main__':
    run_main()

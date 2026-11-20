# 来源：https://docs.zltquant.com/api/zltquant/api/functions/getting-started.html#基础模版1
# 整理日期：2026-11-20。以下正文保留官方公开示例。

from zltquant import * 

def initialize(context): 
    # 设置基准收益: 沪深300指数
    set_benchmark('sz399300')

    # 打印日志
    log.info('策略开始运行,初始化函数全局只运行一次')

    # 股票类每笔交易时的手续费是: 买入时佣金万分之三,卖出时佣金万分之三加千分之一印花税,每笔交易佣金最低扣5块钱
    set_order_cost(OrderCost(close_tax=0.001,open_commission=0.0003,close_commission=0.0003,close_today_commission=0,min_commission=5),type='stock')

    # 为股票设定滑点为百分比滑点
    set_slippage(FixedPercent(0.00246),type='stock')

    # 设置要操作的股票池
    g.security=[]

    # 回测区间、初始资金、运行频率请在下方设置

# 每日开盘前9: 00被调用一次,用于储存自定义参数、全局变量,执行盘前选股等
def before_trading_start(context): 

    # 获取日期
    date=context.current_dt

    # 打印日期
    log.info('{} 盘前运行'.format(date))

def handle_data(context, data): 
    # 获取时间
    time=context.current_dt

    # 打印时间
    log.info('{} 盘中运行'.format(time))

# 收盘后运行函数,用于储存自定义参数、全局变量,执行盘后选股等
def after_trading_end(context): 

    # 获取时间
    time=context.current_dt
    # 打印时间
    log.info('{} 盘后运行'.format(time))
    log.info('一天结束')

if __name__=='__main__': 
    run_main()

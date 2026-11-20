# ZltQuant Python SDK

[返回首页](../README.md) · [全部产品文档](README.md)

使用 Python 编写策略、读取行情与财务数据，并调用策略运行、调度和交易接口。SDK 使用配套研究环境，环境准备见 [ZltQuant MCP / CLI 文档](zltquant-mcp.md#运行环境)与[官方快速开始](https://docs.zltquant.com/api/zltquant/api/functions/getting-started.html)。

## 入门示例

### 使用 Python 读取历史行情

在已完成配置的智量通研究环境中运行。示例依据官方 SDK 文档，初始化和查询可能按环境配置补充本地数据。


```python
from zltquant import init_research, get_price

context = init_research(
    start_time="2024-01-01",
    end_time="2024-06-30",
)

prices = get_price(
    "sz000001",
    start_date="2024-06-01",
    end_date="2024-06-28",
    frequency="daily",
    fields=["time", "open", "high", "low", "close", "volume"],
    df=True,
)
print(prices.tail())
```

`df=True` 返回 DataFrame；未指定时默认返回 NumPy 结构化数组。完整频率、复权和时间参数见 [行情数据接口](https://docs.zltquant.com/api/zltquant/api/functions/market-data.html)。

## 策略模板

[查看仓库内的 14 份官方公开策略模板与示例](../strategies/README.md)。源码标有官方来源，当前仅完成语法检查，未运行回测。

## ZltQuant SDK：开发与数据接口

- [智量通数据库](https://docs.zltquant.com/api/zltquant/api/database/01-query.html)
- [核心资产负债表](https://docs.zltquant.com/api/zltquant/api/database/02-cofinancialrecordbs.html)
- [专业资产负债表](https://docs.zltquant.com/api/zltquant/api/database/03-prfinancerecordbs.html)
- [核心现金流量表＆利润表](https://docs.zltquant.com/api/zltquant/api/database/04-cofinancialrecordiscf.html)
- [专业现金流量表](https://docs.zltquant.com/api/zltquant/api/database/05-prfinancerecordcf.html)
- [专业利润表](https://docs.zltquant.com/api/zltquant/api/database/06-prfinancerecordis.html)
- [分红表](https://docs.zltquant.com/api/zltquant/api/database/07-stk_xr_xd.html)
- [财务数据](https://docs.zltquant.com/api/zltquant/api/financial-data/01-get_fundamentals.html)
- [获取点时间财务数据](https://docs.zltquant.com/api/zltquant/api/financial-data/02-get_fundamentals_pit.html)
- [获取点时间估值衍生指标](https://docs.zltquant.com/api/zltquant/api/financial-data/03-get_valuation_indicators.html)
- [获取点时间经营衍生指标](https://docs.zltquant.com/api/zltquant/api/financial-data/04-get_efficiency_indicators.html)
- [获取点时间现金流衍生指标](https://docs.zltquant.com/api/zltquant/api/financial-data/05-get_cash_flow_indicators.html)
- [获取点时间财务衍生指标](https://docs.zltquant.com/api/zltquant/api/financial-data/06-get_asset_indicators.html)
- [获取点时间增长衍生指标](https://docs.zltquant.com/api/zltquant/api/financial-data/07-get_growth_indicators.html)
- [获取时间范围的估值衍生指标](https://docs.zltquant.com/api/zltquant/api/financial-data/08-get_valuation_indicators_seq.html)
- [获取时间范围的经营衍生指标](https://docs.zltquant.com/api/zltquant/api/financial-data/09-get_efficiency_indicators_seq.html)
- [获取时间范围的现金流衍生指标](https://docs.zltquant.com/api/zltquant/api/financial-data/10-get_cash_flow_indicators_seq.html)
- [获取时间范围的财务衍生指标](https://docs.zltquant.com/api/zltquant/api/financial-data/11-get_asset_indicators_seq.html)
- [获取时间范围的增长衍生指标](https://docs.zltquant.com/api/zltquant/api/financial-data/12-get_growth_indicators_seq.html)
- [获取分红送股数据](https://docs.zltquant.com/api/zltquant/api/financial-data/13-get_dividend.html)
- [基本数据](https://docs.zltquant.com/api/zltquant/api/functions/basic-data.html)
- [债券相关数据](https://docs.zltquant.com/api/zltquant/api/functions/bond-data.html)
- [枚举类型](https://docs.zltquant.com/api/zltquant/api/functions/enum-types.html)
- [扩展数据](https://docs.zltquant.com/api/zltquant/api/functions/extended-data.html)
- [因子数据](https://docs.zltquant.com/api/zltquant/api/functions/factor.html)
- [基金数据（FinORM 数据源）](https://docs.zltquant.com/api/zltquant/api/functions/fund-data.html)
- [期货数据](https://docs.zltquant.com/api/zltquant/api/functions/future-data.html)
- [快速开始](https://docs.zltquant.com/api/zltquant/api/functions/getting-started.html)
- [指数数据](https://docs.zltquant.com/api/zltquant/api/functions/index-data.html)
- [行业数据](https://docs.zltquant.com/api/zltquant/api/functions/industry-data.html)
- [行情数据](https://docs.zltquant.com/api/zltquant/api/functions/market-data.html)
- [规则数据](https://docs.zltquant.com/api/zltquant/api/functions/rule-data.html)
- [策略运行时对象](https://docs.zltquant.com/api/zltquant/api/functions/runtime-objects.html)
- [运行函数](https://docs.zltquant.com/api/zltquant/api/functions/scheduling-functions.html)
- [设置函数](https://docs.zltquant.com/api/zltquant/api/functions/setup-functions.html)
- [状态数据](https://docs.zltquant.com/api/zltquant/api/functions/status-data.html)
- [tick 数据订阅](https://docs.zltquant.com/api/zltquant/api/functions/tick-scheduling.html)
- [时间函数](https://docs.zltquant.com/api/zltquant/api/functions/time-functions.html)
- [交易函数](https://docs.zltquant.com/api/zltquant/api/functions/trading-functions.html)
- [工具函数](https://docs.zltquant.com/api/zltquant/api/functions/utility-functions.html)
- [策略示例](https://docs.zltquant.com/api/zltquant/api/strategy-examples.html)
- [交易规则与常见拒单](https://docs.zltquant.com/api/zltquant/api/trading-rules.html)
- [常见问题](https://docs.zltquant.com/api/zltquant/backtest-and-migration.html)

功能和接口以当前安装版本及官方文档为准。

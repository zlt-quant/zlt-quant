# 智量通使用手册与数据说明

[返回仓库首页](../README.md) · [官方知识库](https://docs.zltquant.com/) · [MCP / CLI 安装说明](https://www.npmjs.com/package/@zltquant/zlt-mcp?activeTab=readme)

本页整理 ZltQuant MCP 数据能力、FinORM 财经数据库目录和官方手册入口。点击下方手册标题可直接阅读官网正文、示例和配图。

## ZltQuant MCP 数据能力

依据 `@zltquant/zlt-mcp@0.11.1` 的工具参数及 2026-11-20 的 `mcp-get-cloud-data-list` 只读查询整理。此次按日线、分钟线、期货、财务与规则、ETF、股票快照分六批列举，六批返回均未截断。

| 类别 | 本次目录返回 |
| --- | --- |
| 股票行情 | 沪深日线、分钟线与快照 |
| 债券行情 | 沪深日线、分钟线 |
| 基金行情 | 沪深日线、分钟线 |
| 指数行情 | 沪深日线、分钟线 |
| 期货行情 | 中金所、郑商所、大商所、上期所、广期所的日线、分钟线与快照 |
| 财务数据 | 专业财务 `pr`、核心财务 `co` |
| ETF 专项 | 沪深 ETF 的多段云端对象区间 |

市场规则 `mr` 在数据工具参数中声明；本次序列表没有单列其日期区间，不能按日期区间判断规则是否落地。北交所标识在参数中支持，但本次未返回相应序列，不据此宣称数据不存在。

云端对象的日期是文件标记边界，不代表每只证券的连续历史或最新真实交易日。部分结束日期晚于核对日，不能解释为行情或财报已更新到未来。账号权限、本地下载和实际可读记录需另行核对。

### 如何查询当前可用数据

| 工具 | 用途 |
| --- | --- |
| `mcp-get-cloud-data-list` | 列举云端对象与范围 |
| `mcp-get-data-range` | 查看本地已下载覆盖 |
| `mcp-get-cache-diff` | 核对云端与缓存差异 |
| `mcp-get-data-disk-space` | 检查磁盘与缓存占用 |
| `mcp-download-data` | 经确认后下载所需数据 |

先查看工具当前参数：

```sh
zlt-mcp list --tool mcp-get-cloud-data-list --json
```

也可以直接向 Agent 提问：

```text
用智量通 MCP 查看沪深股票、指数、基金和债券的日线、分钟线数据目录，
再看五个期货交易所的行情。先只读列举，不下载、不启动回测。
```

下载前明确市场、类型、日期、体量和授权。具体安装、登录与调用方式见 [npm 使用说明](https://www.npmjs.com/package/@zltquant/zlt-mcp?activeTab=readme)。

## 策略模板源码

[查看仓库内的 14 份官方公开策略模板与示例](../strategies/README.md)。源码来自官方文档，已标注来源；本次未运行回测。

## 选择阅读入口

- 第一次开发策略：[SDK 快速开始](https://docs.zltquant.com/api/zltquant/api/functions/getting-started.html)
- 查行情接口：[行情数据](https://docs.zltquant.com/api/zltquant/api/functions/market-data.html)
- 使用现成策略：[策略示例](https://docs.zltquant.com/api/zltquant/api/strategy-examples.html)
- 在 VS Code 中研发：[zlt-claw 插件手册](https://docs.zltquant.com/vscode/)
- 安装投研终端：[终端简介](https://docs.zltquant.com/instructions/terminal-intro.html)

## FinORM 财经数据目录

FinORM 提供按分类、表与字段发现和查询的财经数据库能力。以下目录根据[官方数据范围](https://docs.zltquant.com/finorm/data-scope.html)整理，核对日期为 2026-11-20，共 **15 个数据库、476 张表、8,376 个业务字段**。它与上文按市场、频率组织的 ZltQuant 云端下载目录各有用途，目录规模不作为下载覆盖的证明。

| 数据库与字段明细 | 内容 | 表数 | 字段数 |
| --- | --- | --- | --- |
| [A股 cneqa](https://docs.zltquant.com/finorm/data-scope/cneqa.html) | 沪深京 A/B 股的行情、财报、股东、股本、事件、板块与治理数据，是最完整的一个库。 | 163 | 4462 |
| [行业与商品 cnsect](https://docs.zltquant.com/finorm/data-scope/cnsect.html) | 申万等行业分类，以及能源、材料、农产品、房地产等各细分市场的价格指数与产销数据。 | 142 | 841 |
| [公募基金 cnmf](https://docs.zltquant.com/finorm/data-scope/cnmf.html) | 基金基本信息、净值、持仓、经理、评级，以及 ETF、LOF、REITs 专项数据。 | 54 | 1042 |
| [宏观统计 cnstat](https://docs.zltquant.com/finorm/data-scope/cnstat.html) | 国民经济核算、工业增加值、价格指数、国内贸易、固定资产投资等国家统计口径数据。 | 26 | 351 |
| [期货 cnfut](https://docs.zltquant.com/finorm/data-scope/cnfut.html) | 期货合约与品种参数、交割与仓单、日行情、资金流向与持仓排名。 | 19 | 491 |
| [债券 cnbnd](https://docs.zltquant.com/finorm/data-scope/cnbnd.html) | 可转债条款与转股、债券估值、信用事件、银行间回购拆借行情。 | 15 | 529 |
| [海关进出口 cngac](https://docs.zltquant.com/finorm/data-scope/cngac.html) | 海关总署口径的进出口总值、商品构成、重点商品量值与分地区分企业性质统计。 | 15 | 112 |
| [资讯与研报 intel](https://docs.zltquant.com/finorm/data-scope/intel.html) | 财经日历、行业新闻、交易所互动易、机构研报评级与资讯标签体系。 | 12 | 210 |
| [指数 gbidx](https://docs.zltquant.com/finorm/data-scope/gbidx.html) | 指数基本信息、分类、成分股与权重，覆盖中证、国证及衍生指数。 | 9 | 116 |
| [主数据 main](https://docs.zltquant.com/finorm/data-scope/main.html) | 证券信息主表、行情代码映射、个人信息与自定义板块配置，常用于跨库联表。 | 8 | 92 |
| [美国经济分析局 usbea](https://docs.zltquant.com/finorm/data-scope/usbea.html) | 美国 GDP 行业分解与国际贸易、跨国服务投资数据。 | 4 | 38 |
| [董监高与股东 cneqn](https://docs.zltquant.com/finorm/data-scope/cneqn.html) | 董监高人员基本情况与持股，以及十大股东情况。 | 3 | 36 |
| [美国劳工统计局 usbls](https://docs.zltquant.com/finorm/data-scope/usbls.html) | 美国 CPI、PPI 与进出口价格指数。 | 3 | 35 |
| [港股 hkeq](https://docs.zltquant.com/finorm/data-scope/hkeq.html) | 港股 ETF 庄家信息与单位净值变动。 | 2 | 12 |
| [美联储 usfed](https://docs.zltquant.com/finorm/data-scope/usfed.html) | 美国货币供应量。 | 1 | 9 |

[按表名或表编码搜索完整目录](https://docs.zltquant.com/finorm/table-catalog.html) · [快速开始](https://docs.zltquant.com/finorm/getting-started.html) · [安装说明](https://docs.zltquant.com/finorm/installation.html) · [查询示例](https://docs.zltquant.com/finorm/examples.html) · [接口参考](https://docs.zltquant.com/finorm/api-reference.html)

以上为平台公开目录，实际可查表由账号授权决定；可读区间、字段和时间轴以当前服务规范为准。点击库名可查看全部表与字段。本仓库不提供财经数据记录下载，也不授予数据再分发权限。

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

## 投研终端手册

- [基础操作](https://docs.zltquant.com/instructions/basic-operations.html)
- [实验室](https://docs.zltquant.com/instructions/laboratory.html)
- [行情模块](https://docs.zltquant.com/instructions/market-module.html)
- [投研模块](https://docs.zltquant.com/instructions/research-module.html)
- [策略交易](https://docs.zltquant.com/instructions/strategy-trading.html)
- [终端简介](https://docs.zltquant.com/instructions/terminal-intro.html)
- [交易模块](https://docs.zltquant.com/instructions/trading-module.html)
- [更新说明](https://docs.zltquant.com/instructions/update-notes.html)

## VS Code 插件手册

- [智量通插件使用说明书](https://docs.zltquant.com/vscode/)
- [更新日志](https://docs.zltquant.com/vscode/CHANGELOG.html)

## 文档与数据口径

本页链接指向官方知识库；功能及接口以当前安装版本和官网说明为准。ZltQuant 下载数据说明来自 MCP 实查；FinORM 数据库目录来自官网公开数据范围，账号授权与实时可用性另行核对。

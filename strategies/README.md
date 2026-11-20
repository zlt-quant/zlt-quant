# 官方策略模板与示例

[返回仓库首页](../README.md) · [官方策略示例](https://docs.zltquant.com/api/zltquant/api/strategy-examples.html) · [SDK 快速开始](https://docs.zltquant.com/api/zltquant/api/functions/getting-started.html)

这里收录 **14 份官方公开 Python 模板与示例**。点击文件名可直接阅读源码；需要使用时，可下载后按平台工作区要求保存为 `main.py`。代码正文按官网保留，文件头注明原文来源，整理日期为 2026-11-20。

## 基础框架

| 模板 | 源码 | 用途 |
| --- | --- | --- |
| 基础模版1 | [basic-template.py](basic-template.py) | 策略初始化、调度与交易的基础框架 |
| 基础模版2 | [scheduled-template.py](scheduled-template.py) | 按固定时间调度的基础框架 |
| 多账号策略模版 | [multi-account-template.py](multi-account-template.py) | 通过 pindex 区分账号的策略框架 |
| 期货策略模版 | [futures-template.py](futures-template.py) | 期货交易的基础框架 |
| Tick回测策略模版 | [tick-backtest-template.py](tick-backtest-template.py) | Tick 回调与历史 Tick 查询示例 |
| Tick仿真策略模版 | [tick-simulation-template.py](tick-simulation-template.py) | Tick 订阅与仿真回调示例 |

## 策略示例

| 示例 | 源码 | 用途 |
| --- | --- | --- |
| 均线择时 | [ma-timing.py](ma-timing.py) | EMA / MACD 择时示例 |
| 趋势跟踪 | [trend-following.py](trend-following.py) | 按官网“趋势跟踪”名称保留的示例 |
| 海龟交易法则 | [turtle-trading.py](turtle-trading.py) | 突破、加仓与退出逻辑示例 |
| 布林线均值回归 | [bollinger-mean-reversion.py](bollinger-mean-reversion.py) | 布林带触发的交易示例 |
| 均值回复策略 | [mean-reversion.py](mean-reversion.py) | 均值回复示例 |
| 多因子选股 | [multi-factor-selection.py](multi-factor-selection.py) | 多因子选股示例 |
| 小市值策略 | [small-cap.py](small-cap.py) | 小市值选股示例 |
| 股票配对交易 | [pairs-trading.py](pairs-trading.py) | 股票配对交易示例 |

## 使用方式

1. 按[仓库安装说明](../README.md#安装方法)准备智量通 CLI / MCP 和配套研究环境。
2. 在平台创建独立策略工作区，按实际返回路径编辑源码；平台模板优先从实时列表选择。
3. 将所选示例作为参考，核对标的、频率、参数、调度方式、成本和数据覆盖。
4. 在本地回测环境验证后，再分析收益、委托与报告。

Tick 仿真和多账号示例包含下单调用，使用前需按对应手册确认账号及运行模式。本次只整理源码并通过 Python 语法检查，未运行策略、仿真或回测。第三方库需求见各文件的 import 以及当前研究环境。

## 平台模板目录

2026-11-20 使用 `mcp-strategy-get-template-list` 查询到以下 13 项，返回未分页截断。下表是平台条目；上面的公开源码来自官网手册，不宣称与客户端当前模板逐字一致。

| 平台名称 | 本次返回标识 | 公开源码入口 |
| --- | --- | --- |
| 交易模版 | `A1` | 见上方基础框架；不作源码等同声明 |
| 均线择时 | `A2` | [官网同名示例](ma-timing.py) |
| 布林线均值回归 | `A3` | [官网同名示例](bollinger-mean-reversion.py) |
| 多因子选股 | `A4` | [官网同名示例](multi-factor-selection.py) |
| 趋势跟踪 | `A5` | [官网同名示例](trend-following.py) |
| 均值回复策略 | `A6` | [官网同名示例](mean-reversion.py) |
| 海龟交易法则 | `A7` | [官网同名示例](turtle-trading.py) |
| 小市值策略 | `A8` | [官网同名示例](small-cap.py) |
| 股票配对交易 | `A9` | [官网同名示例](pairs-trading.py) |
| tick策略回测 | `A10` | [官网同名示例](tick-backtest-template.py) |
| tick仿真策略 | `A11` | [官网同名示例](tick-simulation-template.py) |
| 行业轮动（月频） | `A12` | 当前官网页面未提供此项源码，请在平台通过 MCP 获取 |
| 日内回转（T+0） | `A13` | 当前官网页面未提供此项源码，请在平台通过 MCP 获取 |

创建前需重新查询平台列表，使用当次返回的 `val`，不长期硬编码本页标识：

```sh
zlt-mcp list --tool mcp-strategy-get-template-list --json
zlt-mcp call mcp-strategy-get-template-list
```

## 来源与许可

[机器可读目录与来源记录](catalog.json)包含原文链接、正文 SHA-256 和本次平台目录。示例与组件的使用许可遵循智量通官方说明，未另行声明为 MIT 等开源许可。示例不构成收益承诺或投资建议，历史回测表现不代表未来收益。

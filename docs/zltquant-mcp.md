# ZltQuant MCP / CLI / Skill

[返回首页](../README.md) · [全部产品文档](README.md)

通过 AI Agent、命令行或 MCP 客户端使用智量通，完成行情查询、数据准备、策略开发、因子研究与本地回测。

## 主要功能

| 功能 | 可以做什么 |
| --- | --- |
| 行情查询 | 查看 A 股大盘、个股盘口、分时、资金动向与龙头观察面板 |
| 数据准备 | 查看云端数据目录、本地覆盖与缺口，按需下载回测数据 |
| 策略开发 | 获取官方模板，创建、编写或迁移 Python 策略 |
| 本地回测 | 运行股票、场内基金、可转债和期货回测，分析收益、委托与报告 |
| 因子研究 | 创建因子、计算因子值，查看 IC、分层收益和换手率等检测结果 |

## 运行环境

| 使用方式 | 环境要求 |
| --- | --- |
| Skill / CLI / MCP | Node.js 20 或更高版本；Windows x64 或 macOS |
| AI Agent | 支持 Skills 并能运行终端命令，或支持 MCP 的客户端 |
| 本地研究与回测 | 配套 ClientLite 研究环境；当前自动安装流程支持 Windows x64、macOS ARM64 |

行情面板查询无需安装本地回测环境。Python SDK 使用配套研究环境，安装与平台要求见 [npm 文档](https://www.npmjs.com/package/@zltquant/zlt-mcp?activeTab=readme) 和 [终端安装手册](https://docs.zltquant.com/instructions/terminal-intro.html)。

## 安装方法

### 在 AI Agent 中安装 Skill

适用于 Codex、WorkBuddy 等支持 Skills 的 Agent。打开 [SkillHub 页面](https://skillhub.cn/skills/org-gir79457/zlt-quant)，或将下面的内容发送给 Agent：


```text
请根据 https://skillhub.cn/install/skillhub.md，安装 @org-gir79457/zlt-quant。
```

安装完成后，在新会话中描述任务，Skill 会引导登录和环境准备。

### 在终端中安装 CLI


```sh
npm install --global @zltquant/zlt-mcp
zlt-mcp auth login
```

按提示在浏览器中完成登录授权，再查看可用工具：


```sh
zlt-mcp list
zlt-mcp list --tool show_stock_panel --json
```

### 接入 MCP 客户端

先完成上面的登录，再在客户端添加配置。Windows 示例：


```json
{
  "mcpServers": {
    "zlt-quant": {
      "command": "npx.cmd",
      "args": ["-y", "@zltquant/zlt-mcp"]
    }
  }
}
```

macOS 将 `npx.cmd` 改为 `npx`。配置位置和生效方式以所用客户端说明为准。

## 使用示例

### 查询 A 股行情

在 Agent 中提出任务：


```text
用智量通查看今天 A 股大盘行情，说明涨跌分布和成交额，保留数据时间。
```

也可以直接在终端调用：


```sh
zlt-mcp call show_market_panel
```

### 查看数据目录


```text
用智量通 MCP 查看沪深股票、指数、基金和期货的云端数据目录，
列出可用类别与日期范围。先只读查询。
```

云端目录与本地已下载数据分别核对：`mcp-get-cloud-data-list` 查看云端，`mcp-get-data-range` 查看本地覆盖。目录中的日期边界不代表每只证券都有连续历史。

### 运行一次回测


```text
用智量通官方交易模板，对平安银行做一次日线回测，初始资金 100 万。
先核对数据覆盖；安装环境或下载数据前，说明范围并让我确认。
完成后打开报告，解释收益、回撤和结果限制。
```

本地回测支持沪深 A 股、场内基金、可转债和期货；北交所与期权暂不支持。品种与交易规则见 [回测说明](https://docs.zltquant.com/api/zltquant/backtest-and-migration.html)。

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

## 策略与相关产品

- [官方策略模板与 Python 示例](../strategies/README.md)
- [Python SDK 文档](python-sdk.md)
- [FinORM 财经数据 MCP 文档](finorm.md)

## 版本更新

[CLI / MCP 版本记录](https://www.npmjs.com/package/@zltquant/zlt-mcp?activeTab=versions)

## 常见问题

**查询行情和运行回测，需要同一套环境吗？**

行情面板查询无需本地回测环境；本地回测需要准备 ClientLite 研究环境和对应数据。

**云端有数据，为什么本地仍无法回测？**

云端目录不代表本地已下载。先检查本地覆盖、标的、日期与频率，再准备所需数据；拿到任务 ID 后，应继续等待任务完成。

**克隆这个仓库就能直接运行吗？**

本仓库提供介绍和文档。请通过上面的 SkillHub 或 npm 入口安装工具，再按手册准备研究环境。

更多问题见 [回测与迁移说明](https://docs.zltquant.com/api/zltquant/backtest-and-migration.html)。

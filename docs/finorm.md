# FinORM 财经数据库与 MCP

[返回首页](../README.md) · [全部产品文档](README.md)

FinORM 提供财经数据目录发现、字段规范查询和数据查询。下面分别列出数据库范围与 MCP 安装方法。

[数据目录](#finorm-财经数据目录) · [MCP 安装](#安装-finorm-mcp) · [Codex 手动配置](#手动配置-codex) · [连接验证](#验证连接)

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

## 安装 FinORM MCP

FinORM MCP 随官方 Python 客户端 `ZltFinOrmClient` 提供，用于让 AI 助手发现财经数据分类、表和字段并执行查询。它与 `@zltquant/zlt-mcp` 分别安装。以下步骤依据[官方安装手册](https://docs.zltquant.com/finorm/installation.html)，核对日期为 2026-11-20。

### 环境与访问凭据

使用 **Python 3.10 或更高版本**。联系官方客服 [kefu@zltquant.com](mailto:kefu@zltquant.com) 获取服务地址（endpoint）和 `fk_` 开头的 token，并开通所需数据权限。配置示例中的值需要替换；真实 token 仅保存在本机，不要提交到 GitHub。

### 安装与注册

先从公共源安装依赖，再从智量通官方源安装客户端：

```sh
python -m pip install pandas numpy pyarrow mcp --index-url https://pypi.tuna.tsinghua.edu.cn/simple
python -m pip install ZltFinOrmClient --index-url https://pypip.zltquant.com/
python -c "import zlt_finorm_client; print(zlt_finorm_client.__version__)"
```

智量通源仅提供自有包，不能代替上面的公共依赖源，也不要将其设置为 pip 的全局源。

注册 MCP，将下面的 endpoint 和 token 替换为客服提供的值：

```sh
zltfinorm install-mcp --endpoint http://finorm.zltquant.com:7761 --token fk_YOUR_TOKEN
```

该命令会写入 AI 助手的 MCP 配置，完成后重启助手。可另装配套 Skill，帮助助手按目录和字段规范查询；例如 Codex：

```sh
zltfinorm install-skill --agent codex
```

Claude Code 使用 `--agent claude`。不指定 `--agent` 时，Skill 安装命令默认面向本机支持的所有助手。

### 手动配置 Codex

自动注册未生效时，在本机 `~/.codex/config.toml` 中添加下列配置；已有同名配置时修改现有项。先查询当前 Python 环境中的命令路径：

```sh
python -c "import shutil; print(shutil.which('zltfinorm'))"
```

把输出的完整路径填入 `command`。Windows 示例使用正斜杠，避免反斜杠转义问题：

```toml
[mcp_servers.finorm]
command = "C:/path/to/python/Scripts/zltfinorm.exe"
args = ["mcp"]

[mcp_servers.finorm.env]
FINORM_ENDPOINT = "http://finorm.zltquant.com:7761"
FINORM_TOKEN = "fk_YOUR_TOKEN"
```

macOS / Linux 同样使用上面命令查出的实际可执行文件路径。支持 `mcpServers` JSON 格式的客户端可参考[官方手动配置示例](https://docs.zltquant.com/finorm/installation.html#命令没生效时手动配)，按各自配置位置添加 `command`、`args` 和环境变量。

### 验证连接

重启助手后检查 MCP 连接状态；Claude Code 可用 `/mcp` 查看 `finorm`。随后向助手提问：

```text
用 FinORM MCP 列出当前可用的数据分类，再查找 A 股基本信息表并查看字段规范。
先只读查看目录和字段，不导出数据。
```

若服务启动失败，检查 Python 版本、可执行文件完整路径、依赖以及 endpoint / token 配置。终端直接运行 `zltfinorm mcp` 时，正常情况下会等待协议输入；可用 Ctrl+C 退出。更多步骤见[官方安装手册](https://docs.zltquant.com/finorm/installation.html)。

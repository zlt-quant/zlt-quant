# 智量通 ZLT Quant

让 AI Agent 帮你完成行情查询、金融数据研究、因子研究、策略开发和回测分析。

通过智量通 Skill 或 MCP 工具，你可以用自然语言提出研究任务，由 Agent 按相应工作流调用智量通平台能力。

本仓库用于发布智量通的产品介绍、安装指引和交流信息。

**[获取 Skill](https://skillhub.cn/skills/org-gir79457/zlt-quant)** · **[查看 npm 工具包](https://www.npmjs.com/package/@zltquant/zlt-mcp)** · **[加入交流群](#交流与支持)**

## 可以做什么

| 场景 | 主要能力 |
| --- | --- |
| 行情查询 | 查看 A 股大盘、个股及龙头行情面板 |
| 金融数据研究 | 查找金融数据表，查看字段与查询条件，提取研究数据 |
| 因子研究与选股 | 研究因子、按条件筛选股票，查看因子检测结果 |
| 策略开发 | 使用官方模板创建策略，编写或迁移 Python 策略 |
| 本地回测与分析 | 检查数据覆盖，运行股票、期货回测，查看结果与报告 |

## 快速开始

### 方式一：在 AI Agent 中安装 Skill

适用于支持 Skills 且能运行终端命令的 Agent，例如 Codex、WorkBuddy。

打开 [智量通 Skill 页面](https://skillhub.cn/skills/org-gir79457/zlt-quant)，按页面提示安装。也可以将以下内容发送给你的 Agent：

```text
请根据 https://skillhub.cn/install/skillhub.md，安装 @org-gir79457/zlt-quant。
```

安装完成后，在新会话中描述任务。Skill 会按需引导登录及环境准备。

你可以这样提问：

```text
用智量通查看今天的 A 股大盘行情面板。
```

```text
用智量通查询平安银行最近一期财务数据，说明数据来源和字段单位。
```

```text
用智量通的官方交易模板，对平安银行做一次日线回测，初始资金 100 万。
完成后打开报告。需要安装环境、下载数据或登录时先让我确认。
```

### 方式二：在终端使用 CLI

需要 **Node.js 20 或更高版本**，支持 Windows x64 和 macOS。

安装工具并登录：

```sh
npm install --global @zltquant/zlt-mcp
zlt-mcp auth login
```

按提示在浏览器中完成授权，然后查看工具列表或查询大盘行情：

```sh
zlt-mcp list
zlt-mcp call show_market_panel
```

行情和金融数据查询无需安装本地回测环境。本地回测需要另外准备 ClientLite 研究环境，当前自动安装流程支持 Windows x64 和 macOS ARM64。安装步骤与平台限制见 [npm 使用文档](https://www.npmjs.com/package/@zltquant/zlt-mcp?activeTab=readme)。

### 方式三：接入支持 MCP 的客户端

先按上文完成登录，再在客户端添加配置。Windows 示例：

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

macOS 将 `command` 改为 `npx`。配置入口和生效方式以所用客户端的说明为准。

## 交流与支持

欢迎加入 **智量通投研技术交流群**，交流安装配置、使用问题和量化研究经验。

**QQ 群号：516777591**。可使用 QQ 扫描下方二维码，或搜索群号申请加入。

<img src="qq-group.jpg" alt="智量通投研技术交流群 QQ 群二维码，群号 516777591" width="360">

## 使用说明

- 可用数据与功能以当前版本、账号权限及平台实际返回为准。
- 回测和研究结果仅供研究参考，不构成投资建议，历史表现不代表未来收益。
- 智量通专有组件限个人、非商业研究使用；商用需另行书面授权。具体以相应组件随附的产品许可及第三方声明为准。

## 相关链接

- [智量通 Skill：安装入口与工作流说明](https://skillhub.cn/skills/org-gir79457/zlt-quant)
- [@zltquant/zlt-mcp：CLI 与 MCP 使用文档](https://www.npmjs.com/package/@zltquant/zlt-mcp?activeTab=readme)

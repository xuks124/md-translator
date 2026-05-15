<div align="center">

# AI 批量 Markdown 翻译工具 📝🌍

### 一键翻译整站文档，格式零丢失，支持 20+ AI 模型

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/xuks124/md-translator)](https://github.com/xuks124/md-translator)

</div>

---

## 👀 这工具解决什么问题？

**场景：** 你写了一整套中文技术文档（或者教程、API文档、产品手册），想翻译成英文/日文出海。

**传统做法：** 
- 复制到ChatGPT → 翻完格式全乱 → 手动调格式 → 要吐了
- 找翻译公司 → 一星期 + 几千块

**这个方案：** `python translate.py --input ./docs --target-lang en` → 喝完杯咖啡回来，所有文件翻译好了，格式完美保留。

## ✨ 核心亮点

| 功能 | 说明 |
|------|------|
| 🔄 **批量翻译** | 一次处理整个目录，几百个文件 OK |
| 🎨 **格式零丢失** | 标题/列表/代码块/表格/链接/图片 全部保留 |
| 🔌 **20+ 模型** | OpenAI / DeepSeek / Claude / 通义千问 / One-API 中转 |
| ⚡ **并发翻译** | 5 个文件同时翻，速度 10x |
| ▶️ **断点续传** | 翻到一半断了？重跑接着翻，不重复 |
| 💰 **低成本** | One-API 中转只要官方价的 1/5 |
| 🌐 **多语言** | 中⇄英⇄日⇄韩⇄法⇄德 互翻 |

## 🚀 3 分钟上手

```bash
# 1. 安装
git clone https://github.com/xuks124/md-translator.git
cd md-translator
pip install -r requirements.txt

# 2. 配置（支持任何 OpenAI 兼容 API）
export API_KEY="sk-xxx"
export API_BASE="https://api.openai.com/v1"

# 3. 运行 — 把 ./docs 目录下的所有 .md 翻译成英文
python translate.py --input ./docs --target-lang en
```

## ⚙️ 配置项一览

| 环境变量 | 说明 | 默认值 |
|----------|------|--------|
| `API_KEY` | API 密钥 | **必填** |
| `API_BASE` | API 地址 | `https://api.openai.com/v1` |
| `MODEL` | 模型名称 | `deepseek-chat` |
| `CONCURRENCY` | 并发数 | 5 |
| `TARGET_LANG` | 目标语言 | en |

> 💡 **省钱技巧：** 用 One-API 中转（[www.9hcn.pw](https://www.9hcn.pw)），接入 DeepSeek / Qwen 等国产模型，翻译 10 万字才几毛钱。

## 📊 效果对比

| 对比项 | 手动 ChatGPT | md-translator |
|--------|-------------|---------------|
| 100个文件耗时 | 2-3 天 | **3 分钟** |
| 格式是否完整 | ❌ 经常乱 | ✅ 完全保留 |
| 费用（10万字） | ¥50-100 | **¥1-3** |
| 断点续传 | ❌ | ✅ |
| 需要盯着 | ✅ | ❌ 后台跑即可 |

## 💰 这个工具能帮你赚钱的 3 种方式

### 1️⃣ 文档翻译服务（当天接单）
在闲鱼/淘宝挂"技术文档AI翻译"，别人把文档发给你，一分钟搞定。
- 定价：¥0.1-0.3/千字
- 100 页文档 ≈ ¥30-50
- **纯自动化，0 成本**

### 2️⃣ 教程出海卖钱
把你的中文教程/电子书翻译成英文，放到 Gumroad 卖。
- 定价：$10-50/份
- 翻译成本：几乎为 0

### 3️⃣ 企业私有部署
帮企业把内部文档翻译系统部署到内网，收服务费。
- 定价：¥500-2000/次

## 💻 命令参考

```bash
# 基本用法
python translate.py --input ./docs --target-lang en

# 指定输出目录
python translate.py --input ./docs --output ./en-docs --target-lang en

# 指定模型
python translate.py --input ./docs --model gpt-4 --target-lang ja

# 指定源语言（默认自动检测）
python translate.py --input ./docs --source-lang zh --target-lang en

# 强制重新翻译所有文件（忽略缓存）
python translate.py --input ./docs --target-lang en --force

# 翻译单个文件
python translate.py --input ./docs/intro.md --target-lang en
```

## 📁 项目结构

```
├── translate.py        # 核心翻译脚本
├── config.py           # 配置管理
├── requirements.txt    # 依赖
├── README.md           # 中文说明
├── README_EN.md        # English docs
└── test/               # 测试用例
```

## 📄 License

MIT — 随便用，随便改，甚至拿去卖钱也行。

---

**如果这个工具帮到了你，点个 ⭐ 支持一下！**

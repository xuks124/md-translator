<div align="center">

# AI 批量 Markdown 翻译工具 📝🌍

### 利用 AI 一键翻译整站文档，保持格式、支持多模型、断点续传

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

</div>

---

## 🎯 这工具解决什么问题？

**场景：** 你写了一套中文技术文档，想出海翻译成英文/日文/其他语言。

**痛点：** 手动翻译太慢，复制到 ChatGPT 再粘回来格式全乱。

**方案：** `md-translator` — 一键翻译整个目录的 .md 文件，格式完美保留。

## ✨ 功能亮点

| 功能 | 说明 |
|------|------|
| 🔄 **批量翻译** | 一次处理整个目录，几百个文件没问题 |
| 🎨 **格式保留** | Markdown 标题、列表、代码块、表格全保留 |
| 🔌 **多模型** | 支持 OpenAI / DeepSeek / 通义千问 / One-API |
| ⚡ **并发** | 多线程同时翻译，速度快 10 倍 |
| ▶️ **断点续传** | 翻译到一半断了，重跑接着来 |
| 🌐 **多语言** | 中→英→日→韩→法→德 随便选 |

## 🚀 快速开始

```bash
# 1. 装
git clone https://github.com/xuks124/md-translator.git
cd md-translator
pip install -r requirements.txt

# 2. 配
export API_KEY="sk-你的密钥"
export API_BASE="https://api.openai.com/v1"

# 3. 跑
python translate.py --input ./docs --target-lang en
```

## ⚙️ 配置项

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `API_KEY` | API 密钥 | 必填 |
| `API_BASE` | API 地址 | `https://api.openai.com/v1` |
| `MODEL` | 模型名称 | `deepseek-chat` |
| `CONCURRENCY` | 并发数 | `5` |
| `TARGET_LANG` | 目标语言 | `en` |

> 💡 **省钱提示：** 用 One-API 中转（比如 [www.9hcn.pw](https://www.9hcn.pw)）可以便宜 80%，不用绑信用卡。

## 💰 用这个怎么赚钱？

| 方式 | 说明 | 定价参考 |
|------|------|----------|
| 📄 **文档翻译服务** | 帮别人翻译技术文档 | ¥0.1-0.3/千字 |
| 🛠️ **私有部署** | 帮企业部署到内部 | ¥500-2000/次 |
| 🎓 **教程出海** | 把自己的教程翻译成英文卖 | 定价 $10-50/份 |

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

MIT — 随便用，随便改

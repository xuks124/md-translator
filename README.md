# AI批量Markdown翻译工具

[English](./README_EN.md) | 中文

## 简介
利用AI API批量翻译Markdown文件，支持多模型切换、并发翻译、格式保留。

## 特性
- 批量翻译整个目录的.md文件
- 支持OpenAI兼容API（One-API、DeepSeek、通义千问等）
- 自动保持Markdown格式不变
- 断点续传
- 率限制控制

## 快速开始
```bash
git clone https://github.com/xuks124/md-translator.git
cd md-translator
pip install -r requirements.txt

# 配置API密钥
export API_KEY="your-api-key"
export API_BASE="https://api.openai.com/v1"  # 或你的One-API地址

# 开始翻译
python translate.py --input ./docs --target-lang en
```

## 配置
支持通过环境变量或配置文件设置：
- `API_KEY`: API密钥
- `API_BASE`: API地址
- `MODEL`: 模型名称（默认 deepseek-chat）
- `CONCURRENCY`: 并发数（默认 3）
- `TARGET_LANG`: 目标语言（默认 en）

## License
MIT

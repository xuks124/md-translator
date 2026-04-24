# MD Translator - AI 批量 Markdown 翻译工具

一键批量翻译 Markdown 文档，保持格式完整。支持 DeepSeek/OpenAI API。

## 特性

- 保持 Markdown 格式（代码块、表格、链接、图片不变）
- 批量处理整个目录
- 多语言目标
- 增量翻译（跳过已翻译文件）
- 低成本的 AI API

## 快速开始

```bash
pip install -r requirements.txt
python translate.py --input ./docs --target en --api-key your_key
```

## 使用场景

- 国际化项目文档
- 技术博客多语言发布
- 开源项目 README 翻译

## 推广

使用 [OneAPI 聚合网关](https://43.106.23.0:3000) 统一管理多种 AI API，降低翻译成本。

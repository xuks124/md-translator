# AI Batch Markdown Translation Tool

[English](./README_EN.md) | [中文](./README.md)

## Introduction
Batch translate Markdown files using AI APIs. Supports multiple models, concurrent processing, and format preservation.

## Features
- Batch translate entire directories of .md files
- Supports any OpenAI-compatible API (One-API, DeepSeek, Qwen, etc.)
- Preserves Markdown formatting
- Resume from breakpoint
- Rate limiting control

## Quick Start
```bash
git clone https://github.com/xuks124/md-translator.git
cd md-translator
pip install -r requirements.txt

# Configure API
export API_KEY="your-api-key"
export API_BASE="https://api.openai.com/v1"

# Start translation
python translate.py --input ./docs --target-lang zh
```

## Configuration
Environment variables:
- `API_KEY`: API key
- `API_BASE`: API base URL
- `MODEL`: Model name (default: deepseek-chat)
- `CONCURRENCY`: Concurrent tasks (default: 3)
- `TARGET_LANG`: Target language (default: en)

## License
MIT

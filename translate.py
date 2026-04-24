#!/usr/bin/env python3
"""
MD Translator - 批量 Markdown 翻译工具
支持 DeepSeek/OpenAI API，保持格式完整
"""

import os
import sys
import json
import argparse
import hashlib
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    import requests
except ImportError:
    print("请先安装依赖: pip install requests")
    sys.exit(1)

# 默认 API 配置
DEFAULT_API_URL = "https://api.deepseek.com/v1/chat/completions"
DEFAULT_MODEL = "deepseek-chat"

PROMPT_TEMPLATE = """You are a professional translator. Translate the following Markdown content from {source_lang} to {target_lang}.
Rules:
1. Keep ALL Markdown syntax unchanged (code blocks ```, tables |, links [], images ![], headers #, lists -, etc.)
2. Only translate the text content
3. Keep code blocks content unchanged
4. Keep URLs unchanged
5. Return ONLY the translated content, no explanations

Content to translate:
---
{content}
---"""


def file_hash(content):
    return hashlib.md5(content.encode()).hexdigest()[:8]


def load_cache(cache_file):
    if cache_file.exists():
        with open(cache_file, 'r') as f:
            return json.load(f)
    return {}


def save_cache(cache_file, cache):
    cache_file.parent.mkdir(parents=True, exist_ok=True)
    with open(cache_file, 'w') as f:
        json.dump(cache, f)


def translate_chunk(chunk, source_lang, target_lang, api_key, api_url, model):
    prompt = PROMPT_TEMPLATE.format(
        source_lang=source_lang,
        target_lang=target_lang,
        content=chunk
    )
    
    try:
        resp = requests.post(
            api_url,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.3,
                "max_tokens": 4096
            },
            timeout=60
        )
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"\n\n[翻译错误: {str(e)}]\n\n"


def process_file(md_path, source_lang, target_lang, api_key, api_url, model, output_dir, force):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    rel_path = md_path.relative_to(md_path.parent if output_dir else Path.cwd())
    
    # 缓存路径
    cache_file = Path(md_path.parent / '.md_translator_cache' / f"{md_path.stem}.json")
    cache = load_cache(cache_file)
    
    content_hash = file_hash(content)
    
    # 检查缓存
    if not force and content_hash in cache:
        translated = cache[content_hash]
        print(f"  [缓存命中] {md_path.name}")
    else:
        print(f"  [翻译中] {md_path.name} ({len(content)} chars)")
        
        # 分段翻译（超过4000字符的分段）
        if len(content) > 4000:
            chunks = []
            chunk_size = 3000
            for i in range(0, len(content), chunk_size):
                chunks.append(content[i:i + chunk_size])
            
            translated_parts = []
            for chunk in chunks:
                result = translate_chunk(chunk, source_lang, target_lang, api_key, api_url, model)
                translated_parts.append(result)
            
            translated = '\n'.join(translated_parts)
        else:
            translated = translate_chunk(content, source_lang, target_lang, api_key, api_url, model)
        
        # 保存缓存
        cache[content_hash] = translated
        save_cache(cache_file, cache)
    
    # 输出路径
    if output_dir:
        output_path = Path(output_dir) / md_path.name
    else:
        suffix_map = {
            'en': '.en.md',
            'ja': '.ja.md', 
            'ko': '.ko.md',
            'zh': '.zh.md',
        }
        suffix = suffix_map.get(target_lang, f'.{target_lang}.md')
        output_path = md_path.parent / md_path.name.replace('.md', suffix)
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(translated)
    
    return output_path


def main():
    parser = argparse.ArgumentParser(description="批量 Markdown 翻译工具")
    parser.add_argument("--input", "-i", required=True, help="输入目录或文件")
    parser.add_argument("--source", "-s", default="zh", help="源语言 (default: zh)")
    parser.add_argument("--target", "-t", default="en", help="目标语言 (default: en)")
    parser.add_argument("--api-key", "-k", help="API Key (或设置 MD_TRANSLATOR_KEY 环境变量)")
    parser.add_argument("--api-url", "-u", default=DEFAULT_API_URL, help=f"API URL (default: {DEFAULT_API_URL})")
    parser.add_argument("--model", "-m", default=DEFAULT_MODEL, help=f"模型名 (default: {DEFAULT_MODEL})")
    parser.add_argument("--output", "-o", help="输出目录")
    parser.add_argument("--force", "-f", action="store_true", help="强制重新翻译")
    parser.add_argument("--workers", "-w", type=int, default=3, help="并发数 (default: 3)")
    
    args = parser.parse_args()
    
    api_key = args.api_key or os.environ.get("MD_TRANSLATOR_KEY")
    if not api_key:
        print("错误: 请提供 --api-key 或设置 MD_TRANSLATOR_KEY 环境变量")
        sys.exit(1)
    
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"错误: 路径不存在: {input_path}")
        sys.exit(1)
    
    # 收集所有 md 文件
    md_files = []
    if input_path.is_file():
        if input_path.suffix == '.md':
            md_files.append(input_path)
    else:
        for f in sorted(input_path.glob("**/*.md")):
            if '.md_translator_cache' not in str(f):
                md_files.append(f)
    
    if not md_files:
        print("未找到 .md 文件")
        sys.exit(0)
    
    print(f"找到 {len(md_files)} 个 Markdown 文件，开始翻译...")
    print(f"源语言: {args.source} -> 目标语言: {args.target}")
    print(f"API: {args.api_url} | 模型: {args.model}")
    print("-" * 60)
    
    results = []
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(
                process_file, f, args.source, args.target,
                api_key, args.api_url, args.model, args.output, args.force
            ): f for f in md_files
        }
        for future in as_completed(futures):
            f = futures[future]
            try:
                output = future.result()
                results.append((f, output))
            except Exception as e:
                print(f"  [失败] {f.name}: {e}")
    
    print("-" * 60)
    print(f"完成! {len(results)}/{len(md_files)} 文件已翻译")
    for src, dst in results:
        print(f"  {src.name} -> {dst}")


if __name__ == "__main__":
    main()

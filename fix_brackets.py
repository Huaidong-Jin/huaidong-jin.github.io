#!/usr/bin/env python3
"""
修复MDX文件中的引用格式
- 将<u>[数字](URL)</u>改为<u>[[数字]](URL)</u>
- 确保在网页上显示时数字外面有中括号
"""

import re

def fix_citation_brackets(file_path):
    """修复引用格式，确保数字外面有中括号"""
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 使用正则表达式找到所有的<u>[数字](URL)</u>格式
    # 并替换为<u>[[数字]](URL)</u>格式
    pattern = r'<u>\[(\d+)\]\(([^)]+)\)</u>'
    replacement = r'<u>[[\1]](\2)</u>'
    
    updated_content = re.sub(pattern, replacement, content)
    
    # 计算替换数量
    matches = re.findall(pattern, content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)
    
    print(f"已修复 {len(matches)} 个引用格式，确保数字外面有中括号显示")
    return len(matches)

if __name__ == "__main__":
    file_path = "content/posts/2025-06-25-transforming-operation-in-japan-financial-industry-new.mdx"
    fix_citation_brackets(file_path) 
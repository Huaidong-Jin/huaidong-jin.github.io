#!/usr/bin/env python3
"""
优化MDX文件中的标题层级
- 将一级标题 # 改为二级标题 ##
- 将二级标题 ## 改为三级标题 ###
- 保持其他层级标题不变
- 提升用户在电脑和手机上的浏览体验
"""

import re

def optimize_title_hierarchy(file_path):
    """优化标题层级，减小标题字体大小"""
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 统计当前标题分布
    h1_count = len(re.findall(r'^# ', content, re.MULTILINE))
    h2_count = len(re.findall(r'^## ', content, re.MULTILINE))
    h3_count = len(re.findall(r'^### ', content, re.MULTILINE))
    
    print(f"优化前标题分布：")
    print(f"  一级标题 (#): {h1_count}个")
    print(f"  二级标题 (##): {h2_count}个")
    print(f"  三级标题 (###): {h3_count}个")
    
    # 优化标题层级
    # 1. 先将二级标题改为三级标题（避免冲突）
    content = re.sub(r'^## ', '### ', content, flags=re.MULTILINE)
    
    # 2. 将一级标题改为二级标题
    content = re.sub(r'^# ', '## ', content, flags=re.MULTILINE)
    
    # 统计优化后的标题分布
    new_h1_count = len(re.findall(r'^# ', content, re.MULTILINE))
    new_h2_count = len(re.findall(r'^## ', content, re.MULTILINE))
    new_h3_count = len(re.findall(r'^### ', content, re.MULTILINE))
    
    print(f"\\n优化后标题分布：")
    print(f"  一级标题 (#): {new_h1_count}个")
    print(f"  二级标题 (##): {new_h2_count}个")
    print(f"  三级标题 (###): {new_h3_count}个")
    
    # 保存优化后的内容
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"\\n✅ 标题层级优化完成！")
    print(f"主要改进：")
    print(f"  - 消除了过大的一级标题，改为更适中的二级标题")
    print(f"  - 原二级标题调整为三级标题，保持层次结构")
    print(f"  - 提升了在电脑和手机屏幕上的阅读体验")
    
    return {
        'before': {'h1': h1_count, 'h2': h2_count, 'h3': h3_count},
        'after': {'h1': new_h1_count, 'h2': new_h2_count, 'h3': new_h3_count}
    }

if __name__ == "__main__":
    file_path = "content/posts/2025-06-25-transforming-operation-in-japan-financial-industry-new.mdx"
    result = optimize_title_hierarchy(file_path) 
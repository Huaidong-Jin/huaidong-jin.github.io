#!/usr/bin/env python3
"""
进一步优化MDX文件中的标题层级
- 将二级标题 ## 改为三级标题 ###
- 将三级标题 ### 改为四级标题 ####
- 大幅减小标题字体大小，提升用户在各种设备上的浏览体验
"""

import re

def optimize_title_hierarchy_further(file_path):
    """进一步优化标题层级，让标题更适中"""
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 统计当前标题分布
    h2_count = len(re.findall(r'^## ', content, re.MULTILINE))
    h3_count = len(re.findall(r'^### ', content, re.MULTILINE))
    h4_count = len(re.findall(r'^#### ', content, re.MULTILINE))
    
    print(f"优化前标题分布：")
    print(f"  二级标题 (##): {h2_count}个")
    print(f"  三级标题 (###): {h3_count}个")
    print(f"  四级标题 (####): {h4_count}个")
    
    # 进一步优化标题层级
    # 1. 先将三级标题改为四级标题（避免冲突）
    content = re.sub(r'^### ', '#### ', content, flags=re.MULTILINE)
    
    # 2. 将二级标题改为三级标题
    content = re.sub(r'^## ', '### ', content, flags=re.MULTILINE)
    
    # 统计优化后的标题分布
    h2_count_after = len(re.findall(r'^## ', content, re.MULTILINE))
    h3_count_after = len(re.findall(r'^### ', content, re.MULTILINE))
    h4_count_after = len(re.findall(r'^#### ', content, re.MULTILINE))
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"\n优化后标题分布：")
    print(f"  二级标题 (##): {h2_count_after}个")
    print(f"  三级标题 (###): {h3_count_after}个")
    print(f"  四级标题 (####): {h4_count_after}个")
    
    total_optimized = h2_count + h3_count
    print(f"\n✅ 成功优化了 {total_optimized} 个标题")
    print(f"📱 标题现在在电脑和手机屏幕上都会显得更加适中")
    print(f"🎯 用户可以在屏幕上看到更多实际内容")
    
    return total_optimized

if __name__ == "__main__":
    file_path = "content/posts/2025-06-25-transforming-operation-in-japan-financial-industry-new.mdx"
    optimize_title_hierarchy_further(file_path) 
#!/usr/bin/env python3
"""
修复MDX文件中的引用格式
- 将纯数字引用（如1、12、1112）改为<u>[数字]</u>格式
- 保持链接不变
"""

import re
from typing import Dict

def create_citation_mapping() -> Dict[str, str]:
    """创建引用编号到URL的映射"""
    return {
        '1': 'https://personetics.com/going-big-in-japan/',
        '2': 'https://personetics.com/going-big-in-japan/',
        '3': 'https://thebankingscene.com/opinions/the-transformative-forces-in-a-banks-middle-and-back-office',
        '4': 'https://thebankingscene.com/opinions/the-transformative-forces-in-a-banks-middle-and-back-office',
        '5': 'https://www.nbr.org/publication/overcoming-japans-uphill-battle-toward-digital-transformation/',
        '6': 'https://english.kyodonews.net/news/2021/08/ea4d52f95f1c-breaking-news-japans-mizuho-bank-reports-system-failure-at-branch-counters.html',
        '7': 'https://english.kyodonews.net/news/2021/08/ea4d52f95f1c-breaking-news-japans-mizuho-bank-reports-system-failure-at-branch-counters.html',
        '8': 'https://thebankingscene.com/opinions/the-transformative-forces-in-a-banks-middle-and-back-office',
        '9': 'https://tokyoesque.com/the-impact-of-japans-ageing-population-on-the-business-landscape/',
        '10': 'https://tokyoesque.com/the-impact-of-japans-ageing-population-on-the-business-landscape/',
        '11': 'https://thebankingscene.com/opinions/the-transformative-forces-in-a-banks-middle-and-back-office',
        '12': 'https://thebankingscene.com/opinions/the-transformative-forces-in-a-banks-middle-and-back-office',
        '13': 'https://www.spglobal.com/market-intelligence/en/news-insights/articles/2023/3/japan-s-regional-banks-face-pressure-to-consolidate-as-interest-holiday-ends-74229512',
        '14': 'https://www.japantimes.co.jp/business/2025/01/20/companies/japan-regional-bank-merger/',
        '15': 'https://www.accenture.com/us-en/case-studies/banking/minna-bank',
        '16': 'https://www.accenture.com/us-en/case-studies/banking/minna-bank',
        '17': 'https://www.nbr.org/publication/overcoming-japans-uphill-battle-toward-digital-transformation/',
        '18': 'https://www.nbr.org/publication/overcoming-japans-uphill-battle-toward-digital-transformation/',
        '19': 'https://www.mizuhogroup.com/digital/2312-generative-ai',
        '20': 'https://www.mizuhogroup.com/digital/2312-generative-ai',
        '21': 'https://personetics.com/going-big-in-japan/',
        '22': 'https://personetics.com/going-big-in-japan/',
        '23': 'https://thebankingscene.com/opinions/the-transformative-forces-in-a-banks-middle-and-back-office',
        '24': 'https://www.frbsf.org/research-and-insights/blog/sf-fed-blog/2019/03/18/why-do-japanese-households-hold-so-much-cash/',
        '25': 'https://www.nippon.com/en/japan-data/h02053/more-than-half-of-new-nisa-investors-in-japan-using-both-tsumitate-and-growth-accounts.html',
        '26': 'https://www.nippon.com/en/japan-data/h02053/more-than-half-of-new-nisa-investors-in-japan-using-both-tsumitate-and-growth-accounts.html',
        '27': 'https://aws.amazon.com/solutions/case-studies/bedrock-nomura/',
        '28': 'https://aws.amazon.com/solutions/case-studies/bedrock-nomura/',
        '29': 'https://aws.amazon.com/solutions/case-studies/bedrock-nomura/',
        '30': 'https://www.numberanalytics.com/blog/generative-ai-underwriting-claims',
        '31': 'https://www.bcg.com/publications/2023/the-future-of-insurance-claims',
        '32': 'https://www.bcg.com/publications/2023/the-future-of-insurance-claims',
        '33': 'https://www.bcg.com/publications/2023/the-future-of-insurance-claims',
        '34': 'https://newsroom.accenture.com/news/2025/meiji-yasuda-collaborates-with-accenture-to-drive-ai-led-business-reinvention',
        '35': 'https://newsroom.accenture.com/news/2025/meiji-yasuda-collaborates-with-accenture-to-drive-ai-led-business-reinvention',
        '36': 'https://newsroom.accenture.com/news/2025/meiji-yasuda-collaborates-with-accenture-to-drive-ai-led-business-reinvention',
        '37': 'https://newsroom.accenture.com/news/2025/meiji-yasuda-collaborates-with-accenture-to-drive-ai-led-business-reinvention',
        '38': 'https://www.mckinsey.com/industries/financial-services/our-insights/capturing-the-full-value-of-generative-ai-in-banking',
        '39': 'https://www.mckinsey.com/industries/financial-services/our-insights/capturing-the-full-value-of-generative-ai-in-banking',
        '40': 'https://www.mckinsey.com/industries/financial-services/our-insights/capturing-the-full-value-of-generative-ai-in-banking',
        '41': 'https://www.mckinsey.com/industries/financial-services/our-insights/capturing-the-full-value-of-generative-ai-in-banking',
        '42': 'https://www.mckinsey.com/industries/financial-services/our-insights/capturing-the-full-value-of-generative-ai-in-banking',
        '43': 'https://www.mckinsey.com/industries/financial-services/our-insights/capturing-the-full-value-of-generative-ai-in-banking',
        '44': 'https://www.mckinsey.com/industries/financial-services/our-insights/capturing-the-full-value-of-generative-ai-in-banking',
        '45': 'https://www.mckinsey.com/industries/financial-services/our-insights/capturing-the-full-value-of-generative-ai-in-banking',
        '46': 'https://www.mckinsey.com/industries/financial-services/our-insights/capturing-the-full-value-of-generative-ai-in-banking',
        '47': 'https://www.mckinsey.com/industries/financial-services/our-insights/capturing-the-full-value-of-generative-ai-in-banking',
        '48': 'https://www.mckinsey.com/industries/financial-services/our-insights/capturing-the-full-value-of-generative-ai-in-banking',
        '49': 'https://www.mckinsey.com/industries/financial-services/our-insights/capturing-the-full-value-of-generative-ai-in-banking',
        '50': 'https://www.mckinsey.com/industries/financial-services/our-insights/capturing-the-full-value-of-generative-ai-in-banking',
        '51': 'https://www.mizuhogroup.com/digital/2312-generative-ai',
        '52': 'https://www.mizuhogroup.com/digital/2312-generative-ai',
        '53': 'https://www.linkedin.com/posts/sumitomo-mitsui-banking-corporation_smbc-gai-the-inside-story-on-the-smbc-group-activity-7198717261128347648-2VK9',
        '54': 'https://www.mckinsey.com/industries/financial-services/our-insights/capturing-the-full-value-of-generative-ai-in-banking',
        '55': 'https://www.mckinsey.com/industries/financial-services/our-insights/capturing-the-full-value-of-generative-ai-in-banking',
        '56': 'https://www.fsa.go.jp/en/news/2025/20250304/aidp_en.pdf',
        '57': 'https://thebankingscene.com/opinions/the-transformative-forces-in-a-banks-middle-and-back-office',
        '58': 'https://thebankingscene.com/opinions/the-transformative-forces-in-a-banks-middle-and-back-office',
        '59': 'https://www.mckinsey.com/industries/financial-services/our-insights/capturing-the-full-value-of-generative-ai-in-banking',
        '60': 'https://aws.amazon.com/solutions/case-studies/bedrock-nomura/',
    }

def fix_citations_in_file(file_path: str):
    """修复文件中的引用格式"""
    print(f"正在处理文件: {file_path}")
    
    # 读取文件
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 获取引用映射
    citation_mapping = create_citation_mapping()
    
    # 先处理已经是<u>[数字](URL)</u>格式的引用，提取出数字进行重新处理
    # 模式1: 处理<u>[数字](URL)</u>格式
    pattern1 = r'<u>\[(\d+)\]\([^)]+\)</u>'
    
    def replace_underlined_citation(match):
        num = match.group(1)
        if num in citation_mapping:
            url = citation_mapping[num]
            return f'<u>[{num}]({url})</u>'
        else:
            return match.group(0)  # 保持原样
    
    # 先处理已有的下划线引用
    content = re.sub(pattern1, replace_underlined_citation, content)
    
    # 模式2: 查找文本中的纯数字引用（在句子中间或末尾，不在URL中）
    # 这个正则会匹配：文本后面紧跟数字，但不在URL或已有引用格式中
    # 避免匹配URL中的数字、年份等
    pattern2 = r'(?<![\[\(])\b(\d{1,2})(?=[\s。、，！？\.]|$)(?![^\[]*\])'
    
    def replace_plain_citation(match):
        num = match.group(1)
        # 只处理1-60范围内的数字，避免误匹配年份等
        if num in citation_mapping and 1 <= int(num) <= 60:
            url = citation_mapping[num]
            return f'<u>[{num}]({url})</u>'
        else:
            return match.group(0)  # 保持原样
    
    # 处理纯数字引用
    content = re.sub(pattern2, replace_plain_citation, content)
    
    # 特殊处理连续数字（如1112）
    # 这种情况需要特殊处理，将其拆分为单独的引用
    pattern3 = r'\b(\d{3,4})\b'
    
    def replace_multiple_citations(match):
        nums_str = match.group(1)
        # 尝试将连续数字拆分为单个引用
        result = []
        i = 0
        while i < len(nums_str):
            # 尝试匹配两位数
            if i + 1 < len(nums_str):
                two_digit = nums_str[i:i+2]
                if two_digit in citation_mapping:
                    url = citation_mapping[two_digit]
                    result.append(f'<u>[{two_digit}]({url})</u>')
                    i += 2
                    continue
            
            # 匹配单位数
            one_digit = nums_str[i]
            if one_digit in citation_mapping:
                url = citation_mapping[one_digit]
                result.append(f'<u>[{one_digit}]({url})</u>')
            i += 1
        
        return ''.join(result) if result else match.group(0)
    
    # 处理连续数字
    content = re.sub(pattern3, replace_multiple_citations, content)
    
    print(f"文件处理完成: {file_path}")
    print("所有引用已转换为 <u>[数字](URL)</u> 格式")
    
    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    file_path = "content/posts/2025-06-25-transforming-operation-in-japan-financial-industry-new.mdx"
    fix_citations_in_file(file_path) 
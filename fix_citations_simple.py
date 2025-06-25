#!/usr/bin/env python3
"""
修复MDX文件中的引用格式
- 将[^2^]格式改为<u>[2]</u>格式，添加下划线
- 映射到正确的URL
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
    
    # 查找所有引用模式并替换
    # 模式: [^1,2^](url) 或 [^1^](url)
    pattern = r'\[\^([0-9,\s]+)\^\]\(([^)]+)\)'
    
    def replace_citation(match):
        citation_nums_str = match.group(1)
        original_url = match.group(2)
        
        # 处理多个引用编号（如"1,2"或"1, 2"）
        nums = [num.strip() for num in citation_nums_str.split(',') if num.strip()]
        
        new_citations = []
        for num in nums:
            if num in citation_mapping:
                mapped_url = citation_mapping[num]
                new_citations.append(f'<u>[{num}]({mapped_url})</u>')
            else:
                print(f"警告: 未找到引用编号 {num} 的映射，保留原URL")
                new_citations.append(f'<u>[{num}]({original_url})</u>')
        
        return ''.join(new_citations)
    
    # 执行替换
    modified_content = re.sub(pattern, replace_citation, content)
    
    # 统计替换次数
    original_citations = len(re.findall(pattern, content))
    print(f"找到 {original_citations} 个引用，已全部转换为新格式")
    
    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(modified_content)
    
    print(f"文件处理完成: {file_path}")
    print("所有引用已转换为 <u>[数字](URL)</u> 格式，并添加了下划线样式")

if __name__ == "__main__":
    file_path = "content/posts/2025-06-25-transforming-operation-in-japan-financial-industry-new.mdx"
    fix_citations_in_file(file_path) 
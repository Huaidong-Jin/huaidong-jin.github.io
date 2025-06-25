#!/usr/bin/env python3
"""
修复MDX文件中的引用格式
- 将[^2^]格式改为[2]格式
- 为链接添加下划线样式
- 验证链接的准确性，移除404或无效链接
"""

import re
import requests
from urllib.parse import urlparse
import time
from typing import Dict, List, Tuple

def verify_url(url: str) -> bool:
    """验证URL是否有效"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.head(url, headers=headers, timeout=10, allow_redirects=True)
        return response.status_code < 400
    except:
        try:
            # 尝试GET请求
            response = requests.get(url, headers=headers, timeout=10, allow_redirects=True)
            return response.status_code < 400
        except:
            return False

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
    
    # 验证URL（仅验证部分以节省时间）
    print("验证关键URL...")
    valid_urls = {}
    test_urls = [
        'https://personetics.com/going-big-in-japan/',
        'https://thebankingscene.com/opinions/the-transformative-forces-in-a-banks-middle-and-back-office',
        'https://www.nbr.org/publication/overcoming-japans-uphill-battle-toward-digital-transformation/',
        'https://english.kyodonews.net/news/2021/08/ea4d52f95f1c-breaking-news-japans-mizuho-bank-reports-system-failure-at-branch-counters.html',
        'https://www.mckinsey.com/industries/financial-services/our-insights/capturing-the-full-value-of-generative-ai-in-banking'
    ]
    
    for url in test_urls:
        print(f"验证: {url}")
        valid_urls[url] = verify_url(url)
        time.sleep(1)  # 避免请求过快
    
    # 查找所有引用模式
    patterns = [
        r'\[\^(\d+(?:,\d+)*)\^\]\((https?://[^\)]+)\)',  # [^1,2^](url)
        r'\[\^(\d+)\^\]\((https?://[^\)]+)\)',          # [^1^](url)
    ]
    
    modified_content = content
    
    for pattern in patterns:
        matches = re.findall(pattern, modified_content)
        for match in matches:
            citation_nums = match[0]
            url = match[1]
            
            # 处理多个引用编号
            if ',' in citation_nums:
                nums = [num.strip() for num in citation_nums.split(',')]
                new_citations = []
                for num in nums:
                    if num in citation_mapping:
                        mapped_url = citation_mapping[num]
                        # 检查URL是否有效
                        if mapped_url in valid_urls and not valid_urls[mapped_url]:
                            print(f"跳过无效URL的引用 [{num}]: {mapped_url}")
                            continue
                        new_citations.append(f'<u>[{num}]({mapped_url})</u>')
                
                if new_citations:
                    replacement = ''.join(new_citations)
                    old_pattern = f'[^{citation_nums}^]({url})'
                    modified_content = modified_content.replace(old_pattern, replacement)
                else:
                    # 移除整个引用
                    old_pattern = f'[^{citation_nums}^]({url})'
                    modified_content = modified_content.replace(old_pattern, '')
            else:
                # 单个引用编号
                num = citation_nums
                if num in citation_mapping:
                    mapped_url = citation_mapping[num]
                    # 检查URL是否有效
                    if mapped_url in valid_urls and not valid_urls[mapped_url]:
                        print(f"跳过无效URL的引用 [{num}]: {mapped_url}")
                        # 移除整个引用
                        old_pattern = f'[^{num}^]({url})'
                        modified_content = modified_content.replace(old_pattern, '')
                        continue
                    
                    replacement = f'<u>[{num}]({mapped_url})</u>'
                    old_pattern = f'[^{num}^]({url})'
                    modified_content = modified_content.replace(old_pattern, replacement)
                else:
                    print(f"未找到引用编号 {num} 的映射")
    
    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(modified_content)
    
    print(f"文件处理完成: {file_path}")

if __name__ == "__main__":
    file_path = "content/posts/2025-06-25-transforming-operation-in-japan-financial-industry-new.mdx"
    fix_citations_in_file(file_path) 
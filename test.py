import requests
import time
from bs4 import BeautifulSoup

ticker = 'META'
ticker_keywords = {
    "META": ["Meta", "Facebook", "Zuckerberg", "Instagram", "WhatsApp"],
    "AAPL": ["Apple", "iPhone", "Tim Cook", "MacBook", "iCloud"],
    "PTT.BK": ["PTT", "Bangchak", "Oil", "Gas", "Energy"], # A SET50 example
    "NVDA": ["Nvidia", "Jensen Huang", "AI", "chips", "GPU", "microchips"]
}

url = f"https://finance.yahoo.com/quote/{ticker}/news"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': f'https://finance.yahoo.com/quote/{ticker}', # The "Magic" line
    'DNT': '1',
    'Connection': 'keep-alive',
}
response = requests.get(url, headers=headers)
print(response)
soup = BeautifulSoup(response.text, 'html.parser')

main_content = soup.find('section', {'class':'container yf-1m8w4l1'})
links = main_content.find_all('a')
all_articles = []

for link in links:
    h3_tag = link.find('h3')
    if h3_tag:
        headline_text = h3_tag.get_text().strip()
        link_url = link.get('href')
        if link_url.startswith('/'):
            full_url = "https://finance.yahoo.com" + link_url
        else:
            full_url = link_url
            
        print(f"Headline: {headline_text}")
        article_response = requests.get(full_url, headers=headers)
        article_soup = BeautifulSoup(article_response.text, 'html.parser')
        
        time_tag = article_soup.find('time', {'class':'byline-attr-meta-time'})
        if time_tag:
            article_time = time_tag.get('datetime')
            print(article_time)

        body_wrapper = article_soup.find('div', {'class':'bodyItems-wrapper'})
        if body_wrapper:
            paragraphs = body_wrapper.find_all('p')

            all_text = [p.get_text().strip() for p in paragraphs]
            full_content = " ".join(all_text)
            article_data = {
            "headline": headline_text,
            "url": full_url,
            "timestamp": article_time,
            "content": full_content
        }
            
            current_keywords = ticker_keywords.get(ticker, [])
            is_relevant = any(word.lower() in full_content.lower() for word in current_keywords)
            if is_relevant:
                all_articles.append(article_data)
                print(f"Successfully saved: {headline_text}")
                print("-" * 20)
            else:
                print(f"Skipping noise: {headline_text}")

        
        
        time.sleep(0.25)

import pandas as pd
df = pd.DataFrame(all_articles)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df.sort_values(by='timestamp', ascending=True)
df.to_csv(f'data/raw_news/yahoo_news_{ticker}.csv', index=False, encoding='utf-8-sig')

print(f"Mission Accomplished: CSV exported to data/raw_news/yahoo_news_{ticker}.csv")
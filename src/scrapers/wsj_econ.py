import feedparser
import pandas as pd

# 1. The Target
RSS_URL = "https://feeds.content.dowjones.io/public/rss/socialeconomyfeed"

# 2. The "Reading" (Fetch and Parse automatically)
# feedparser handles the network request and XML parsing in one line.
feed = feedparser.parse(RSS_URL)

# 3. The Verification
if feed.status == 200:
    print(f"SUCCESS: Connected. Feed Title: {feed.feed.title}")
else:
    print(f"FAILED: Status Code {feed.status}")

# 4. The Extraction
print(f"TOTAL ARTICLES FOUND: {len(feed.entries)}")

data_rows = []
for entry in feed.entries:
    row = {
        "title": entry.title,
        "link": entry.link,
        "published": entry.published
    }
    data_rows.append(row)

df = pd.DataFrame(data_rows)
df = pd.DataFrame(data_rows)
df['published'] = pd.to_datetime(df['published'])
df = df.sort_values(by='published', ascending=True)
df.to_csv(f'data/raw/wsj_econ.csv', index=False, encoding='utf-8-sig')
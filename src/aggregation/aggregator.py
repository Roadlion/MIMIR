import ast
import os
import pandas as pd

#this script's dir
script_dir = os.path.dirname(__file__)

#get merged_impacted_news
impacted_news_rel = os.path.join(script_dir, '..', '..',  'data', 'processed', 'merged_impacted_news.csv')
impacted_news_abs = os.path.abspath(impacted_news_rel)

#read impacted news
df = pd.read_csv(impacted_news_abs)

#flatten impacts
df['impacts'] = df['impacts'].apply(ast.literal_eval)

flattened = []
for _, row in df.iterrows():
    for impact in row['impacts']:
        impact['source_headline'] = row['title']  # Track origin
        flattened.append(impact)
impacts_df = pd.DataFrame(flattened)

aggregated = impacts_df.groupby('asset').agg({
    'confidence': ['mean', 'count'],
    'direction': lambda x: x.mode()[0] if not x.mode().empty else 'neutral',
    'impact': lambda x: list(x)[:2],  # Top 2 impact descriptions
    'source_headline': lambda x: list(x)[:3]  # Top 3 source headlines
}).round(4)

aggregated['signal_strength'] = aggregated[('confidence', 'mean')] * aggregated[('confidence', 'count')]

aggregated.columns = ['confidence_avg', 'signal_count', 'dominant_direction', 'top_impacts', 'source_headlines', 'signal_strength']
aggregated = aggregated.reset_index()

dashboard_folder_rel = os.path.join(script_dir, '..', 'dashboard')
dashboard_folder_abs = os.path.abspath(dashboard_folder_rel)

json_dir = os.path.join(dashboard_folder_abs, 'signals.json')

aggregated.to_json(json_dir, orient='records')
print("Aggregation complete!")
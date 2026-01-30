import pandas as pd
import json
import os
from impact_rules import impact_rules

#this script's dir
script_dir = os.path.dirname(__file__)

# Navigate up two levels, then down into data/raw
csv_rel_path = os.path.join(script_dir, '..', '..', 'data', 'processed', 'merged_analyzed_news.csv')
csv_abs_path = os.path.abspath(csv_rel_path)

df = pd.read_csv(csv_abs_path)

#Rule application function
def apply_rules_to_row(row, rules):
    impacts = []
    sentiment = row['title_score']
    sentiment_dir = 'positive' if sentiment > 0.1 else 'negative' if sentiment < -0.1 else 'neutral'
    
    topics_list = row['topics']  # Already converted to list
    entities_list = row['entities']
    
    for rule in rules:
        # Check topic condition
        if not all(topic in topics_list for topic in rule['conditions']['required_topics']):
            continue
        # Check entity condition
        if not all(entity in entities_list for entity in rule['conditions']['required_entities']):
            continue
        # Check sentiment direction
        if rule['conditions']['sentiment_direction'] not in [sentiment_dir, 'any']:
            continue
        
        # Calculate final confidence (base * sentiment strength)
        sentiment_strength = abs(sentiment)
        final_confidence = rule['confidence_base'] * min(sentiment_strength, 1.0)
        
        impacts.append({
            'asset': rule['affected_asset'],
            'impact': rule['impact'],
            'direction': sentiment_dir,  # or derive from rule
            'confidence': final_confidence,
            'reasoning': rule['reasoning']
        })
    return impacts

df['impacts'] = df.apply(apply_rules_to_row, axis=1, args=(impact_rules, ))
#Save the results
df.to_csv('data/processed/merged_impacted_news.csv', index=False,  encoding='utf-8-sig')
print("Impact Rules applied! File saved in data/processed/")
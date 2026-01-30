import pandas as pd
import os
from tagger import auto_tag_entity, auto_tag_topic
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

#import FINBERT
model_name = "ProsusAI/finbert"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

def get_sentiment(text):
    # Prepare the text for the AI (truncating if it's too long)
    inputs = tokenizer(text, padding=True, truncation=True, max_length=512, return_tensors='pt')
    
    with torch.no_grad():
        outputs = model(**inputs)
        
    # Convert "Logits" to "Probabilities" using Softmax
    probs = F.softmax(outputs.logits, dim=-1).numpy()[0]
    
    # FinBERT Mapping: [0] -> Positive, [1] -> Negative, [2] -> Neutral
    # We calculate the BEN Sentiment Index: Pos - Neg
    sentiment_index = probs[0] - probs[1]
    return sentiment_index

#this script's dir
script_dir = os.path.dirname(__file__)

# Navigate up two levels, then down into data/raw
csv_rel_path = os.path.join(script_dir, '..', '..', 'data', 'raw', 'merged', 'merged_news.csv')
csv_abs_path = os.path.abspath(csv_rel_path)

df = pd.read_csv(csv_abs_path)

print("Running FinBERT (this might take a  while)...")
df["title_score"] = df["title"].apply(get_sentiment)

print("Tagging Entities...")
df["entities"] = df["title"].apply(auto_tag_entity)

print("Tagging Topics...")
df["topics"] = df["title"].apply(auto_tag_topic)

#Save the results
df.to_csv('data/processed/merged_analyzed_news.csv', index=False,  encoding='utf-8-sig')
print("Analysis complete! File saved in data/processed/")
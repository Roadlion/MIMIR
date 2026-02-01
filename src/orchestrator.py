import os
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
import glob
import subprocess
import pandas as pd

#get all list of all scraper files

#this script's dir
script_dir = os.path.dirname(__file__)

scraper_dir_rel = os.path.join(script_dir, "scrapers",  "*.py")
scraper_dir_abs = os.path.abspath(scraper_dir_rel)

scraper_files = glob.glob(scraper_dir_abs)

#Scraper Execution Loop
for file in scraper_files:
    subprocess.run(['python', file])
print('FINISHED SCRAPING AND EXPORTING')

#Raw CSV Path
raw_data_rel = os.path.join(script_dir, "..",  "data", "raw", '*.csv')
raw_data_abs = os.path.abspath(raw_data_rel)

#List of all CSV files
raw_files = glob.glob(raw_data_abs)

list_of_df = []

for csv in raw_files:
    list_of_df.append(pd.read_csv(csv))

#Merging all Dataframes
merged_df = pd.concat(list_of_df, ignore_index=True)
merged_df = merged_df.drop_duplicates(
    subset=['title', 'link', 'published'], 
    keep='first'
)
merged_df = merged_df.sort_values(by='published', ascending=True)
merged_df.to_csv('data/raw/merged/merged_news.csv', index=False,  encoding='utf-8-sig')
print("NEWS MERGING COMPLETE")

#Get analyzer path
analyzer_rel = os.path.join(script_dir, 'analysis', 'analyzer.py')
analyzer_abs = os.path.abspath(analyzer_rel)

#Run analyzer
print("Running Analyzer...")
subprocess.run(['python',analyzer_abs])

#Get Impact Engine Path
impact_rel = os.path.join(script_dir, 'inference', 'impact_engine.py')
impact_abs = os.path.abspath(impact_rel)

#Run Impact Engine
print("Running Impact Engine...")
subprocess.run(['python', impact_abs])

#Get Aggregator Path
agg_rel = os.path.join(script_dir, 'aggregation', 'aggregator.py')
agg_abs = os.path.abspath(agg_rel)

#Run Aggregator
print("Running Aggregator...")
subprocess.run(['python', agg_abs])

#Get Dashboard Path
db_rel = os.path.join(script_dir, 'dashboard', 'dashboard.py')
db_abs = os.path.abspath(db_rel)

#Run Dashboard
print("Opening Dashboard...")
subprocess.run(['streamlit', 'run', db_abs])
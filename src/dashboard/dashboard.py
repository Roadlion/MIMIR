import streamlit as st
import pandas as pd
import plotly.express as px
import os
#this script's dir
script_dir = os.path.dirname(__file__)

#Read Signals
signals_rel = os.path.join(script_dir, 'signals.json')
signals_abs = os.path.abspath(signals_rel)
signals = pd.read_json(signals_abs)

#get merged_impacted_news
impacted_news_rel = os.path.join(script_dir, '..', '..',  'data', 'processed', 'merged_impacted_news.csv')
impacted_news_abs = os.path.abspath(impacted_news_rel)

#read impacted news
articles = pd.read_csv(impacted_news_abs)

#get country code

def get_iso_code(asset_name):
    # Currency Mapping
    if asset_name == 'USD': return 'USA'
    if asset_name == 'EUR': return 'DEU' 
    if asset_name == 'GBP': return 'GBR'
    if asset_name == 'JPY': return 'JPN'
    if asset_name == 'CAD': return 'CAN'
    if asset_name == 'IDR': return 'IDN'
    if asset_name == 'CNY': return 'CHN'
    if asset_name == 'THB': return 'THA'
    if asset_name == 'INR': return 'IND'
    if asset_name == 'KRW': return 'KOR'
    if asset_name == 'RUB': return 'RUS'
    
    # Economy/Equity Mapping (Extract Country Prefix)
    if asset_name.startswith('US_'): return 'USA'
    if asset_name.startswith('CHINA_'): return 'CHN'
    if asset_name.startswith('EU_'): return 'DEU' # Proxy for Eurozone
    if asset_name.startswith('UK_'): return 'GBR'
    if asset_name.startswith('JAPAN_'): return 'JPN'
    if asset_name.startswith('CANADA_'): return 'CAN'
    if asset_name.startswith('INDONESIA_'): return 'IDN'
    if asset_name.startswith('THAI_'): return 'THA'
    if asset_name.startswith('INDIA_'): return 'IND'
    if asset_name.startswith('SOUTH_KOREA_'): return 'KOR'
    if asset_name.startswith('RUSSIA_'): return 'RUS'
    
    return None

#categorize impacted asset
def categorize_asset(asset_name):
    if asset_name in ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'IDR', 'CNY', 'THB']:
        return 'Currencies'
    elif asset_name.startswith('COMMODITY'):
        return 'Commodities'
    elif 'EQUITY' in asset_name or 'STOCK' in asset_name:
        return 'Global Equities'
    elif 'BOND' in asset_name or 'GILT' in asset_name or 'TREASURY' in asset_name or 'JGB' in asset_name:
        return 'Fixed Income'
    elif 'POLICY' in asset_name:
        return 'POLICY'
    elif 'ECONOMY' in asset_name:
        return 'ECONOMY'
    else:
        return 'Global Factors' # For Crypto, Geopolitics, Tech, etc.

signals['category'] = signals['asset'].apply(categorize_asset)

st.title("M.I.M.I.R. Dashboard")
st.subheader("(Market Intelligence & Macroeconomic Indicator Reactor)")

map_tab1, map_tab2, map_tab3 = st.tabs([
    "Global Equities Map", 
    "Currencies (FX) Map", 
    "Economies Map"
])

def render_map(df, title):
    """Renders a Choropleth map based on the filtered dataframe."""
    st.subheader(title)
    
    # Filter for mappable assets
    df['iso_code'] = df['asset'].apply(get_iso_code)
    map_data = df.dropna(subset=['iso_code'])
    
    if map_data.empty:
        st.info("No geographic data available for this category.")
        return

    # Color Map
    # We map 'positive' to Green, 'negative' to Red.
    color_map = {'positive': '#2ecc71', 'negative': '#e74c3c'}
    
    fig = px.choropleth(
        map_data,
        locations="iso_code",
        color="dominant_direction",
        hover_name="asset",
        hover_data=["signal_strength", "top_impacts"],
        color_discrete_map=color_map,
        projection="natural earth", # Good global view
        category_orders={"dominant_direction": ["positive", "negative"]} # Force order if needed
    )
    
    fig.update_geos(showcountries=True, countrycolor="#e0e0e0")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}) # Compact layout
    
    st.plotly_chart(fig, use_container_width=True)

with map_tab1:
    # Filter: Equities
    # Includes US_EQUITY, JAPAN_EQUITY, THAI_EQUITY, etc.
    equity_geo = signals[signals['category'] == 'Global Equities']
    render_map(equity_geo, "Equity Markets")

with map_tab2:
    # Filter: Currencies
    # Includes USD, THB, JPY, etc.
    curr_geo = signals[signals['category'] == 'Currencies']
    render_map(curr_geo, "Currency Strength")

with map_tab3:
    # Filter: Economies
    # Includes US_ECONOMY, CHINA_ECONOMY, etc.
    econ_geo = signals[signals['category'] == 'ECONOMY']
    render_map(econ_geo, "Economic Health")


# Create Tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "Currencies (FX)", 
    "Commodities", 
    "Equity Markets", 
    "Fixed Income", 
    "Central Bank Policies",
    "Economies",
    "Global Factors",
    "All Signals (The Noise)"
])

# --- CHART GENERATION FUNCTION ---
# We define this once to reuse it across tabs
def render_leaderboard(df, title):
    st.subheader(title)
    if df.empty:
        st.info("No signals detected for this sector.")
        return
    
    # Sort by Signal Strength (Most volatile/active first)
    df_sorted = df.sort_values('signal_strength', ascending=False)
    
    # Color Map: Red = Negative (Bearish), Green = Positive (Bullish)
    # Using a distinct, professional palette
    fig = px.bar(
        df_sorted, 
        x='signal_strength', 
        y='asset', 
        color='dominant_direction', 
        orientation='h',
        color_discrete_map={'positive': '#2ecc71', 'negative': '#e74c3c'}, # Emerald & Alizarin
        text='signal_strength', # Show value on bar
        title="Aggregated Signal Strength (Confidence Weighted)"
    )
    
    # Layout updates for cleaner look
    fig.update_layout(
        yaxis={'categoryorder': 'total ascending'}, # Sorts bars nicely
        xaxis_title="Signal Strength",
        yaxis_title="Asset",
        height=600,
        plot_bgcolor='rgba(0,0,0,0)' # Transparent background
    )
    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Optional: Show source headlines below chart
    with st.expander("View Source Headlines"):
        for _, row in df_sorted.iterrows():
            st.write(f"**{row['asset']}** ({row['dominant_direction']})")
            for headline in row['source_headlines']:
                st.write(f"- {headline}")
            st.markdown("---")

# --- TAB CONTENT ---

with tab1:
    # Filter for Currencies
    curr_signals = signals[signals['category'] == 'Currencies']
    render_leaderboard(curr_signals, "Currency Market Sentiment")

with tab2:
    # Filter for Commodities
    comm_signals = signals[signals['category'].isin(['Commodities'])]
    render_leaderboard(comm_signals, "Commodity Market Sentiment")

with tab3:
    # Filter for Equities
    equity_signals = signals[signals['category'] == 'Global Equities']
    render_leaderboard(equity_signals, "Global Equity Market Sentiment")

with tab4:
    # Filter for Bonds
    macro_signals = signals[signals['category'].isin(['Fixed Income'])]
    render_leaderboard(macro_signals, "Bond Market Sentiment")

with tab5:
    # Filter for Central Bank Policy
    macro_signals = signals[signals['category'].isin(['POLICY'])]
    render_leaderboard(macro_signals, "Central Bank Policies")

with tab6:
    # Filter Economic Data
    macro_signals = signals[signals['category'].isin(['ECONOMY'])]
    render_leaderboard(macro_signals, "Economic Data")

with tab7:
    # Filter for Global Factors
    macro_signals = signals[signals['category'].isin(['Global Factors'])]
    render_leaderboard(macro_signals, "Global Factors")

with tab8:
    # The "Dump" View - Shows everything
    render_leaderboard(signals, "All Aggregated Signals")

# 2. Headlines feed
st.header("Recent Headlines")
for _, row in articles.tail(20).iterrows():
    impacts = row['impacts']

    if isinstance(impacts, str):
        if impacts == "[]" or impacts == "":
            continue
    elif isinstance(impacts, list):
        if not impacts:  # Empty list
            continue
    else:
        continue  # Unexpected type

    st.write(f"[{row['published']}, Sentiment Score: {row['title_score']}] **{row['title']}**")
    st.caption(f"Impacts: {row['impacts']}")
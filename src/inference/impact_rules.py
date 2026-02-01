impact_rules = [
        # ==================== THAILAND ====================
    {
        'id': 'CORE_BOT_HAWKISH',
        'conditions': {
            'required_topics': ['CENTRAL_BANK'],
            'required_entities': ['THAILAND'],
            'sentiment_direction': 'negative'  # "Tightening", "Fighting inflation", "Rate hike" usually reads as Negative/Hawkish
        },
        'impact': 'Monetary Tightening Bias',
        'affected_asset': 'THB_POLICY',
        'confidence_base': 0.95,
        'reasoning': 'Indicates a shift towards controlling inflation via interest rates, bullish for currency yields.'
    },
    {
        'id': 'CORE_BOT_DOVISH',
        'conditions': {
            'required_topics': ['CENTRAL_BANK'],
            'required_entities': ['THAILAND'],
            'sentiment_direction': 'positive'  # "Supporting growth", "Rate cut", "Accommodative" usually reads as Positive/Dovish
        },
        'impact': 'Monetary Easing Bias',
        'affected_asset': 'THB_POLICY',
        'confidence_base': 0.95,
        'reasoning': 'Indicates a shift towards supporting growth, bearish for currency yields.'
    },
    {
        'id': 'CORE_THAI_INFLATION_PRESSURE',
        'conditions': {
            'required_topics': ['INFLATION'],
            'required_entities': ['THAILAND'],
            'sentiment_direction': 'negative'  # "Surging costs", "High CPI" is usually negative sentiment
        },
        'impact': 'High Inflation Environment',
        'affected_asset': 'THAI_INFLATION',
        'confidence_base': 0.9,
        'reasoning': 'Flags rising cost of living. This pressures the central bank and hurts consumer purchasing power.'
    },
    {
        'id': 'THAILAND_ECONOMY_UP',
        'conditions': {
            'required_topics': ['ECONOMIC_DATA'],
            'required_entities': ['THAILAND'],
            'sentiment_direction': 'positive'
        },
        'impact': 'Robust Economic Growth',
        'affected_asset': 'THAI_ECONOMY',
        'confidence_base': 0.95,
        'reasoning': 'Flags strong GDP, PMI, or export data indicating a healthy expansion.'
    },
    {
        'id': 'THAILAND_ECONOMY_DOWN',
        'conditions': {
            'required_topics': ['ECONOMIC_DATA'],
            'required_entities': ['THAILAND'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Economic Contraction / Slowdown',
        'affected_asset': 'THAI_ECONOMY',
        'confidence_base': 0.95,
        'reasoning': 'Flags weak GDP, PMI, or export data indicating a contraction.'
    },
    {
        'id': 'THAI_BOND_YIELD_RISING',
        'conditions': {
            'required_topics': ['BOND_MARKET'],
            'required_entities': ['THAILAND'],
            'sentiment_direction': 'negative'  # FinBERT tags "Rising Yields" or "Selloff" as Negative
        },
        'impact': 'Bond Prices Falling (Yields Rising)',
        'affected_asset': 'THAI_BONDS',
        'confidence_base': 0.9,
        'reasoning': 'Detects a selloff in Thai debt or rising interest rates. This signals Bearish sentiment for Bond Prices (and usually Bullish for the Currency).'
    },
    {
        'id': 'THAI_BOND_YIELD_FALLING',
        'conditions': {
            'required_topics': ['BOND_MARKET'],
            'required_entities': ['THAILAND'],
            'sentiment_direction': 'positive'  # FinBERT tags "Rally" or "Yields Dropping" as Positive
        },
        'impact': 'Bond Prices Rising (Yields Falling)',
        'affected_asset': 'THAI_BONDS',
        'confidence_base': 0.9,
        'reasoning': 'Detects demand for Thai safe assets or monetary easing expectations. This signals Bullish sentiment for Bond Prices (and usually Bearish for the Currency).'
    },
    {
        'id': 'THAI_EQUITY_UP',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['THAILAND'],
            'sentiment_direction': 'positive'
        },
        'impact': 'Robust Equity Performance',
        'affected_asset': 'THAI_EQUITY',
        'confidence_base': 0.95,
        'reasoning': 'Flags strength in the Thai stock market (SET). Indicates strong local liquidity, foreign fund inflows, or optimism in tourism/export sectors.'
    },
    {
        'id': 'THAI_EQUITY_DOWN',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['THAILAND'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Equity Market Weakness',
        'affected_asset': 'THAI_EQUITY',
        'confidence_base': 0.95,
        'reasoning': 'Flags weakness in the Thai stock market (SET). Signals foreign capital outflow or concerns over domestic economic growth/political stability.'
    },


        # ==================== UNITED STATES ====================
    {
        'id': 'CORE_FED_HAWKISH',
        'conditions': {
            'required_topics': ['CENTRAL_BANK'],
            'required_entities': ['USA', 'FEDERAL_RESERVE'],
            'sentiment_direction': 'negative'  # Hawkish = tightening = negative sentiment
        },
        'impact': 'Monetary Tightening Bias',
        'affected_asset': 'USD_POLICY', # Specific asset for Fed stance
        'confidence_base': 0.95,
        'reasoning': 'Indicates Fed is tightening policy or fighting inflation. Inherently bullish for USD yield.'
    },
    {
        'id': 'CORE_FED_DOVISH',
        'conditions': {
            'required_topics': ['CENTRAL_BANK'],
            'required_entities': ['USA', 'FEDERAL_RESERVE'],
            'sentiment_direction': 'positive'  # Dovish = easing = positive sentiment
        },
        'impact': 'Monetary Easing Bias',
        'affected_asset': 'USD_POLICY',
        'confidence_base': 0.95,
        'reasoning': 'Indicates Fed is supporting growth or cutting rates. Inherently bearish for USD yield.'
    },
    {
        'id': 'CORE_US_INFLATION_PRESSURE',
        'conditions': {
            'required_topics': ['INFLATION'],
            'required_entities': ['USA'],
            'sentiment_direction': 'positive' # "Surging inflation" usually positive sentiment regarding the topic magnitude
        },
        'impact': 'High Inflation Environment',
        'affected_asset': 'US_INFLATION',
        'confidence_base': 0.9,
        'reasoning': 'Flags rising price levels in the US, which typically forces a hawkish Fed response.'
    },
    {
        'id': 'US_TREASURY_YIELD_RISING',
        'conditions': {
            'required_topics': ['BOND_MARKET'],
            'required_entities': ['USA'],
            'sentiment_direction': 'negative' # "Yields spike", "Bond selloff" = Negative sentiment
        },
        'impact': 'Bond Prices Falling (Yields Rising)',
        'affected_asset': 'US_TREASURY',
        'confidence_base': 0.9,
        'reasoning': 'Detects a selloff in US Treasuries. Rising yields often attract global capital away from EM bonds.'
    },
    {
        'id': 'US_TREASURY_YIELD_FALLING',
        'conditions': {
            'required_topics': ['BOND_MARKET'],
            'required_entities': ['USA'],
            'sentiment_direction': 'positive' # "Yields drop", "Bond rally" = Positive sentiment
        },
        'impact': 'Bond Prices Rising (Yields Falling)',
        'affected_asset': 'US_TREASURY',
        'confidence_base': 0.9,
        'reasoning': 'Detects high demand for safe-haven US Treasuries. Falling yields reduce the rate appeal of the USD.'
    },
    {
        'id': 'US_EQUITY_UP',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['USA'],
            'sentiment_direction': 'positive'
        },
        'impact': 'Robust Equity Performance',
        'affected_asset': 'US_EQUITY',
        'confidence_base': 0.95,
        'reasoning': 'Flags strength in US stock markets (S&P 500, Nasdaq). Primary driver of global "Risk-On" sentiment.'
    },
    {
        'id': 'US_EQUITY_DOWN',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['USA'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Equity Market Weakness',
        'affected_asset': 'US_EQUITY',
        'confidence_base': 0.95,
        'reasoning': 'Flags weakness in US stock markets. Primary driver of global "Risk-Off" sentiment.'
    },
    {
        'id': 'US_ECONOMY_UP',
        'conditions': {
            'required_topics': ['ECONOMIC_DATA'],
            'required_entities': ['USA'],
            'sentiment_direction': 'positive'
        },
        'impact': 'Robust Economic Growth',
        'affected_asset': 'US_ECONOMY',
        'confidence_base': 0.95,
        'reasoning': 'Flags strong US data (Jobs, GDP, Retail Sales). Supports USD strength via growth differentials.'
    },
    {
        'id': 'US_ECONOMY_DOWN',
        'conditions': {
            'required_topics': ['ECONOMIC_DATA'],
            'required_entities': ['USA'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Economic Slowdown',
        'affected_asset': 'US_ECONOMY',
        'confidence_base': 0.95,
        'reasoning': 'Flags weak US data. Increases probability of Fed rate cuts, weakening USD.'
    },
    {
        'id': 'USD_STRENGTH',
        'conditions': {
            'required_topics': ['CURRENCY_MOVEMENT'],
            'required_entities': ['USD'],
            'sentiment_direction': 'positive'  # "Dollar rallies", "Strong demand" = Positive
        },
        'impact': 'USD Appreciation',
        'affected_asset': 'USD',
        'confidence_base': 0.95,
        'reasoning': 'Direct detection of US Dollar strength. Often driven by safe-haven flows or rate differentials.'
    },
    {
        'id': 'USD_WEAKNESS',
        'conditions': {
            'required_topics': ['CURRENCY_MOVEMENT'],
            'required_entities': ['USD'],
            'sentiment_direction': 'negative'  # "Dollar slumps", "Selling pressure" = Negative
        },
        'impact': 'USD Depreciation',
        'affected_asset': 'USD',
        'confidence_base': 0.95,
        'reasoning': 'Direct detection of US Dollar weakness. Often driven by dovish Fed policy or global risk-on appetite.'
    },

    # ==================== CHINA ====================
    {
        'id': 'CHINA_ECONOMY_UP',
        'conditions': {
            'required_topics': ['ECONOMIC_DATA'],
            'required_entities': ['CHINA'],
            'sentiment_direction': 'positive'
        },
        'impact': 'Robust Economic Growth',
        'affected_asset': 'CHINA_ECONOMY',
        'confidence_base': 0.95,
        'reasoning': 'Flags strong GDP, PMI, or industrial output. Primary driver for regional export demand.'
    },
    {
        'id': 'CHINA_ECONOMY_DOWN',
        'conditions': {
            'required_topics': ['ECONOMIC_DATA'],
            'required_entities': ['CHINA'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Economic Slowdown',
        'affected_asset': 'CHINA_ECONOMY',
        'confidence_base': 0.95,
        'reasoning': 'Flags weak Chinese data. Signals reduced demand for commodities and regional exports.'
    },
    {
        'id': 'CHINA_EQUITY_UP',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['CHINA'],
            'sentiment_direction': 'positive'
        },
        'impact': 'Equity Market Rally',
        'affected_asset': 'CHINA_EQUITY',
        'confidence_base': 0.95,
        'reasoning': 'Flags strength in Shanghai/Shenzhen markets. Signals "Risk-On" behavior in Asia.'
    },
    {
        'id': 'CHINA_EQUITY_DOWN',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['CHINA'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Equity Market Sell-off',
        'affected_asset': 'CHINA_EQUITY',
        'confidence_base': 0.95,
        'reasoning': 'Flags weakness in Chinese equities. Signals "Risk-Off" sentiment in the region.'
    },
    {
        'id': 'CHINA_BOND_YIELD_RISING',
        'conditions': {
            'required_topics': ['BOND_MARKET'],
            'required_entities': ['CHINA'],
            'sentiment_direction': 'negative' # "Yields spike", "Bond selloff" = Negative sentiment
        },
        'impact': 'Bond Prices Falling (Yields Rising)',
        'affected_asset': 'CHINA_BONDS',
        'confidence_base': 0.9,
        'reasoning': 'Detects a selloff in Chinese Government Bonds or tightening PBoC policy. Reduces liquidity stimulus.'
    },
    {
        'id': 'CHINA_BOND_YIELD_FALLING',
        'conditions': {
            'required_topics': ['BOND_MARKET'],
            'required_entities': ['CHINA'],
            'sentiment_direction': 'positive' # "Yields drop", "Bond rally", "Stimulus" = Positive sentiment
        },
        'impact': 'Bond Prices Rising (Yields Falling)',
        'affected_asset': 'CHINA_BONDS',
        'confidence_base': 0.9,
        'reasoning': 'Detects a flight to safety or PBoC easing. Falling yields signal monetary stimulus or growth fears.'
    },
        {
        'id': 'CNY_STRENGTH',
        'conditions': {
            'required_topics': ['CURRENCY_MOVEMENT'],
            'required_entities': ['CHINA'],
            'sentiment_direction': 'positive'  # "Yuan rallies", "PBOC support"
        },
        'impact': 'CNY Appreciation',
        'affected_asset': 'CNY',
        'confidence_base': 0.95,
        'reasoning': 'Direct detection of Chinese Yuan (RMB) strength. Driven by PBoC intervention, strong trade data, or capital inflows.'
    },
    {
        'id': 'CNY_WEAKNESS',
        'conditions': {
            'required_topics': ['CURRENCY_MOVEMENT'],
            'required_entities': ['CHINA'],
            'sentiment_direction': 'negative'  # "Yuan slumps", "Capital outflows"
        },
        'impact': 'CNY Depreciation',
        'affected_asset': 'CNY',
        'confidence_base': 0.95,
        'reasoning': 'Direct detection of Chinese Yuan weakness. Driven by economic slowdown fears, PBoC easing, or trade tensions.'
    },

    # ==================== INDIA ====================
    {
        'id': 'INDIA_ECONOMY_UP',
        'conditions': {
            'required_topics': ['ECONOMIC_DATA'],
            'required_entities': ['INDIA'],
            'sentiment_direction': 'positive'
        },
        'impact': 'Robust Economic Growth',
        'affected_asset': 'INDIA_ECONOMY',
        'confidence_base': 0.95,
        'reasoning': 'Flags strong Indian GDP, PMI, or industrial output. Primary driver for Asian regional demand.'
    },
    {
        'id': 'INDIA_ECONOMY_DOWN',
        'conditions': {
            'required_topics': ['ECONOMIC_DATA'],
            'required_entities': ['INDIA'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Economic Slowdown',
        'affected_asset': 'INDIA_ECONOMY',
        'confidence_base': 0.95,
        'reasoning': 'Flags weak Indian data. Signals reduced demand for commodities and regional imports.'
    },
    {
        'id': 'INDIA_EQUITY_UP',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['INDIA'],
            'sentiment_direction': 'positive'
        },
        'impact': 'Equity Market Rally',
        'affected_asset': 'INDIA_EQUITY',
        'confidence_base': 0.95,
        'reasoning': 'Flags strength in Indian markets (Nifty 50). Signals "Risk-On" behavior in Emerging Markets.'
    },
    {
        'id': 'INDIA_EQUITY_DOWN',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['INDIA'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Equity Market Sell-off',
        'affected_asset': 'INDIA_EQUITY',
        'confidence_base': 0.95,
        'reasoning': 'Flags weakness in Indian equities. Signals "Risk-Off" sentiment or foreign capital outflows from EM.'
    },
    {
        'id': 'INDIA_BOND_YIELD_RISING',
        'conditions': {
            'required_topics': ['BOND_MARKET'],
            'required_entities': ['INDIA'],
            'sentiment_direction': 'negative' # "Yields spike", "Bond selloff" = Negative sentiment
        },
        'impact': 'Bond Prices Falling (Yields Rising)',
        'affected_asset': 'INDIA_BONDS',
        'confidence_base': 0.9,
        'reasoning': 'Detects a selloff in Indian Government Bonds or tightening RBI policy. Reduces domestic liquidity.'
    },
    {
        'id': 'INDIA_BOND_YIELD_FALLING',
        'conditions': {
            'required_topics': ['BOND_MARKET'],
            'required_entities': ['INDIA'],
            'sentiment_direction': 'positive' # "Yields drop", "Bond rally", "Stimulus" = Positive sentiment
        },
        'impact': 'Bond Prices Rising (Yields Falling)',
        'affected_asset': 'INDIA_BONDS',
        'confidence_base': 0.9,
        'reasoning': 'Detects strong demand for Indian debt or RBI easing measures. Falling yields signal monetary accommodation.'
    },
    {
        'id': 'CORE_RBI_HAWKISH',
        'conditions': {
            'required_topics': ['CENTRAL_BANK'],
            'required_entities': ['INDIA'],
            'sentiment_direction': 'negative' # Hawkish/Tightening = Negative sentiment
        },
        'impact': 'Monetary Tightening Bias',
        'affected_asset': 'RBI_POLICY',
        'confidence_base': 0.95,
        'reasoning': 'Indicates RBI is raising rates to combat inflation. Bullish for INR yield, Bearish for equities.'
    },
    {
        'id': 'CORE_RBI_DOVISH',
        'conditions': {
            'required_topics': ['CENTRAL_BANK'],
            'required_entities': ['INDIA'],
            'sentiment_direction': 'positive' # Dovish/Easing = Positive sentiment
        },
        'impact': 'Monetary Easing Bias',
        'affected_asset': 'RBI_POLICY',
        'confidence_base': 0.95,
        'reasoning': 'Indicates RBI is cutting rates or pausing hikes to support growth. Bearish for INR yield, Bullish for equities.'
    },
    {
        'id': 'INR_STRENGTH',
        'conditions': {
            'required_topics': ['CURRENCY_MOVEMENT'],
            'required_entities': ['INDIA'],
            'sentiment_direction': 'positive'  # "Rupee rallies"
        },
        'impact': 'INR Appreciation',
        'affected_asset': 'INR',
        'confidence_base': 0.95,
        'reasoning': 'Direct detection of Indian Rupee strength. Driven by strong FDI inflows or RBI intervention.'
    },
    {
        'id': 'INR_WEAKNESS',
        'conditions': {
            'required_topics': ['CURRENCY_MOVEMENT'],
            'required_entities': ['INDIA'],
            'sentiment_direction': 'negative'  # "Rupee slumps"
        },
        'impact': 'INR Depreciation',
        'affected_asset': 'INR',
        'confidence_base': 0.95,
        'reasoning': 'Direct detection of Indian Rupee weakness. Driven by high oil import bills or widening trade deficit.'
    },

    # ==================== EUROPE ====================
    {
        'id': 'CORE_ECB_HAWKISH',
        'conditions': {
            'required_topics': ['CENTRAL_BANK'],
            'required_entities': ['EU'],
            'sentiment_direction': 'negative'  # Hawkish = tightening = negative sentiment
        },
        'impact': 'Monetary Tightening Bias',
        'affected_asset': 'EUR_POLICY',
        'confidence_base': 0.95,
        'reasoning': 'Indicates ECB is raising rates or reducing stimulus. Bullish for the Euro yield.'
    },
    {
        'id': 'CORE_ECB_DOVISH',
        'conditions': {
            'required_topics': ['CENTRAL_BANK'],
            'required_entities': ['EU'],
            'sentiment_direction': 'positive'  # Dovish = easing = positive sentiment
        },
        'impact': 'Monetary Easing Bias',
        'affected_asset': 'EUR_POLICY',
        'confidence_base': 0.95,
        'reasoning': 'Indicates ECB is cutting rates or adding stimulus. Bearish for the Euro yield.'
    },
    {
        'id': 'EU_BOND_YIELD_RISING',
        'conditions': {
            'required_topics': ['BOND_MARKET'],
            'required_entities': ['EU', 'GERMANY', 'BUND'], # Bunds are the EU benchmark
            'sentiment_direction': 'negative' # "Yields spike", "Selloff" = Negative sentiment
        },
        'impact': 'Bond Prices Falling (Yields Rising)',
        'affected_asset': 'EU_BONDS',
        'confidence_base': 0.9,
        'reasoning': 'Detects a selloff in European sovereign debt (Bunds). Rising yields reflect inflation concerns or growth expectations.'
    },
    {
        'id': 'EU_BOND_YIELD_FALLING',
        'conditions': {
            'required_topics': ['BOND_MARKET'],
            'required_entities': ['EU', 'GERMANY', 'BUND'],
            'sentiment_direction': 'positive' # "Yields drop", "Rally" = Positive sentiment
        },
        'impact': 'Bond Prices Rising (Yields Falling)',
        'affected_asset': 'EU_BONDS',
        'confidence_base': 0.9,
        'reasoning': 'Detects high demand for European safe-havens or expectations of economic slowdown.'
    },
    {
        'id': 'EU_EQUITY_UP',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['EU'],
            'sentiment_direction': 'positive'
        },
        'impact': 'Robust Equity Performance',
        'affected_asset': 'EU_EQUITY',
        'confidence_base': 0.95,
        'reasoning': 'Flags strength in European indices. Signals regional growth optimism and "Risk-On" sentiment.'
    },
    {
        'id': 'EU_EQUITY_DOWN',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['EU'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Equity Market Weakness',
        'affected_asset': 'EU_EQUITY',
        'confidence_base': 0.95,
        'reasoning': 'Flags weakness in European indices. Signals regional growth concerns or "Risk-Off" sentiment.'
    },
    {
        'id': 'EU_ECONOMY_UP',
        'conditions': {
            'required_topics': ['ECONOMIC_DATA'],
            'required_entities': ['EU'],
            'sentiment_direction': 'positive'
        },
        'impact': 'Robust Economic Growth',
        'affected_asset': 'EU_ECONOMY',
        'confidence_base': 0.95,
        'reasoning': 'Flags strong Eurozone data (GDP, PMI). Supports the Euro and global growth outlook.'
    },
    {
        'id': 'EU_ECONOMY_DOWN',
        'conditions': {
            'required_topics': ['ECONOMIC_DATA'],
            'required_entities': ['EU'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Economic Slowdown',
        'affected_asset': 'EU_ECONOMY',
        'confidence_base': 0.95,
        'reasoning': 'Flags weak Eurozone data. Undermines the Euro and suggests potential ECB support.'
    },
    {
        'id': 'EUR_STRENGTH',
        'conditions': {
            'required_topics': ['CURRENCY_MOVEMENT'],
            'required_entities': ['EUR'],
            'sentiment_direction': 'positive'  # "Euro rallies", "Euro soars" = Positive
        },
        'impact': 'EUR Appreciation',
        'affected_asset': 'EUR',
        'confidence_base': 0.95,
        'reasoning': 'Direct detection of Euro strength. Signals confidence in the Eurozone economy or ECB hawkishness.'
    },
    {
        'id': 'EUR_WEAKNESS',
        'conditions': {
            'required_topics': ['CURRENCY_MOVEMENT'],
            'required_entities': ['EUR'],
            'sentiment_direction': 'negative'  # "Euro slumps", "Euro falls" = Negative
        },
        'impact': 'EUR Depreciation',
        'affected_asset': 'EUR',
        'confidence_base': 0.95,
        'reasoning': 'Direct detection of Euro weakness. Signals fragmentation fears or ECB dovishness.'
    },

    # ==================== SOUTH KOREA ====================
    {
        'id': 'SOUTH_KOREA_ECONOMY_UP',
        'conditions': {
            'required_topics': ['ECONOMIC_DATA'],
            'required_entities': ['SOUTH_KOREA'],
            'sentiment_direction': 'positive'
        },
        'impact': 'Robust Economic Growth',
        'affected_asset': 'SOUTH_KOREA_ECONOMY',
        'confidence_base': 0.95,
        'reasoning': 'Flags strong Korean GDP, exports, or semiconductor output. A leading indicator for global tech demand.'
    },
    {
        'id': 'SOUTH_KOREA_ECONOMY_DOWN',
        'conditions': {
            'required_topics': ['ECONOMIC_DATA'],
            'required_entities': ['SOUTH_KOREA'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Economic Slowdown',
        'affected_asset': 'SOUTH_KOREA_ECONOMY',
        'confidence_base': 0.95,
        'reasoning': 'Flags weak Korean data. Signals slowing global trade or reduced demand for electronics/chips.'
    },
    {
        'id': 'SOUTH_KOREA_EQUITY_UP',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['SOUTH_KOREA'],
            'sentiment_direction': 'positive'
        },
        'impact': 'Equity Market Rally',
        'affected_asset': 'SOUTH_KOREA_EQUITY',
        'confidence_base': 0.95,
        'reasoning': 'Flags strength in the KOSPI. Indicates foreign investor confidence in Asian tech and manufacturing exports.'
    },
    {
        'id': 'SOUTH_KOREA_EQUITY_DOWN',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['SOUTH_KOREA'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Equity Market Sell-off',
        'affected_asset': 'SOUTH_KOREA_EQUITY',
        'confidence_base': 0.95,
        'reasoning': 'Flags weakness in the KOSPI. Signals "Risk-Off" sentiment in the Asian tech sector or foreign capital outflows.'
    },
    {
        'id': 'SOUTH_KOREA_BOND_YIELD_RISING',
        'conditions': {
            'required_topics': ['BOND_MARKET'],
            'required_entities': ['SOUTH_KOREA'],
            'sentiment_direction': 'negative' # "Yields spike", "Bond selloff" = Negative sentiment
        },
        'impact': 'Bond Prices Falling (Yields Rising)',
        'affected_asset': 'SOUTH_KOREA_BONDS',
        'confidence_base': 0.9,
        'reasoning': 'Detects a selloff in Korean Government Bonds or BOK tightening. Reduces domestic liquidity.'
    },
    {
        'id': 'SOUTH_KOREA_BOND_YIELD_FALLING',
        'conditions': {
            'required_topics': ['BOND_MARKET'],
            'required_entities': ['SOUTH_KOREA'],
            'sentiment_direction': 'positive' # "Yields drop", "Bond rally", "Stimulus" = Positive sentiment
        },
        'impact': 'Bond Prices Rising (Yields Falling)',
        'affected_asset': 'SOUTH_KOREA_BONDS',
        'confidence_base': 0.9,
        'reasoning': 'Detects strong demand for Korean debt or BOK easing. Falling yields signal monetary accommodation.'
    },
    {
        'id': 'CORE_BOK_HAWKISH',
        'conditions': {
            'required_topics': ['CENTRAL_BANK'],
            'required_entities': ['SOUTH_KOREA'],
            'sentiment_direction': 'negative' # Hawkish/Tightening = Negative sentiment
        },
        'impact': 'Monetary Tightening Bias',
        'affected_asset': 'BOK_POLICY',
        'confidence_base': 0.95,
        'reasoning': 'Indicates BOK is raising rates to combat inflation or support the Won. Bullish for KRW yield.'
    },
    {
        'id': 'CORE_BOK_DOVISH',
        'conditions': {
            'required_topics': ['CENTRAL_BANK'],
            'required_entities': ['SOUTH_KOREA'],
            'sentiment_direction': 'positive' # Dovish/Easing = Positive sentiment
        },
        'impact': 'Monetary Easing Bias',
        'affected_asset': 'BOK_POLICY',
        'confidence_base': 0.95,
        'reasoning': 'Indicates BOK is cutting rates or pausing hikes to support exports. Bearish for KRW yield.'
    },
    {
        'id': 'KRW_STRENGTH',
        'conditions': {
            'required_topics': ['CURRENCY_MOVEMENT'],
            'required_entities': ['SOUTH_KOREA'],
            'sentiment_direction': 'positive'  # "Won rallies"
        },
        'impact': 'KRW Appreciation',
        'affected_asset': 'KRW',
        'confidence_base': 0.95,
        'reasoning': 'Direct detection of Korean Won strength. Driven by export earnings or BOK intervention.'
    },
    {
        'id': 'KRW_WEAKNESS',
        'conditions': {
            'required_topics': ['CURRENCY_MOVEMENT'],
            'required_entities': ['SOUTH_KOREA'],
            'sentiment_direction': 'negative'  # "Won slumps"
        },
        'impact': 'KRW Depreciation',
        'affected_asset': 'KRW',
        'confidence_base': 0.95,
        'reasoning': 'Direct detection of Korean Won weakness. Driven by global risk aversion or deteriorating trade balance.'
    },
    
    # ==================== RUSSIA ====================
    {
        'id': 'RUSSIA_ECONOMY_UP',
        'conditions': {
            'required_topics': ['ECONOMIC_DATA'],
            'required_entities': ['RUSSIA'],
            'sentiment_direction': 'positive'
        },
        'impact': 'Resilient Economic Growth',
        'affected_asset': 'RUSSIA_ECONOMY',
        'confidence_base': 0.95,
        'reasoning': 'Flags strong Russian GDP or industrial output despite sanctions. Often driven by military spending or energy export pivots.'
    },
    {
        'id': 'RUSSIA_ECONOMY_DOWN',
        'conditions': {
            'required_topics': ['ECONOMIC_DATA'],
            'required_entities': ['RUSSIA'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Economic Contraction',
        'affected_asset': 'RUSSIA_ECONOMY',
        'confidence_base': 0.95,
        'reasoning': 'Flags weak Russian data. Signals impact of sanctions, labor shortages, or energy revenue decline.'
    },
    {
        'id': 'RUSSIA_EQUITY_UP',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['RUSSIA'],
            'sentiment_direction': 'positive'
        },
        'impact': 'Equity Market Rally',
        'affected_asset': 'RUSSIA_EQUITY',
        'confidence_base': 0.95,
        'reasoning': 'Flags strength in the MOEX index. Indicates domestic liquidity or optimism in state-controlled sectors.'
    },
    {
        'id': 'RUSSIA_EQUITY_DOWN',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['RUSSIA'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Equity Market Sell-off',
        'affected_asset': 'RUSSIA_EQUITY',
        'confidence_base': 0.95,
        'reasoning': 'Flags weakness in Russian equities. Signals escalating geopolitical risk or new sanctions.'
    },
    {
        'id': 'RUSSIA_BOND_YIELD_RISING',
        'conditions': {
            'required_topics': ['BOND_MARKET'],
            'required_entities': ['RUSSIA'],
            'sentiment_direction': 'negative' # "Yields spike", "Bond selloff" = Negative sentiment
        },
        'impact': 'Bond Prices Falling (Yields Rising)',
        'affected_asset': 'RUSSIA_BONDS',
        'confidence_base': 0.9,
        'reasoning': 'Detects a selloff in Russian debt (OFZ). Signals default risk, high inflation, or capital flight.'
    },
    {
        'id': 'RUSSIA_BOND_YIELD_FALLING',
        'conditions': {
            'required_topics': ['BOND_MARKET'],
            'required_entities': ['RUSSIA'],
            'sentiment_direction': 'positive' # "Yields drop", "Bond rally" = Positive sentiment
        },
        'impact': 'Bond Prices Rising (Yields Falling)',
        'affected_asset': 'RUSSIA_BONDS',
        'confidence_base': 0.9,
        'reasoning': 'Detects demand for Russian debt or CBR easing. Falling yields signal short-term stability or forced buying.'
    },
    {
        'id': 'CORE_CBR_HAWKISH',
        'conditions': {
            'required_topics': ['CENTRAL_BANK'],
            'required_entities': ['RUSSIA'],
            'sentiment_direction': 'negative' # Hawkish/Tightening = Negative sentiment
        },
        'impact': 'Monetary Tightening Bias',
        'affected_asset': 'CBR_POLICY',
        'confidence_base': 0.95,
        'reasoning': 'Indicates Central Bank of Russia is hiking rates to defend the RUB or curb inflation. Bullish for currency yield.'
    },
    {
        'id': 'CORE_CBR_DOVISH',
        'conditions': {
            'required_topics': ['CENTRAL_BANK'],
            'required_entities': ['RUSSIA'],
            'sentiment_direction': 'positive' # Dovish/Easing = Positive sentiment
        },
        'impact': 'Monetary Easing Bias',
        'affected_asset': 'CBR_POLICY',
        'confidence_base': 0.95,
        'reasoning': 'Indicates CBR is cutting rates to support the war economy. Bearish for RUB yield, risk of depreciation.'
    },
    {
        'id': 'RUB_STRENGTH',
        'conditions': {
            'required_topics': ['CURRENCY_MOVEMENT'],
            'required_entities': ['RUSSIA'],
            'sentiment_direction': 'positive'  # "Ruble rallies", "Capital controls"
        },
        'impact': 'RUB Appreciation',
        'affected_asset': 'RUB',
        'confidence_base': 0.95,
        'reasoning': 'Direct detection of Ruble strength. Driven by capital controls, energy revenues, or aggressive CBR intervention.'
    },
    {
        'id': 'RUB_WEAKNESS',
        'conditions': {
            'required_topics': ['CURRENCY_MOVEMENT'],
            'required_entities': ['RUSSIA'],
            'sentiment_direction': 'negative'  # "Ruble slumps", "Sanctions"
        },
        'impact': 'RUB Depreciation',
        'affected_asset': 'RUB',
        'confidence_base': 0.95,
        'reasoning': 'Direct detection of Ruble weakness. Driven by sanctions, military spending costs, or falling energy prices.'
    },

    # ==================== UNITED KINGDOM ====================
    {
        'id': 'CORE_BOE_HAWKISH',
        'conditions': {
            'required_topics': ['CENTRAL_BANK'],
            'required_entities': ['UK'],
            'sentiment_direction': 'negative'  # Hawkish = tightening = negative sentiment
        },
        'impact': 'Monetary Tightening Bias',
        'affected_asset': 'GBP_POLICY',
        'confidence_base': 0.95,
        'reasoning': 'Indicates BoE is raising rates to combat inflation. Bullish for GBP yield.'
    },
    {
        'id': 'CORE_BOE_DOVISH',
        'conditions': {
            'required_topics': ['CENTRAL_BANK'],
            'required_entities': ['UK'],
            'sentiment_direction': 'positive'  # Dovish = easing = positive sentiment
        },
        'impact': 'Monetary Easing Bias',
        'affected_asset': 'GBP_POLICY',
        'confidence_base': 0.95,
        'reasoning': 'Indicates BoE is cutting rates or pausing hikes. Bearish for GBP yield.'
    },
    {
        'id': 'UK_GILT_YIELD_RISING',
        'conditions': {
            'required_topics': ['BOND_MARKET'],
            'required_entities': ['UK'],
            'sentiment_direction': 'negative' # "Yields spike", "Selloff" = Negative sentiment
        },
        'impact': 'Bond Prices Falling (Yields Rising)',
        'affected_asset': 'UK_GILTS',
        'confidence_base': 0.9,
        'reasoning': 'Detects a selloff in UK Government Bonds (Gilts). Rising yields reflect inflation expectations or fiscal concerns.'
    },
    {
        'id': 'UK_GILT_YIELD_FALLING',
        'conditions': {
            'required_topics': ['BOND_MARKET'],
            'required_entities': ['UK'],
            'sentiment_direction': 'positive' # "Yields drop", "Rally" = Positive sentiment
        },
        'impact': 'Bond Prices Rising (Yields Falling)',
        'affected_asset': 'UK_GILTS',
        'confidence_base': 0.9,
        'reasoning': 'Detects high demand for Gilts or economic slowdown expectations.'
    },
    {
        'id': 'UK_EQUITY_UP',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['UK'],
            'sentiment_direction': 'positive'
        },
        'impact': 'Robust Equity Performance',
        'affected_asset': 'UK_EQUITY',
        'confidence_base': 0.95,
        'reasoning': 'Flags strength in UK stock markets. Signals regional risk appetite.'
    },
    {
        'id': 'UK_EQUITY_DOWN',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['UK'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Equity Market Weakness',
        'affected_asset': 'UK_EQUITY',
        'confidence_base': 0.95,
        'reasoning': 'Flags weakness in UK stock markets. Signals regional risk aversion.'
    },
    {
        'id': 'UK_ECONOMY_UP',
        'conditions': {
            'required_topics': ['ECONOMIC_DATA'],
            'required_entities': ['UK'],
            'sentiment_direction': 'positive'
        },
        'impact': 'Robust Economic Growth',
        'affected_asset': 'UK_ECONOMY',
        'confidence_base': 0.95,
        'reasoning': 'Flags strong UK economic data. Supports GBP and BoE tightening expectations.'
    },
    {
        'id': 'UK_ECONOMY_DOWN',
        'conditions': {
            'required_topics': ['ECONOMIC_DATA'],
            'required_entities': ['UK'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Economic Slowdown',
        'affected_asset': 'UK_ECONOMY',
        'confidence_base': 0.95,
        'reasoning': 'Flags weak UK economic data. Pressures GBP and increases probability of BoE support.'
    },
    {
        'id': 'GBP_STRENGTH',
        'conditions': {
            'required_topics': ['CURRENCY_MOVEMENT'],
            'required_entities': ['UK'],
            'sentiment_direction': 'positive' # "Pound rallies", "GBP surges"
        },
        'impact': 'GBP Appreciation',
        'affected_asset': 'GBP',
        'confidence_base': 0.9,
        'reasoning': 'Direct detection of Pound Sterling strength vs trading partners.'
    },
    {
        'id': 'GBP_WEAKNESS',
        'conditions': {
            'required_topics': ['CURRENCY_MOVEMENT'],
            'required_entities': ['UK'],
            'sentiment_direction': 'negative' # "Pound slumps", "GBP plunges"
        },
        'impact': 'GBP Depreciation',
        'affected_asset': 'GBP',
        'confidence_base': 0.9,
        'reasoning': 'Direct detection of Pound Sterling weakness.'
    },

    # ==================== JAPAN ====================
    {
        'id': 'JAPAN_EQUITY_UP',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['JAPAN'],
            'sentiment_direction': 'positive'
        },
        'impact': 'Robust Equity Performance',
        'affected_asset': 'JAPAN_EQUITY',
        'confidence_base': 0.95,
        'reasoning': 'Flags strength in Japanese stock markets (Nikkei). Often correlates with "Risk-On" sentiment and weak Yen (Carry Trade).'
    },
    {
        'id': 'JAPAN_EQUITY_DOWN',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['JAPAN'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Equity Market Weakness',
        'affected_asset': 'JAPAN_EQUITY',
        'confidence_base': 0.95,
        'reasoning': 'Flags weakness in Japanese stock markets. Signals regional risk aversion or potential Carry Trade unwinding.'
    },
    {
        'id': 'JAPAN_ECONOMY_UP',
        'conditions': {
            'required_topics': ['ECONOMIC_DATA'],
            'required_entities': ['JAPAN'],
            'sentiment_direction': 'positive'
        },
        'impact': 'Robust Economic Growth',
        'affected_asset': 'JAPAN_ECONOMY',
        'confidence_base': 0.95,
        'reasoning': 'Flags strong Japanese economic data. Increases pressure on BoJ to normalize policy (Bullish for JPY).'
    },
    {
        'id': 'JAPAN_ECONOMY_DOWN',
        'conditions': {
            'required_topics': ['ECONOMIC_DATA'],
            'required_entities': ['JAPAN'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Economic Slowdown',
        'affected_asset': 'JAPAN_ECONOMY',
        'confidence_base': 0.95,
        'reasoning': 'Flags weak Japanese economic data. Reinforces BoJ ultra-easy policy stance (Bearish for JPY).'
    },
    {
        'id': 'CORE_BOJ_HAWKISH',
        'conditions': {
            'required_topics': ['CENTRAL_BANK'],
            'required_entities': ['JAPAN'],
            'sentiment_direction': 'negative' # Hawkish/Tightening = Negative sentiment for markets
        },
        'impact': 'Monetary Tightening Bias',
        'affected_asset': 'BOJ_POLICY',
        'confidence_base': 0.95,
        'reasoning': 'Indicates Bank of Japan is shifting away from ultra-loose policy (YCC adjustments). Strongly Bullish for JPY.'
    },
    {
        'id': 'CORE_BOJ_DOVISH',
        'conditions': {
            'required_topics': ['CENTRAL_BANK'],
            'required_entities': ['JAPAN'],
            'sentiment_direction': 'positive' # Dovish/Stimulus = Positive sentiment
        },
        'impact': 'Monetary Easing Bias',
        'affected_asset': 'BOJ_POLICY',
        'confidence_base': 0.95,
        'reasoning': 'Indicates Bank of Japan is maintaining or increasing stimulus. Bearish for JPY, supportive for Carry Trades.'
    },
    {
        'id': 'JGB_YIELD_RISING',
        'conditions': {
            'required_topics': ['BOND_MARKET'],
            'required_entities': ['JAPAN'],
            'sentiment_direction': 'negative' # "Yields spike", "Selloff" = Negative sentiment
        },
        'impact': 'Bond Prices Falling (Yields Rising)',
        'affected_asset': 'JGB',
        'confidence_base': 0.9,
        'reasoning': 'Detects a selloff in Japanese Government Bonds (JGBs). Rising yields suggest policy normalization or inflation expectations (Bullish for JPY).'
    },
    {
        'id': 'JGB_YIELD_FALLING',
        'conditions': {
            'required_topics': ['BOND_MARKET'],
            'required_entities': ['JAPAN'],
            'sentiment_direction': 'positive' # "Yields drop", "Rally" = Positive sentiment
        },
        'impact': 'Bond Prices Rising (Yields Falling)',
        'affected_asset': 'JGB',
        'confidence_base': 0.9,
        'reasoning': 'Detects high demand for JGBs or deflationary concerns. Falling yields reinforce BoJ easy policy (Bearish for JPY).'
    },
    {
        'id': 'JPY_STRENGTH',
        'conditions': {
            'required_topics': ['CURRENCY_MOVEMENT'],
            'required_entities': ['JAPAN'],
            'sentiment_direction': 'positive' # "Yen surges", "Safe haven flows"
        },
        'impact': 'JPY Appreciation',
        'affected_asset': 'JPY',
        'confidence_base': 0.9,
        'reasoning': 'Direct detection of Yen strength. Often signals global "Risk-Off" sentiment or BoJ intervention.'
    },
    {
        'id': 'JPY_WEAKNESS',
        'conditions': {
            'required_topics': ['CURRENCY_MOVEMENT'],
            'required_entities': ['JAPAN'],
            'sentiment_direction': 'negative' # "Yen slumps", "Weakness"
        },
        'impact': 'JPY Depreciation',
        'affected_asset': 'JPY',
        'confidence_base': 0.9,
        'reasoning': 'Direct detection of Yen weakness. Often signals global "Risk-On" sentiment or Carry Trade expansion.'
    },

        # ==================== INDONESIA ====================
    {
        'id': 'INDO_EQUITY_UP',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['INDONESIA'],
            'sentiment_direction': 'positive'
        },
        'impact': 'Robust Equity Performance',
        'affected_asset': 'INDO_EQUITY',
        'confidence_base': 0.95,
        'reasoning': 'Flags strength in Indonesian markets (JCI). Indicates strong regional EM risk appetite.'
    },
    {
        'id': 'INDO_EQUITY_DOWN',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['INDONESIA'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Equity Market Weakness',
        'affected_asset': 'INDO_EQUITY',
        'confidence_base': 0.95,
        'reasoning': 'Flags weakness in Indonesian markets. Signals "Risk-Off" sentiment in the Southeast Asian region.'
    },
    {
        'id': 'INDO_ECONOMY_UP',
        'conditions': {
            'required_topics': ['ECONOMIC_DATA'],
            'required_entities': ['INDONESIA'],
            'sentiment_direction': 'positive'
        },
        'impact': 'Robust Economic Growth',
        'affected_asset': 'INDO_ECONOMY',
        'confidence_base': 0.95,
        'reasoning': 'Flags strong Indonesian growth data (consumption, commodities).'
    },
    {
        'id': 'INDO_ECONOMY_DOWN',
        'conditions': {
            'required_topics': ['ECONOMIC_DATA'],
            'required_entities': ['INDONESIA'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Economic Slowdown',
        'affected_asset': 'INDO_ECONOMY',
        'confidence_base': 0.95,
        'reasoning': 'Flags weak Indonesian economic data.'
    },
    {
        'id': 'CORE_BI_HAWKISH',
        'conditions': {
            'required_topics': ['CENTRAL_BANK'],
            'required_entities': ['INDONESIA'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Monetary Tightening Bias',
        'affected_asset': 'BI_POLICY',
        'confidence_base': 0.95,
        'reasoning': 'Indicates Bank of Indonesia is tightening policy. Bullish for the Rupiah.'
    },
    {
        'id': 'IDR_STRENGTH',
        'conditions': {
            'required_topics': ['CURRENCY_MOVEMENT'],
            'required_entities': ['INDONESIA'],
            'sentiment_direction': 'positive'
        },
        'impact': 'IDR Appreciation',
        'affected_asset': 'IDR',
        'confidence_base': 0.9,
        'reasoning': 'Direct detection of Rupiah strength.'
    },

        # ==================== CANADA ====================
    {
        'id': 'CANADIAN_EQUITY_UP',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['CANADA'],
            'sentiment_direction': 'positive'
        },
        'impact': 'Robust Equity Performance',
        'affected_asset': 'CANADA_EQUITY',
        'confidence_base': 0.95,
        'reasoning': 'Flags strength in Canadian markets (TSX). Often driven by energy and financial sector performance.'
    },
    {
        'id': 'CANADIAN_EQUITY_DOWN',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['CANADA'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Equity Market Weakness',
        'affected_asset': 'CANADA_EQUITY',
        'confidence_base': 0.95,
        'reasoning': 'Flags weakness in Canadian markets. Signals risk-off in commodity-linked economies.'
    },
    {
        'id': 'CANADA_ECONOMY_UP',
        'conditions': {
            'required_topics': ['ECONOMIC_DATA'],
            'required_entities': ['CANADA'],
            'sentiment_direction': 'positive'
        },
        'impact': 'Robust Economic Growth',
        'affected_asset': 'CANADA_ECONOMY',
        'confidence_base': 0.95,
        'reasoning': 'Flags strong Canadian economic data.'
    },
    {
        'id': 'CANADA_ECONOMY_DOWN',
        'conditions': {
            'required_topics': ['ECONOMIC_DATA'],
            'required_entities': ['CANADA'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Economic Slowdown',
        'affected_asset': 'CANADA_ECONOMY',
        'confidence_base': 0.95,
        'reasoning': 'Flags weak Canadian economic data.'
    },
    {
        'id': 'CORE_BOC_HAWKISH',
        'conditions': {
            'required_topics': ['CENTRAL_BANK'],
            'required_entities': ['CANADA'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Monetary Tightening Bias',
        'affected_asset': 'BOC_POLICY',
        'confidence_base': 0.95,
        'reasoning': 'Indicates Bank of Canada is tightening policy. Bullish for the Canadian Dollar.'
    },
    {
        'id': 'CAD_STRENGTH',
        'conditions': {
            'required_topics': ['CURRENCY_MOVEMENT'],
            'required_entities': ['CANADA'],
            'sentiment_direction': 'positive'
        },
        'impact': 'CAD Appreciation',
        'affected_asset': 'CAD',
        'confidence_base': 0.9,
        'reasoning': 'Direct detection of Canadian Dollar strength. Often correlated with Oil prices.'
    },

    # ==================== GLOBAL / SECTORS / COMMODITIES ====================

        # ==================== GEOPOLITICS ====================
    {
        'id': 'CORE_GEOPOLITICAL_RISK_UP',
        'conditions': {
            'required_topics': ['GEOPOLITICAL_RISK'],
            'required_entities': [],
            'sentiment_direction': 'negative'  # War, Tension, Conflict = Negative sentiment
        },
        'impact': 'Elevated Global Risk',
        'affected_asset': 'GEOPOLITICS',
        'confidence_base': 0.9,
        'reasoning': 'Flags rising instability, conflicts, or geopolitical tensions. Generally triggers safe-haven flows (USD, JPY, GOLD).'
    },

    # ==================== COMMODITIES ====================
    {
        'id': 'COMMODITY_OIL_UP',
        'conditions': {
            'required_topics': ['COMMODITY_ENERGY'],
            'required_entities': [],
            'sentiment_direction': 'positive'  # "Oil surges", "Prices rally"
        },
        'impact': 'Energy Price Appreciation',
        'affected_asset': 'COMMODITY_ENERGY',
        'confidence_base': 0.95,
        'reasoning': 'Flags rising energy prices (Crude, Nat Gas). Inflationary signal for net importers like Thailand.'
    },
    {
        'id': 'COMMODITY_OIL_DOWN',
        'conditions': {
            'required_topics': ['COMMODITY_ENERGY'],
            'required_entities': [],
            'sentiment_direction': 'negative'  # "Oil plunges", "Demand slump"
        },
        'impact': 'Energy Price Depreciation',
        'affected_asset': 'COMMODITY_ENERGY',
        'confidence_base': 0.95,
        'reasoning': 'Flags falling energy prices. Deflationary signal and cost relief for importers.'
    },
    {
        'id': 'COMMODITY_METALS_BASE_UP',
        'conditions': {
            'required_topics': ['COMMODITY_BASE_METALS'],
            'required_entities': [],
            'sentiment_direction': 'positive'  # "Copper rallies", "Iron ore surges"
        },
        'impact': 'Industrial Demand Optimism',
        'affected_asset': 'COMMODITY_METALS_BASE',
        'confidence_base': 0.9,
        'reasoning': 'Flags strong demand for industrial metals. Signals global manufacturing growth and "Risk-On" sentiment.'
    },
    {
        'id': 'COMMODITY_METALS_BASE_DOWN',
        'conditions': {
            'required_topics': ['COMMODITY_BASE_METALS'],
            'required_entities': [],
            'sentiment_direction': 'negative'  # "Copper crashes", "Metal slump"
        },
        'impact': 'Industrial Demand Slowdown',
        'affected_asset': 'COMMODITY_METALS_BASE',
        'confidence_base': 0.9,
        'reasoning': 'Flags weakening demand for industrial metals. Signals global manufacturing slowdown or recession fears.'
    },
    {
        'id': 'COMMODITY_METALS_PRECIOUS_UP',
        'conditions': {
            'required_topics': ['COMMODITY_PRECIOUS_METALS'],
            'required_entities': [],
            'sentiment_direction': 'positive'  # "Gold hits high", "Safe haven buying"
        },
        'impact': 'Safe-Haven Demand / Inflation Hedging',
        'affected_asset': 'COMMODITY_METALS_PRECIOUS',
        'confidence_base': 0.9,
        'reasoning': 'Flags rising Gold/Silver prices. Typically indicates fear (Risk-Off) or inflation hedging.'
    },
    {
        'id': 'COMMODITY_METALS_PRECIOUS_DOWN',
        'conditions': {
            'required_topics': ['COMMODITY_PRECIOUS_METALS'],
            'required_entities': [],
            'sentiment_direction': 'negative'  # "Gold sells off"
        },
        'impact': 'Reduced Fear / Lower Inflation Expectations',
        'affected_asset': 'COMMODITY_METALS_PRECIOUS',
        'confidence_base': 0.9,
        'reasoning': 'Flags falling Gold/Silver prices. Typically indicates "Risk-On" sentiment or reduced inflation worries.'
    },
    {
        'id': 'COMMODITY_AGRI_UP',
        'conditions': {
            'required_topics': ['COMMODITY_AGRICULTURE'],
            'required_entities': [],
            'sentiment_direction': 'positive'  # "Crop prices surge"
        },
        'impact': 'Food Price Inflation',
        'affected_asset': 'COMMODITY_AGRI',
        'confidence_base': 0.85,
        'reasoning': 'Flags rising agricultural prices. Direct contributor to CPI inflation, relevant for emerging markets.'
    },
    {
        'id': 'COMMODITY_AGRI_DOWN',
        'conditions': {
            'required_topics': ['COMMODITY_AGRICULTURE'],
            'required_entities': [],
            'sentiment_direction': 'negative'  # "Grain prices slump"
        },
        'impact': 'Food Price Deflation',
        'affected_asset': 'COMMODITY_AGRI',
        'confidence_base': 0.85,
        'reasoning': 'Flags falling agricultural prices. Relief measure for food inflation.'
    },
    {
        'id': 'CRYPTO_UP',
        'conditions': {
            'required_topics': ['COMMODITY_CRYPTO'],
            'required_entities': [],
            'sentiment_direction': 'positive'  # "Bitcoin rallies"
        },
        'impact': 'High Risk Appetite / Speculative Euphoria',
        'affected_asset': 'CRYPTO',
        'confidence_base': 0.8,
        'reasoning': 'Flags strength in crypto markets. A leading indicator of excess liquidity and "Risk-On" sentiment.'
    },
    {
        'id': 'CRYPTO_DOWN',
        'conditions': {
            'required_topics': ['COMMODITY_CRYPTO'],
            'required_entities': [],
            'sentiment_direction': 'negative'  # "Crypto crash"
        },
        'impact': 'Risk Aversion / Liquidity Withdrawal',
        'affected_asset': 'CRYPTO',
        'confidence_base': 0.8,
        'reasoning': 'Flags weakness in crypto markets. Often signals broader risk aversion or liquidity stress.'
    },

    # SECTORS
    {
        'id': 'TECH_SECTOR_UP',
        'conditions': {
            'required_topics': ['TECHNOLOGY'],
            'required_entities': [], # Global scope (US, Taiwan, China)
            'sentiment_direction': 'positive'
        },
        'impact': 'High Growth Liquidity',
        'affected_asset': 'TECH_SECTOR',
        'confidence_base': 0.9,
        'reasoning': 'Flags strength in the technology sector. Indicates abundant global liquidity and high investor confidence in growth/risk assets.'
    },
    {
        'id': 'TECH_SECTOR_DOWN',
        'conditions': {
            'required_topics': ['TECHNOLOGY'],
            'required_entities': [], # Global scope
            'sentiment_direction': 'negative'
        },
        'impact': 'Growth De-risking / Liquidity Drain',
        'affected_asset': 'TECH_SECTOR',
        'confidence_base': 0.9,
        'reasoning': 'Flags weakness in the technology sector. Often the "canary in the coal mine" for broader market de-risking or interest rate fears.'
    },
]
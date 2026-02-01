impact_rules = [
    # ==================== THAILAND SPECIFIC ====================
    {
        'id': 'CORE_BOT_HAWKISH',
        'conditions': {
            'required_topics': ['CENTRAL_BANK'],
            'required_entities': ['THAILAND'],
            'sentiment_direction': 'negative'  # Negative sentiment = hawkish (tightening)
        },
        'impact': 'THB appreciation pressure, short-term Thai bond yields rise',
        'affected_asset': 'THB/USD',
        'confidence_base': 0.85,
        'reasoning': 'Direct hawkish signal from Bank of Thailand supports THB via interest rate differentials.'
    },
    {
        'id': 'CORE_BOT_DOVISH',
        'conditions': {
            'required_topics': ['CENTRAL_BANK'],
            'required_entities': ['THAILAND'],
            'sentiment_direction': 'positive'  # Positive sentiment = dovish (easing)
        },
        'impact': 'THB depreciation pressure, short-term Thai bond yields fall',
        'affected_asset': 'THB/USD',
        'confidence_base': 0.85,
        'reasoning': 'Direct dovish signal from Bank of Thailand weakens THB via rate cut expectations.'
    },
    {
        'id': 'CORE_THAI_INFLATION_UP',
        'conditions': {
            'required_topics': ['INFLATION'],
            'required_entities': ['THAILAND'],
            'sentiment_direction': 'positive'  # Positive sentiment about inflation = higher inflation
        },
        'impact': 'Increased BOT tightening expectations, THB support, bond sell-off pressure',
        'affected_asset': 'THB/USD',
        'confidence_base': 0.75,
        'reasoning': 'Rising Thai inflation prompts expectations of monetary tightening, supporting THB.'
    },
    
    # ==================== UNITED STATES ====================
    {
        'id': 'CORE_FED_HAWKISH',
        'conditions': {
            'required_topics': ['CENTRAL_BANK'],
            'required_entities': ['USA', 'FEDERAL_RESERVE'],
            'sentiment_direction': 'negative'  # Hawkish = negative sentiment
        },
        'impact': 'THB depreciation vs USD, upward pressure on Thai bond yields',
        'affected_asset': 'THB/USD',
        'confidence_base': 0.8,
        'reasoning': 'Hawkish Fed strengthens USD via rate differentials and safe-haven flows, pressuring EM currencies.'
    },
    {
        'id': 'CORE_FED_DOVISH',
        'conditions': {
            'required_topics': ['CENTRAL_BANK'],
            'required_entities': ['USA', 'FEDERAL_RESERVE'],
            'sentiment_direction': 'positive'  # Dovish = positive sentiment
        },
        'impact': 'THB appreciation vs USD, downward pressure on Thai bond yields',
        'affected_asset': 'THB/USD',
        'confidence_base': 0.8,
        'reasoning': 'Dovish Fed weakens USD, supportive for EM capital inflows and currencies like THB.'
    },
    {
        'id': 'CORE_US_INFLATION_UP',
        'conditions': {
            'required_topics': ['INFLATION'],
            'required_entities': ['USA'],
            'sentiment_direction': 'positive'
        },
        'impact': 'Fed tightening expectations increase, THB depreciation vs USD',
        'affected_asset': 'THB/USD',
        'confidence_base': 0.7,
        'reasoning': 'High US inflation forces Fed hawkish response, strengthening USD globally.'
    },
    
    # ==================== CHINA ====================
    {
        'id': 'CORE_CHINA_ECONOMIC_WEAKNESS',
        'conditions': {
            'required_topics': ['ECONOMIC_DATA'],
            'required_entities': ['CHINA'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Asian FX volatility increase, negative Thai export outlook, THB pressure',
        'affected_asset': 'THB/USD',
        'confidence_base': 0.75,
        'reasoning': 'China slowdown reduces regional growth and trade, pressuring Asian currencies including THB.'
    },
    {
        'id': 'CORE_CHINA_STIMULUS',
        'conditions': {
            'required_topics': ['ECONOMIC_DATA', 'CENTRAL_BANK'],
            'required_entities': ['CHINA'],
            'sentiment_direction': 'positive'
        },
        'impact': 'Asian growth optimism, THB supportive via trade channel',
        'affected_asset': 'THB/USD',
        'confidence_base': 0.65,
        'reasoning': 'Chinese stimulus boosts regional growth prospects and export demand, supporting THB.'
    },
    
    # ==================== EUROPE ====================
    {
        'id': 'CORE_ECB_HAWKISH',
        'conditions': {
            'required_topics': ['CENTRAL_BANK'],
            'required_entities': ['EU', 'ECB'],
            'sentiment_direction': 'negative'
        },
        'impact': 'EUR strength may pressure USD, indirect THB support vs USD',
        'affected_asset': 'THB/USD',
        'confidence_base': 0.6,
        'reasoning': 'Hawkish ECB strengthens EUR, potentially weakening USD index, providing indirect support to THB.'
    },
    {
        'id': 'CORE_ECB_DOVISH',
        'conditions': {
            'required_topics': ['CENTRAL_BANK'],
            'required_entities': ['EU', 'ECB'],
            'sentiment_direction': 'positive'
        },
        'impact': 'EUR weakness may boost USD, indirect THB pressure vs USD',
        'affected_asset': 'THB/USD',
        'confidence_base': 0.6,
        'reasoning': 'Dovish ECB weakens EUR, potentially strengthening USD index, pressuring THB indirectly.'
    },
    
    
    # ==================== GEOPOLITICAL ====================
    {
        'id': 'CORE_GEOPOLITICAL_RISK_UP',
        'conditions': {
            'required_topics': ['GEOPOLITICAL_RISK'],
            'required_entities': [],  # Any region
            'sentiment_direction': 'negative'
        },
        'impact': 'Safe-haven USD demand, Asian FX volatility increase, THB pressure',
        'affected_asset': 'THB/USD',
        'confidence_base': 0.65,
        'reasoning': 'Geopolitical tension drives flight to safety (USD), increasing volatility and pressuring EM currencies.'
    },
    
    # ==================== BROAD USD TREND ====================
    {
        'id': 'CORE_USD_WEAKNESS_BROAD',
        'conditions': {
            'required_topics': ['CURRENCY_MOVEMENT'],
            'required_entities': ['USD'],
            'sentiment_direction': 'negative'  # Negative sentiment about USD
        },
        'impact': 'THB appreciation vs USD',
        'affected_asset': 'THB/USD',
        'confidence_base': 0.75,
        'reasoning': 'Broad USD weakness directly translates to THB appreciation via exchange rate mechanism.'
    },
    {
        'id': 'CORE_USD_STRENGTH_BROAD',
        'conditions': {
            'required_topics': ['CURRENCY_MOVEMENT'],
            'required_entities': ['USD'],
            'sentiment_direction': 'positive'  # Positive sentiment about USD
        },
        'impact': 'THB depreciation vs USD',
        'affected_asset': 'THB/USD',
        'confidence_base': 0.75,
        'reasoning': 'Broad USD strength directly translates to THB depreciation via exchange rate mechanism.'
    },

   # ======= COMMODITY RULES ======= #

    # ENERGY (THAILAND = NET IMPORTER)
    {
        'id': 'COMMODITY_ENERGY_UP',
        'conditions': {
            'required_topics': ['COMMODITY_ENERGY'],
            'required_entities': [],
            'sentiment_direction': 'positive'
        },
        'impact': 'THB depreciation pressure, Thai inflation upside risk',
        'affected_asset': 'THB/USD',
        'confidence_base': 0.7,
        'reasoning': 'Thailand imports over 60% of its oil. Higher energy prices worsen trade balance and increase import costs, pressuring THB.'
    },
    {
        'id': 'COMMODITY_ENERGY_DOWN',
        'conditions': {
            'required_topics': ['COMMODITY_ENERGY'],
            'required_entities': [],
            'sentiment_direction': 'negative'
        },
        'impact': 'THB appreciation support, Thai inflation relief',
        'affected_asset': 'THB/USD',
        'confidence_base': 0.65,
        'reasoning': 'Lower energy prices improve Thailand\'s trade balance and reduce import cost inflation, supportive for THB.'
    },

    # BASE METALS (INDUSTRIAL DEMAND PROXY)
    {
        'id': 'COMMODITY_BASE_METALS_UP',
        'conditions': {
            'required_topics': ['COMMODITY_BASE_METALS'],
            'required_entities': [],
            'sentiment_direction': 'positive'
        },
        'impact': 'Global growth optimism signal, mixed THB impact',
        'affected_asset': 'GLOBAL_GROWTH_OUTLOOK',
        'confidence_base': 0.6,
        'reasoning': 'Base metals rally suggests strong industrial demand and global growth, which supports Thai exports but may increase input costs.'
    },
    {
        'id': 'COMMODITY_BASE_METALS_DOWN',
        'conditions': {
            'required_topics': ['COMMODITY_BASE_METALS'],
            'required_entities': [],
            'sentiment_direction': 'negative'
        },
        'impact': 'Global growth concern signal, risk-off sentiment',
        'affected_asset': 'GLOBAL_GROWTH_OUTLOOK',
        'confidence_base': 0.6,
        'reasoning': 'Base metals decline indicates weakening industrial demand, negative for global growth and Thai export outlook.'
    },

    # PRECIOUS METALS (SAFE HAVEN/INFLATION HEDGE)
    {
        'id': 'COMMODITY_PRECIOUS_METALS_UP',
        'conditions': {
            'required_topics': ['COMMODITY_PRECIOUS_METALS'],
            'required_entities': [],
            'sentiment_direction': 'positive'
        },
        'impact': 'Safe-haven demand signal, potential USD weakness',
        'affected_asset': 'GLOBAL_RISK_SENTIMENT',
        'confidence_base': 0.65,
        'reasoning': 'Precious metals surge often indicates risk-off sentiment or inflation hedging, which may correlate with USD weakness (supportive for THB).'
    },
    {
        'id': 'COMMODITY_PRECIOUS_METALS_DOWN',
        'conditions': {
            'required_topics': ['COMMODITY_PRECIOUS_METALS'],
            'required_entities': [],
            'sentiment_direction': 'negative'
        },
        'impact': 'Risk-on sentiment signal, reduced inflation hedging',
        'affected_asset': 'GLOBAL_RISK_SENTIMENT',
        'confidence_base': 0.55,
        'reasoning': 'Precious metals decline suggests improving risk appetite or reduced inflation fears, potentially supporting risk assets.'
    },

    # AGRICULTURE (FOOD INFLATION, COUNTRY-SPECIFIC)
    {
        'id': 'COMMODITY_AGRICULTURE_UP',
        'conditions': {
            'required_topics': ['COMMODITY_AGRICULTURE'],
            'required_entities': [],
            'sentiment_direction': 'positive'
        },
        'impact': 'Food inflation risk, mixed impact depending on Thailand\'s net trade position for specific commodity',
        'affected_asset': 'THAI_INFLATION',
        'confidence_base': 0.5,
        'reasoning': 'Agricultural price increases contribute to food inflation. Impact on THB depends on whether Thailand is net exporter or importer of that specific commodity.'
    },
    {
        'id': 'COMMODITY_AGRICULTURE_DOWN',
        'conditions': {
            'required_topics': ['COMMODITY_AGRICULTURE'],
            'required_entities': [],
            'sentiment_direction': 'negative'
        },
        'impact': 'Food inflation relief, potential support for consumer spending',
        'affected_asset': 'THAI_INFLATION',
        'confidence_base': 0.5,
        'reasoning': 'Lower agricultural prices ease food inflation pressures, potentially supporting Thai consumer demand.'
    },

    # CRYPTO
    {
        'id': 'CRYPTO_UP',
        'conditions': {
            'required_topics': ['COMMODITY_CRYPTO'],
            'required_entities': [],
            'sentiment_direction': 'positive'
        },
        'impact': 'Risk-on sentiment indicator, potential USD weakness correlation',
        'affected_asset': 'GLOBAL_RISK_SENTIMENT',
        'confidence_base': 0.4,
        'reasoning': 'Crypto rallies often correlate with high risk appetite and sometimes USD weakness, but the relationship is volatile and not fundamentally driven like traditional assets.'
    },
    {
        'id': 'CRYPTO_DOWN',
        'conditions': {
            'required_topics': ['COMMODITY_CRYPTO'],
            'required_entities': [],
            'sentiment_direction': 'negative'
        },
        'impact': 'Risk-off sentiment indicator, potential liquidity stress signal',
        'affected_asset': 'GLOBAL_RISK_SENTIMENT',
        'confidence_base': 0.45,
        'reasoning': 'Sharp crypto sell-offs can signal broader risk aversion or liquidity withdrawal from speculative assets, contributing to negative market sentiment.'
    },

    # ===== EQUITY MARKET RULES ===== #

    # INDONESIA (EMERGING MARKET PEER - CONTAGION/RISK SENTIMENT)
    {
        'id': 'INDONESIA_EQUITY_UP',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['INDONESIA'],
            'sentiment_direction': 'positive'
        },
        'impact': 'Positive EM sentiment, supportive for regional risk appetite and Thai equities',
        'affected_asset': 'THAI_EQUITY',
        'confidence_base': 0.6,
        'reasoning': 'Indonesian equity strength signals improving EM risk appetite, which often benefits correlated markets like Thailand via regional fund flows.'
    },
    {
        'id': 'INDONESIA_EQUITY_DOWN',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['INDONESIA'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Negative EM sentiment, risk-off pressure on Thai equities',
        'affected_asset': 'THAI_EQUITY',
        'confidence_base': 0.65,
        'reasoning': 'Sharp EM sell-offs can trigger regional contagion as investors reduce overall EM exposure, pressuring Thai markets.'
    },

    # UNITED KINGDOM (G7, FINANCIAL CENTER - GLOBAL RISK SENTIMENT)
    {
        'id': 'UK_EQUITY_UP',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['UK'],
            'sentiment_direction': 'positive'
        },
        'impact': 'Positive global risk sentiment, GBP strength potential',
        'affected_asset': 'GLOBAL_RISK_SENTIMENT',
        'confidence_base': 0.55,
        'reasoning': 'UK equity strength reflects global risk appetite. Strong GBP could modestly pressure USD (indirect THB support).'
    },
    {
        'id': 'UK_EQUITY_DOWN',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['UK'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Risk-off sentiment, safe-haven flows to USD',
        'affected_asset': 'GLOBAL_RISK_SENTIMENT',
        'confidence_base': 0.6,
        'reasoning': 'UK market weakness contributes to global risk-off, potentially boosting safe-haven USD (THB pressure).'
    },

    # EUROPE (G7 BLOC - GROWTH/TRADE IMPLICATIONS)
    {
        'id': 'EU_EQUITY_UP',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['EU'],
            'sentiment_direction': 'positive'
        },
        'impact': 'European growth optimism, EUR strength potential',
        'affected_asset': 'EUR/USD',
        'confidence_base': 0.5,
        'reasoning': 'Strong EU equities signal regional growth, supporting EUR which may modestly weaken USD (indirect THB support).'
    },
    {
        'id': 'EU_EQUITY_DOWN',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['EU'],
            'sentiment_direction': 'negative'
        },
        'impact': 'European growth concerns, risk-off sentiment',
        'affected_asset': 'GLOBAL_GROWTH_OUTLOOK',
        'confidence_base': 0.55,
        'reasoning': 'EU equity weakness indicates regional growth concerns, negative for global trade and risk sentiment.'
    },

    # ADDITIONAL KEY MARKETS:

    # JAPAN (G7, YEN CARRY TRADE IMPLICATIONS)
    {
        'id': 'JAPAN_EQUITY_UP',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['JAPAN'],
            'sentiment_direction': 'positive'
        },
        'impact': 'Risk-on sentiment, potential JPY weakness (carry trade)',
        'affected_asset': 'GLOBAL_RISK_SENTIMENT',
        'confidence_base': 0.5,
        'reasoning': 'Japanese equity strength often correlates with JPY weakness as carry trades increase, reflecting risk-on global conditions.'
    },
    {
        'id': 'JAPAN_EQUITY_DOWN',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['JAPAN'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Risk-off, potential JPY strength (carry unwind)',
        'affected_asset': 'GLOBAL_RISK_SENTIMENT',
        'confidence_base': 0.55,
        'reasoning': 'Japanese equity weakness may trigger JPY safe-haven flows as carry trades unwind, indicating global risk aversion.'
    },

    # CHINA (KEY TRADE PARTNER - DIRECT THAI IMPACT)
    {
        'id': 'CHINA_EQUITY_UP',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['CHINA'],
            'sentiment_direction': 'positive'
        },
        'impact': 'Positive Asian sentiment, supportive for Thai exports and equities',
        'affected_asset': 'THAI_EQUITY',
        'confidence_base': 0.7,
        'reasoning': 'Chinese equity strength directly boosts regional sentiment and demand outlook for Thai exports.'
    },
    {
        'id': 'CHINA_EQUITY_DOWN',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['CHINA'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Negative Asian sentiment, pressure on Thai exports and equities',
        'affected_asset': 'THAI_EQUITY',
        'confidence_base': 0.75,
        'reasoning': 'Chinese equity weakness directly pressures regional markets and Thai export demand given close trade links.'
    },

    # US EQUITY
    {
        'id': 'US_EQUITY_UP',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['USA'],  # Will capture "stocks" via default entity mapping
            'sentiment_direction': 'positive'
        },
        'impact': 'Risk-on sentiment, supports EM flows, potential USD mixed impact',
        'affected_asset': 'GLOBAL_RISK_SENTIMENT',
        'confidence_base': 0.65,
        'reasoning': 'US equity strength signals robust risk appetite, supportive for EM capital inflows. However, strong US growth may also support USD via rate expectations, creating mixed pressure on THB.'
    },
    {
        'id': 'US_EQUITY_DOWN',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['USA'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Risk-off sentiment, safe-haven USD demand, pressure on EM assets',
        'affected_asset': 'THB/USD',
        'confidence_base': 0.7,
        'reasoning': 'US equity weakness triggers global risk-off, boosting safe-haven USD demand and reducing capital flows to EM, pressuring THB.'
    },

    #CANADA EQUITY
    {
        'id': 'CANADIAN_EQUITY_UP',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['CANADA'],
            'sentiment_direction': 'positive'
        },
        'impact': 'Commodity-linked growth optimism, potential CAD strength',
        'affected_asset': 'GLOBAL_GROWTH_OUTLOOK',
        'confidence_base': 0.5,
        'reasoning': 'Canadian equity strength often reflects optimism about commodity demand (energy, metals), signaling global growth expectations. Strong CAD may modestly pressure USD.'
    },
    {
        'id': 'CANADIAN_EQUITY_DOWN',
        'conditions': {
            'required_topics': ['EQUITY_MARKET'],
            'required_entities': ['CANADA'],
            'sentiment_direction': 'negative'
        },
        'impact': 'Commodity demand concern, risk-off in resource sectors',
        'affected_asset': 'GLOBAL_GROWTH_OUTLOOK',
        'confidence_base': 0.55,
        'reasoning': 'Canadian equity weakness suggests pessimism about commodity demand and global growth, contributing to risk-off sentiment but with less direct EM impact than US moves.'
    },

    #==== SECTORS ====#

    # TECHNOLOGY
    {
        'id': 'TECH_UP',
        'conditions': {
            'required_topics': ['TECHNOLOGY'],
            'required_entities': [],  # Could be US, China, Taiwan, or global
            'sentiment_direction': 'positive'
        },
        'impact': 'Growth/innovation optimism, supports risk appetite, mixed FX impact',
        'affected_asset': 'GLOBAL_RISK_SENTIMENT',
        'confidence_base': 0.55,
        'reasoning': 'Technology sector strength signals growth and innovation optimism, supporting overall risk appetite. FX impact depends on which country/companies dominate the news.'
    },
    {
        'id': 'TECH_DOWN',
        'conditions': {
            'required_topics': ['TECHNOLOGY'],
            'required_entities': [],
            'sentiment_direction': 'negative'
        },
        'impact': 'Growth concern, sector-specific risk-off, potential pressure on tech-heavy indices',
        'affected_asset': 'GLOBAL_RISK_SENTIMENT',
        'confidence_base': 0.6,
        'reasoning': 'Technology sector weakness can indicate growth concerns or regulatory/competitive risks, contributing to risk-off sentiment, especially in tech-heavy markets like US/Nasdaq.'
    }


]
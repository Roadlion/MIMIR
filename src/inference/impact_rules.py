
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
    }
]
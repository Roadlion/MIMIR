TOPIC_KEYWORDS = {
    # MONETARY & POLICY
    'CENTRAL_BANK': ['powell', 'fed', 'central bank', 'ecb', 'boj', 'bank of england', 'bank of thailand', 'rbi', 'monetary policy', 'interest rate', 'rate decision', 'policy meeting', 'hawkish', 'dovish', 'tightening', 'easing', 'quantitative tightening', 'qt', 'qe', 'schlegel', 'snb', 'central bank'],
    'INFLATION': ['cpi', 'inflation', 'deflation', 'price pressure', 'price pressures', 'consumer price', 'ppi', 'wage growth', 'core inflation', 'hyperinflation', 'stagflation'],
    
    # FINANCIAL MARKETS
    'BOND_MARKET': ['bonds', 'bond', 'yield', 'treasury', 'gilts', 'jgb', 'auction', 'duration', 'spread', 'rating', 'moody\'s', 'fitch', 'default', 'treasuries', 'treasury'],
    'CURRENCY_MOVEMENT': ['currency', 'currencies', 'forex', 'fx', 'dollar', 'yen', 'euro', 'pound', 'yuan', 'baht', 'won', 'rupiah', 'ringgit', 'devaluation', 'appreciation', 'depreciation', 'debasement', 'usd'],
    'EQUITY_MARKET': ['stock', 'stocks', 'ipo', 'ipos', 'equity', 'share', 'shares', 's&p', 'ftse', 'nikkei', 'kospi', 'index', 'selloff', 'correction', 'bull', 'bear', 'nasdaq', 'wall street', 'market turmoil'],
    
    ### COMMODITIES ###
    
    # ENERGY
    'COMMODITY_ENERGY': [
        'oil', 'crude', 'brent', 'wti', 'petroleum', 'energy',
        'natural gas', 'ng', 'lng', 'gasoline', 'diesel', 'jet fuel',
        'opec', 'opec+', 'production cut', 'output cut', 'supply cut',
        'inventory', 'eia', 'storage', 'refinery', 'drilling', 'gas', 'coal'
    ],
    
    # PRECIOUS METALS
    'COMMODITY_PRECIOUS_METALS': [
        'gold', 'silver', 'platinum', 'palladium', 'precious metal',
        'bullion', 'safe haven', 'xau', 'xag', 'xpt', 'xpd'
    ],
    
    # INDUSTRIAL/BASE METALS
    'COMMODITY_BASE_METALS': [
        'copper', 'aluminum', 'aluminium', 'zinc', 'nickel', 'lead', 'tin',
        'iron ore', 'steel', 'base metal', 'industrial metal',
        'lme', 'london metal exchange', 'metal'
    ],
    
    # AGRICULTURE
    'COMMODITY_AGRICULTURE': [
        'wheat', 'corn', 'soybean', 'soy', 'rice', 'palm oil', 'coffee', 'cocoa', 'cotton', 'livestock', 'cattle',
        'agriculture', 'grain', 'crop', 'harvest', 'drought', 
    ],
    
    # SOFT COMMODITIES/BULK
    'COMMODITY_SOFT': [
        'rubber', 'lumber', 'timber', 'paper', 'pulp'
    ],
    
    # CRYPTO (Optional - if relevant)
    'COMMODITY_CRYPTO': [
        'bitcoin', 'crypto', 'ethereum', 'blockchain', 'digital asset'
    ],
    
    # MACROECONOMIC DATA
    'ECONOMIC_DATA': [
    # Core Growth/Output
    'gdp', 'growth', 'growing', 'economy', 'recession', 'slowdown', 'expansion', 'contraction', 
    'industrial production', 'pmi', 'manufacturing', 'services', 'output', 'output gap', 'grows',
    
    # Labor Market
    'unemployment', 'jobs', 'jobless', 'retail sales', 'consumer confidence', 'spending',
    
    # Trade & Supply Chain (Merged In)
    'exports', 'imports', 'trade deficit', 'trade surplus', 'balance of trade', 
    'tariff', 'trade war', 'trade agreement', 'supply chain', 'protectionism', 'wto',
    
    # Forecasting
    'economy forecast', 'economic outlook'
    ],
    
    # RISK & EVENTS
    'GEOPOLITICAL_RISK': ['war', 'tension', 'tensions', 'sanction', 'conflict', 'crisis', 'attack', 'retaliation', 'diplomacy', 'summit', 'election', 'vote', 'instability', 'coup'],
    
    # SECTOR SPECIFIC (Optional, for depth)
    'TECHNOLOGY': ['tech', 'semiconductor', 'chip', 'ai', 'software', 'hardware', 'big tech', 'memory'],
}

ENTITY_KEYWORDS = {
    # COUNTRIES (From your headlines + core)
    'USA': ['u.s.', 'united states', 'federal reserve', 'fed', 'washington', 'america', 'trump', 'dollar', 'usd', 'us', 's&p', 'nasdaq', 'wall street', 'chicago'],
    'CHINA': ['china', 'beijing', 'pboc', 'chinese', 'yuan', 'renminbi', 'evergrande', "china's"],
    'JAPAN': ['japan', 'boj', 'bank of japan', 'tokyo', 'yen', 'jpy', 'japanese'],
    'UK': ['u.k.', 'united kingdom', 'bank of england', 'london', 'pound', 'sterling', 'gbp', 'ftse', 'uk'],
    'EU': ['european union', 'european', 'ecb', "ecb's", 'eurozone', 'frankfurt', 'europe', 'brussels', 'euro', "eu", 'hungary', "hungary's", 'hungarian', 'forint', 'spain', "spain's", 'spanish', 'italy', "italy's", 'italian', 'greece', "greece's", 'greek', 'germany', "germany's", 'german', 'adidas', 'france', 'paris', 'french', 'czech republic', "czech republic's", 'czech', 'czechia', 'poland', "poland's", 'polish', 'zloty'],
    'THAILAND': ['thailand', 'bangkok', 'bank of thailand', 'thai', 'baht'],
    'SWITZERLAND': ['swiss', 'switzerland', 'swiss franc'],
    'INDIA': ['india', 'new delhi', 'mumbai', 'rupee', 'indian', 'inr', 'usd/inr', 'rbi'],
    'SOUTH_KOREA': ['south korea', 'korea', 'seoul', 'bank of korea', 'won', 'kospi', 'south korean'],
    'INDONESIA': ['indonesia', 'jakarta', 'rupiah', 'idx', 'indonesian'],
    'TAIWAN': ['taiwan', 'taipei', 'taiwan dollar', 'tsmc'],
    'SINGAPORE': ['singapore', 'sgx', 'singapore dollar'],
    'AUSTRALIA': ['australia', 'australian', 'aud'],
    'SOUTH_AFRICA': ['south africa', 'sarb', 'rand', 'johannesburg', 's. africa', "s. africa's"],
    'RUSSIA': ['russia', 'moscow', 'kremlin', 'ruble'],
    'TURKEY': ['turkey', 'turkish', 'istanbul', 'lira'],
    'KENYA': ['kenya', 'nairobі', 'shilling', 'kenyan'],
    'FRANCE': ['france', 'paris', 'french', 'cac'],
    'VIETNAM': ['vietnam', 'vnd', 'dong'],
    'UKRAINE': ['ukraine', "ukraine's", 'ukrainian'],
    'SWEDEN': ['sweden', "sweden's", 'swedish', 'nok'],
    'MALAYSIA': ['malaysia', "malaysia's", 'malaysian', 'myr'],
    'GREECE': ['greece', "greece's", 'greek'],
    'CANADA': ['canada', "canada's", 'canadian'],
    'ITALY': ['italy', "italy's", 'italian'],
    'CZECH REPUBLIC': ['czech republic', "czech republic's", 'czech', 'czechia'],
    'POLAND': ['poland', "poland's", 'polish', 'zloty'],
    'HUNGARY': ['hungary', "hungary's", 'hungarian', 'forint'],
    'SPAIN': ['spain', "spain's", 'spanish'],
    'GERMANY': ['germany', "germany's", 'german', 'adidas'],
    
    # REGIONS (For multi-country or regional headlines)
    'ASIA': ['asia', 'asian', 'pacific'],
    'MIDDLE_EAST': ['middle east', 'gulf', 'iran', 'israel', 'saudi arabia', 'qatar', 'uae', 'dubai', 'tehran', 'gaza', 'saudi'],
    'EMERGING_MARKETS': ['emerging market', 'em', 'frontier', 'emerging markets', 'emerging'],
    
    # INSTITUTIONS (Standalone entity tags)
    'FEDERAL_RESERVE': ['federal reserve', 'fed'],
    'ECB': ['european central bank', 'ecb'],
    'BOJ': ['bank of japan', 'boj'],
    'BANK_OF_ENGLAND': ['bank of england', 'boe'],
    
    # CURRENCIES (Act as strong proxies)
    'USD': ['dollar', 'usd', 'greenback', 'eur/usd'],
    'JPY': ['yen', 'jpy', 'japanese yen'],
    'EUR': ['euro', 'eur', 'eur/usd'],
    'GBP': ['pound', 'gbp', 'sterling'],
    'CNY': ['yuan', 'renminbi', 'cny'],
}

DEFAULT_ENTITY_MAP = {
    'EQUITY_MARKET': 'USA',          # "stocks slip"
    'BOND_MARKET': 'USA',            # "treasuries fall"
    'CENTRAL_BANK': 'USA',           # "fed officials signal"
}
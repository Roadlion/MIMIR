TOPIC_KEYWORDS = {
    # MONETARY & POLICY
    'CENTRAL_BANK': ['powell', 'fed', 'central bank', 'ecb', 'boj', 'bank of england', 'bank of thailand', 'rbi', 'monetary policy', 'interest rate', 'rate decision', 'policy meeting', 'hawkish', 'dovish', 'tightening', 'easing', 'quantitative tightening', 'qt', 'qe', 'schlegel', 'snb'],
    'INFLATION': ['cpi', 'inflation', 'deflation', 'price pressure', 'price pressures', 'consumer price', 'ppi', 'wage growth', 'core inflation', 'hyperinflation', 'stagflation'],
    
    # FINANCIAL MARKETS
    'BOND_MARKET': ['bonds', 'bond', 'yield', 'treasury', 'gilts', 'jgb', 'debt', 'auction', 'duration', 'spread', 'rating', 'moody\'s', 'fitch', 'credit', 'default', 'treasuries', 'treasury'],
    'CURRENCY_MOVEMENT': ['currency', 'currencies', 'forex', 'fx', 'dollar', 'yen', 'euro', 'pound', 'yuan', 'baht', 'won', 'rupiah', 'ringgit', 'devaluation', 'appreciation', 'depreciation', 'debasement'],
    'EQUITY_MARKET': ['stock', 'stocks', 'ipo', 'ipos', 'equity', 'share', 'shares', 's&p', 'ftse', 'nikkei', 'kospi', 'index', 'selloff', 'correction', 'bull', 'bear', 'nasdaq'],
    
    ### COMMODITIES ###
    
    # ENERGY
    'COMMODITY_ENERGY': [
        'oil', 'crude', 'brent', 'wti', 'petroleum', 'energy',
        'natural gas', 'ng', 'lng', 'gasoline', 'diesel', 'jet fuel',
        'opec', 'opec+', 'production cut', 'output cut', 'supply cut',
        'inventory', 'eia', 'storage', 'refinery', 'drilling'
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
    'ECONOMIC_DATA': ['gdp', 'growth', 'recession', 'slowdown', 'expansion', 'contraction', 'unemployment', 'jobs', 'retail sales', 'industrial production', 'pmi', 'manufacturing', 'services', 'consumer confidence', 'spending', 'output gap', 'grow', 'economy forecast'],
    'TRADE': ['tariff', 'trade war', 'exports', 'imports', 'trade deficit', 'trade surplus', 'balance of trade', 'supply chain', 'protectionism', 'wto', 'trade deficits', 'trade agreement'],
    
    # RISK & EVENTS
    'GEOPOLITICAL_RISK': ['war', 'tension', 'tensions', 'sanction', 'conflict', 'crisis', 'attack', 'strike', 'retaliation', 'diplomacy', 'summit', 'election', 'vote', 'turmoil', 'instability', 'coup'],
    'SOVEREIGN_RISK': ['default', 'debt crisis', 'debt ceiling', 'bailout', 'imf', 'world bank', 'austerity', 'fiscal cliff'],
    
    # CORPORATE
    'CORPORATE_EARNINGS': ['earnings', 'profit', 'revenue', 'loss', 'quarterly', 'results', 'outlook', 'guidance', 'dividend', 'buyback'],
    'MERGERS_ACQUISITIONS': ['merger', 'acquisition', 'm&a', 'takeover', 'bid', 'deal'],
    
    # SECTOR SPECIFIC (Optional, for depth)
    'TECHNOLOGY': ['tech', 'semiconductor', 'chip', 'ai', 'software', 'hardware', 'big tech', 'memory'],
    'FINANCIAL_SERVICES': ['bank', 'lender', 'insurer', 'credit', 'loan', 'leverage', 'etf', 'ipo', 'windfall'],
}

ENTITY_KEYWORDS = {
    # COUNTRIES (From your headlines + core)
    'USA': ['u.s.', 'united states', 'federal reserve', 'fed', 'washington', 'america', 'trump', 'dollar', 'usd', 'us', 's&p', 'nasdaq', 'wall street'],
    'CHINA': ['china', 'beijing', 'pboc', 'chinese', 'yuan', 'renminbi', 'evergrande', "china's"],
    'JAPAN': ['japan', 'boj', 'bank of japan', 'tokyo', 'yen', 'jpy', 'japanese'],
    'UK': ['u.k.', 'united kingdom', 'bank of england', 'london', 'pound', 'sterling', 'gbp', 'ftse', 'uk'],
    'EU': ['european union', 'european', 'ecb', "ecb's", 'eurozone', 'frankfurt', 'europe', 'brussels', 'euro', "eu"],
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
    'FRANCE': ['france', 'paris', 'french', 'euro', 'cac'],
    'VIETNAM': ['vietnam', 'vnd', 'dong'],
    'UKRAINE': ['ukraine', "ukraine's", 'ukrainian'],
    'SWEDEN': ['sweden', "sweden's", 'swedish', 'nok'],
    'MALAYSIA': ['malaysia', "mmalaysia's", 'malaysian', 'myr'],
    'GREECE': ['greece', "greece's", 'greek'],
    'CANADA': ['canda', "canada's", 'canadian'],
    
    # REGIONS (For multi-country or regional headlines)
    'ASIA': ['asia', 'asian', 'pacific'],
    'MIDDLE_EAST': ['middle east', 'gulf', 'iran', 'israel', 'saudi arabia', 'qatar', 'uae', 'dubai', 'tehran', 'gaza'],
    'EMERGING_MARKETS': ['emerging market', 'em', 'frontier', 'emerging markets'],
    
    # INSTITUTIONS (Standalone entity tags)
    'FEDERAL_RESERVE': ['federal reserve', 'fed'],
    'ECB': ['european central bank', 'ecb'],
    'BOJ': ['bank of japan', 'boj'],
    'BANK_OF_ENGLAND': ['bank of england', 'boe'],
    
    # CURRENCIES (Act as strong proxies)
    'USD': ['dollar', 'usd', 'greenback'],
    'JPY': ['yen', 'jpy', 'japanese yen'],
    'EUR': ['euro', 'eur'],
    'GBP': ['pound', 'gbp', 'sterling'],
    'CNY': ['yuan', 'renminbi', 'cny'],
}
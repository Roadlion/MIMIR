import string

def normalize_word(word):
    """Remove possessive 's and other common suffixes from a word."""
    # Remove trailing 's or ' (handles "ECB's", "China's")
    if word.endswith("'s"):
        word = word[:-2]
    elif word.endswith("’s"):  # Different apostrophe character
        word = word[:-2]
    elif word.endswith("'"):
        word = word[:-1]
    elif word.endswith("’"):
        word = word[:-1]
    return word

def get_words(text):
        # Remove punctuation, split into words
        translator = str.maketrans('', '', string.punctuation)
        words = text.lower().translate(translator).split()
        normalized_words = [normalize_word(w) for w in words]
        return set(normalized_words)  # Using set for O(1) lookup

#Entity Auto Tagger
def auto_tag_entity(headline: str):
    import re
    from keywords import ENTITY_KEYWORDS

    lower_headline = headline.lower()
    new_headline = re.sub(r"[,:!;]", "", lower_headline)
    headline_words = get_words(new_headline)

    entities_found = []

    for entity in ENTITY_KEYWORDS:
        for i in ENTITY_KEYWORDS[entity]:
            if i in headline_words:
                if entity not in entities_found:
                    entities_found.append(entity)
    return entities_found

#Topic Auto Tagger
def auto_tag_topic(headline: str):
    import re
    from keywords import TOPIC_KEYWORDS

    lower_headline = headline.lower()
    new_headline = re.sub(r"[,:!;]", "", lower_headline)
    headline_words = get_words(new_headline)

    topics_found = []

    for topic in TOPIC_KEYWORDS:
        for i in TOPIC_KEYWORDS[topic]:
            if i in headline_words:
                if topic not in topics_found:
                    topics_found.append(topic)
        
    return topics_found

def apply_default_entities(topics, entities):
    from keywords import DEFAULT_ENTITY_MAP
    if not entities:  # No country detected
        for topic in topics:
            if topic in DEFAULT_ENTITY_MAP:
                entities.append(DEFAULT_ENTITY_MAP[topic])
                break  # Add only one default
    return entities
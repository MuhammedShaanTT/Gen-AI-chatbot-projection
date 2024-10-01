import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def analyze_input(user_input):
    doc = nlp(user_input)
    analysis = {
        'tokens': [token.text for token in doc],
        'lemmas': [token.lemma_ for token in doc],
        'parts_of_speech': [token.pos_ for token in doc]
    }
    return analysis

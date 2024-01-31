import spacy

# Load the spaCy model for Named Entity Recognition
nlp = spacy.load("en_core_web_sm")

def perform_ner(text):
    # Process the text using spaCy NLP pipeline
    doc = nlp(text)

    # Extract named entities
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    return entities

# Example usage:
text = "Apple Inc. is planning to open a new store in Paris in 2022."
named_entities = perform_ner(text)

print("Named Entities:")
for entity, label in named_entities:
    print(f"{entity}: {label}")

import nltk

# Uncomment the line below to download the NLTK resource
# nltk.download('averaged_perceptron_tagger')

def pos_tagging_nltk(text):
    # Tokenize the text into words
    words = nltk.word_tokenize(text)

    # Perform part-of-speech tagging
    pos_tags = nltk.pos_tag(words)

    return pos_tags

# Example usage:
text = "The quick brown fox jumps over the lazy dog."

# Uncomment the line below if you haven't downloaded the NLTK resource yet
# nltk.download('averaged_perceptron_tagger')

tagged_result = pos_tagging_nltk(text)

print("Tagged Result:")
for word, pos_tag in tagged_result:
    print(f"{word}: {pos_tag}")

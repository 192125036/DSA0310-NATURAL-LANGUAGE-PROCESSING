import nltk
from nltk.stem import PorterStemmer

# Download the Porter Stemmer data (only need to do this once)
nltk.download('punkt')

def perform_stemming(words):
    porter = PorterStemmer()
    stemmed_words = [porter.stem(word) for word in words]
    return stemmed_words

# Example usage:
input_words = ["running", "flies", "jumps", "happily", "better"]
stemmed_words = perform_stemming(input_words)

print("Original words:", input_words)
print("Stemmed words:", stemmed_words)

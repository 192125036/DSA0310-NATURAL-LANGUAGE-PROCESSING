import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet

nltk.download('punkt')
nltk.download('wordnet')

def morphological_analysis(text):
    # Tokenization
    words = word_tokenize(text)
    print("Tokenized words:", words)

    # Stemming using Porter Stemmer
    porter_stemmer = PorterStemmer()
    stemmed_words = [porter_stemmer.stem(word) for word in words]
    print("Stemmed words:", stemmed_words)

    # Lemmatization using WordNet Lemmatizer
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word, get_wordnet_pos(word)) for word in words]
    print("Lemmatized words:", lemmatized_words)

def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"N": wordnet.NOUN, "V": wordnet.VERB, "R": wordnet.ADV, "J": wordnet.ADJ}
    return tag_dict.get(tag, wordnet.NOUN)

# Example text
text_to_analyze = "The quick brown foxes are jumping over the lazy dogs."

# Perform morphological analysis
morphological_analysis(text_to_analyze)

import random
from collections import defaultdict

class BigramModel:
    def __init__(self):
        self.bigram_counts = defaultdict(lambda: defaultdict(int))
        self.start_tokens = []

    def train(self, corpus):
        for sentence in corpus:
            tokens = sentence.split()
            self.start_tokens.append(tokens[0])

            for i in range(len(tokens) - 1):
                current_word, next_word = tokens[i], tokens[i + 1]
                self.bigram_counts[current_word][next_word] += 1

    def generate_text(self, max_length=20):
        current_word = random.choice(self.start_tokens)
        generated_text = [current_word]

        while len(generated_text) < max_length:
            next_word = self.select_next_word(current_word)
            if next_word is None:
                break
            generated_text.append(next_word)
            current_word = next_word

        return ' '.join(generated_text)

    def select_next_word(self, current_word):
        possible_next_words = list(self.bigram_counts[current_word].keys())
        if not possible_next_words:
            return None

        probabilities = [self.bigram_counts[current_word][word] for word in possible_next_words]
        next_word = random.choices(possible_next_words, weights=probabilities)[0]

        return next_word

# Example usage:
corpus = [
    "This is a sample sentence.",
    "A sample sentence is here.",
    "Another example is given."
]

bigram_model = BigramModel()
bigram_model.train(corpus)

generated_text = bigram_model.generate_text()
print("Generated Text:")
print(generated_text)

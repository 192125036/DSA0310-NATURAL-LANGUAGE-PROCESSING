import nltk

# Define a Probabilistic Context-Free Grammar (PCFG)
pcfg_grammar = nltk.PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.5] | 'John' [0.2] | 'Mary' [0.3]
    VP -> V NP [0.7] | 'loves' [0.3]
    Det -> 'the' [0.6] | 'a' [0.4]
    N -> 'man' [0.5] | 'woman' [0.5]
    V -> 'saw' [0.4] | 'walked' [0.6]
""")

# Define a probabilistic parser using the PCFG
parser = nltk.ViterbiParser(pcfg_grammar)

# Example sentence
sentence = "the man saw John"

# Tokenize the sentence
tokens = sentence.split()

# Parse the sentence using the probabilistic parser
parses = list(parser.parse(tokens))

# Print the most likely parse tree
if parses:
    most_likely_parse = parses[0]
    most_likely_parse.pretty_print()
else:
    print("Parsing failed.")

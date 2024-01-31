import nltk
from nltk import Tree

def generate_parse_tree(grammar, sentence):
    parser = nltk.ChartParser(grammar)
    parses = list(parser.parse(sentence.split()))

    if len(parses) > 0:
        return parses[0]
    else:
        return None

# Example usage:
cfg = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N | NP PP
    VP -> V NP | VP PP
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat'
    V -> 'chased' | 'ate'
    P -> 'with' | 'in'
""")

sentence = "the dog chased the cat with a stick"
parse_tree = generate_parse_tree(cfg, sentence)

if parse_tree:
    parse_tree.pretty_print()
else:
    print("Parsing failed.")

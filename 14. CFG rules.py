import nltk

def check_agreement(grammar, sentence):
    parser = nltk.ChartParser(grammar)
    parses = list(parser.parse(sentence.split()))

    if len(parses) > 0:
        print("Parsing successful!")
        for tree in parses:
            check_agreement_tree(tree)
    else:
        print("Parsing failed.")

def check_agreement_tree(tree):
    subject = None
    verb = None

    for subtree in tree.subtrees():
        if subtree.label() == 'NP':
            subject = subtree.leaves()[-1]
        elif subtree.label() == 'VP':
            verb = subtree.leaves()[0]

    if subject and verb:
        if subject.endswith('s') and not verb.endswith('s'):
            print(f"Agreement Error: Plural subject '{subject}' does not agree with singular verb '{verb}'.")
        elif not subject.endswith('s') and verb.endswith('s'):
            print(f"Agreement Error: Singular subject '{subject}' does not agree with plural verb '{verb}'.")
        else:
            print("Agreement is correct.")
    else:
        print("Unable to determine agreement.")

# Example usage:
agreement_grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> 'the' 'dog' | 'the' 'dogs'
    VP -> 'chases' | 'chase'
""")

sentence1 = "the dog chases"
sentence2 = "the dogs chase"

print("Checking Agreement for Sentence 1:")
check_agreement(agreement_grammar, sentence1)

print("\nChecking Agreement for Sentence 2:")
check_agreement(agreement_grammar, sentence2)

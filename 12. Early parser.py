class EarleyParser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.chart = []

    def parse(self, sentence):
        self.chart = [set() for _ in range(len(sentence) + 1)]
        self.predict(0, 'S', 0)
        self.chart_scan(sentence)
        self.chart_complete()

        # Check if the sentence is accepted
        accepted = any(item.rule == ('S', ('NP', 'VP')) and item.start == 0 and item.end == len(sentence) for item in self.chart[-1])

        if accepted:
            print("Parsing successful!")
        else:
            print("Parsing failed!")

    def predict(self, index, non_terminal, dot):
        for production in self.grammar[non_terminal]:
            self.chart[index].add(Item(non_terminal, production, dot, index))

    def chart_scan(self, sentence):
        for i in range(len(sentence) + 1):
            for item in self.chart[i]:
                if not item.is_complete() and item.next_symbol() == sentence[i:i+1]:
                    self.chart[i+1].add(item.advance())

    def chart_complete(self):
        changed = True
        while changed:
            changed = False
            for i in range(len(self.chart)):
                for item in list(self.chart[i]):
                    if item.is_complete():
                        self.chart_complete_item(item, i)
                        changed = True

    def chart_complete_item(self, item, index):
        for predecessor in self.chart[item.start]:
            if not predecessor.is_complete() and predecessor.next_symbol() == item.rule[0]:
                self.chart[index].add(predecessor.advance())

class Item:
    def __init__(self, lhs, rhs, dot, start):
        self.lhs = lhs
        self.rhs = rhs
        self.dot = dot
        self.start = start

    def __repr__(self):
        return f'{self.lhs} -> {" ".join(self.rhs[:self.dot] + ["●"] + self.rhs[self.dot:])} [{self.start}]'

    def is_complete(self):
        return self.dot == len(self.rhs)

    def next_symbol(self):
        return self.rhs[self.dot]

    def advance(self):
        return Item(self.lhs, self.rhs, self.dot + 1, self.start)


# Example usage:
grammar = {
    'S': [('NP', 'VP')],
    'NP': [('Det', 'N'), ('NP', 'PP')],
    'VP': [('V', 'NP'), ('VP', 'PP')],
    'PP': [('P', 'NP')],
    'Det': ['the', 'a'],
    'N': ['dog', 'cat'],
    'V': ['chased', 'ate'],
    'P': ['with', 'in']
}

earley_parser = EarleyParser(grammar)
sentence = "the dog chased the cat with a stick"
earley_parser.parse(sentence)

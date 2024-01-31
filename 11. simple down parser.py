class SimpleParser:
    def __init__(self):
        self.tokens = []
        self.current_token = 0

    def parse(self, sentence):
        self.tokens = sentence.split()
        self.current_token = 0

        if self.parse_sentence():
            print("Parsing successful!")
        else:
            print("Parsing failed!")

    def match(self, expected):
        if self.current_token < len(self.tokens) and self.tokens[self.current_token] == expected:
            self.current_token += 1
            return True
        return False

    def parse_sentence(self):
        return self.parse_subject() and self.parse_verb() and self.parse_object()

    def parse_subject(self):
        return self.match("The")

    def parse_verb(self):
        return self.match("quick")

    def parse_object(self):
        return self.match("fox") or self.match("dog")

# Example usage:
parser = SimpleParser()

sentence1 = "The quick fox"
parser.parse(sentence1)

sentence2 = "The quick dog"
parser.parse(sentence2)

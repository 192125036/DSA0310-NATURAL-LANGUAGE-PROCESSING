class PluralStateMachine:
    def __init__(self):
        self.state = 'start'
        self.transitions = {
            'start': {'consonant': 'add_s', 'vowel': 'add_s', 'y': 'change_y_to_ies'},
            'add_s': {'': 'final'},
            'change_y_to_ies': {'': 'final'}
        }

    def parse_word(self, word):
        for char in word:
            category = self.get_char_category(char)
            if category in self.transitions[self.state]:
                action = self.transitions[self.state][category]
                getattr(self, action)()
            else:
                raise ValueError(f"Invalid transition from state {self.state} with character {char}")

        return self.state == 'final'

    def get_char_category(self, char):
        vowels = 'aeiou'
        if char.lower() in vowels:
            return 'vowel'
        elif char.lower() == 'y':
            return 'y'
        else:
            return 'consonant'

    def add_s(self):
        print("Adding 's' to the word.")
        self.state = 'final'

    def change_y_to_ies(self):
        print("Changing 'y' to 'ies' in the word.")
        self.state = 'final'


# Example usage:
word_to_pluralize = input("Enter a singular noun: ")
plural_fsm = PluralStateMachine()

if plural_fsm.parse_word(word_to_pluralize):
    print(f"The plural form is: {word_to_pluralize}")
else:
    print("Invalid input for pluralization.")

class StateAutomaton:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2'}
        self.accept_state = 'q2'
        self.current_state = 'q0'

    def transition(self, char):
        if self.current_state == 'q0' and char == 'a':
            self.current_state = 'q1'
        elif self.current_state == 'q1' and char == 'b':
            self.current_state = 'q2'
        else:
            self.current_state = 'q0'

    def is_accepting(self):
        return self.current_state == self.accept_state


def match_pattern(input_str):
    automaton = StateAutomaton()

    for char in input_str:
        automaton.transition(char)

    return automaton.is_accepting()


# Test the finite state automaton with some examples
test_strings = ['ab', 'abc', 'xyzab', 'defab', 'abab']

for test_str in test_strings:
    result = match_pattern(test_str)
    print(f'The string "{test_str}" ends with "ab": {result}')

from configuration import Configuration

class TuringMachine:
    def __init__(self, states, alphabet, tape_symbols, blank, transitions, initial_state, accept_states, reject_states):
        self.states = set(states)
        self.alphabet = set(alphabet)
        self.tape_symbols = set(tape_symbols)
        self.transitions = transitions
        self.initial_state = initial_state
        self.accept_states = set(accept_states) ##list
        self.reject_states = set(reject_states) ##list
        self.blank = blank

    def run_step(self, configuration):
        # Check if the current state is an accepting or rejecting state
        tape=configuration.tape
        current_state=configuration.state
        head_position=configuration.head_position
        if configuration.state in self.accept_states or configuration.state in self.reject_states:
            return configuration

        # Retrieve the current symbol under the tape head
        current_symbol = tape[configuration.head_position] if 0 <= configuration.head_position < len(tape) else '_'
        if(current_symbol not in self.tape_symbols):
            raise Exception("error on input: tape contains symbol not in tape alphabet.")
            ##return tape, -1, current_state # return head_position as -1
        # Check if a transition is defined for the current state and symbol
        if (configuration.state, current_symbol) in self.transitions:
            new_state, write_symbol, move_direction = self.transitions[(current_state, current_symbol)]

            # Write the new symbol to the tape
            if 0 <= head_position < len(tape):
                tape[head_position] = write_symbol
            elif move_direction == 'R':
                tape.append(write_symbol)
            elif move_direction == 'L': ## why insert at -1?, the head is in the end it cant be lower than 0
                tape.insert(0, write_symbol)

            # Move the tape head according to the direction specified in the transition
            if move_direction == 'R':
                head_position += 1
                if head_position == len(tape):
                        tape.append(self.blank)  # Blank symbol for extending the tape to the right
            elif move_direction == 'L':
                head_position -= 1
                if head_position < 0: ##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ this isn't illegal? if the head is on 0 and the transition says to move left this means the turing machine is incorrect isn't it?
                        tape.insert(0, self.blank)  # Blank symbol for extending the tape to the left

            return Configuration(tape, head_position, new_state)
        else:
            # If no transition is defined, stay in the current state
            return configuration

    def contains_chars(self, input_string, input_alphabet):
        for ch in input_string:
            if(ch not in input_alphabet):
                return False
        return True

    def run(self, input_string):
        max_steps=100*len(input_string)
        tape = list(input_string)
        head_position = 0
        current_state = self.initial_state
        steps = 0

        if not self.contains_chars(input_string, self.alphabet):
            raise Exception("input string contains char not from the alphabet.")
            return Configuration(''.join(tape), head_position,current_state in self.accept_states) ## @@@@ current_state in self.accept_states why boolean it should be state?


        while current_state not in self.accept_states and current_state not in self.reject_states and steps < max_steps:
            current_symbol = tape[head_position]

            if(current_symbol not in self.tape_symbols):
                raise Exception("error on input: tape contains symbol not in tape alphabet.")
                return tape, -1, current_state # return head_position as -1

            if (current_state, current_symbol) in self.transitions:
                new_state, new_symbol, move_direction = self.transitions[(current_state, current_symbol)]

                tape[head_position] = new_symbol

                if move_direction == 'R':
                    head_position += 1
                    if head_position == len(tape):
                        tape.append(self.blank)  # Blank symbol for extending the tape to the right
                elif move_direction == 'L':
                    head_position -= 1
                    if head_position < 0: ##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ this isn't illegal? if the head is on 0 and the transition says to move left this means the turing machine is incorrect isn't it?
                        tape.insert(0, self.blank)  # Blank symbol for extending the tape to the left

                current_state = new_state
                steps += 1
            else:
                break

        return ''.join(tape), current_state in self.accept_states

    def run_combined(self, input_string,head_position): ##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ head=0?
          max_steps=100*len(input_string)
          tape = list(input_string)
          #head_position = 0
          current_state = self.initial_state
          steps = 0

          while current_state not in self.accept_states and current_state not in self.reject_states and steps < max_steps:
              current_symbol = tape[head_position]

              if (current_state, current_symbol) in self.transitions:
                  new_state, new_symbol, move_direction = self.transitions[(current_state, current_symbol)]

                  tape[head_position] = new_symbol

                  if move_direction == 'R':
                      head_position += 1
                      if head_position == len(tape):
                          tape.append(self.blank)  # Blank symbol for extending the tape to the right
                  elif move_direction == 'L':
                      head_position -= 1
                      if head_position < 0:
                          tape.insert(0, self.blank)  # Blank symbol for extending the tape to the left

                  current_state = new_state
                  steps += 1
              else:
                  break

          #return ''.join(tape), current_state in self.accept_states, head_position
          return ''.join(tape), current_state, head_position


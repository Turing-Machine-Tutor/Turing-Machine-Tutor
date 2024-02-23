from Tape import Tape
from configuration import Configuration
from machine_run_state import Machine_Run_State




class TuringMachine:
    def __init__(self, states, alphabet, tape_symbols, blank, transitions, initial_state, accept_states, reject_states):
        self.states = set(states)
        self.input_alphabet = set(alphabet)
        self.tape_alphabet = set(tape_symbols)
        self.transitions = transitions
        self.initial_state = initial_state
        self.accept_states = set(accept_states) ##list
        self.reject_states = set(reject_states) ##list
        self.blank = blank
        self.current_machine_state=Machine_Run_State(Tape(list()),0,initial_state)

    def run_step(self, configuration):
        # Check if the current state is an accepting or rejecting state

        tape=self.current_machine_state.tape
        current_state=self.current_machine_state
        head_position=self.current_machine_state.head_position
        if current_state in self.accept_states or current_state in self.reject_states:
            return self.current_machine_state

        # Retrieve the current symbol under the tape head
        current_symbol = tape[head_position] if 0 <= head_position < len(tape) else '_'
        if(current_symbol not in self.tape_alphabet):
            raise Exception("error on input: tape contains symbol not in tape alphabet.")
            ##return tape, -1, current_state # return head_position as -1
        # Check if a transition is defined for the current state and symbol
        if (self.current_machine_state.state, current_symbol) in self.transitions:
            new_config = self.transitions[(current_state, current_symbol)]
            # Write the new symbol to the tape +  Move the tape head according to the direction specified in the transition
            self.current_machine_state.write_to_tape(new_config)
        return self.current_machine_state
            # If no transition is defined, stay in the current state and return it


    def contains_chars(self, input_string, input_alphabet):
        for ch in input_string:
            if(ch not in input_alphabet):
                return False
        return True

    def reset_turing_machine(self):
        self.current_machine_state.tape = list()
        self.current_machine_state.head_position = 0
        self.current_machine_state.current_state = self.initial_state

    def run(self, input_string):
        max_steps=100*len(input_string)
        self.reset_turing_machine()
        steps = 0

        if not self.contains_chars(input_string, self.alphabet):
            raise Exception("input string contains char not from the alphabet.")
            ##return Configuration(''.join(tape), head_position,current_state in self.accept_states) ## @@@@ current_state in self.accept_states why boolean it should be state?


        while self.current_machine_state.current_state not in self.accept_states and self.current_machine_state.current_state not in self.reject_states and steps < max_steps:
            current_symbol = self.current_machine_state.tape[self.current_machine_state.head_position]
            if(current_symbol not in self.tape_symbols):
                raise Exception("error on input: tape contains symbol not in tape alphabet.")
                ##return tape, -1, current_state # return head_position as -1
            if (self.current_machine_state.current_state, current_symbol) in self.transitions:
                current_config=self.transitions[(self.current_machine_state.current_state, current_symbol)]
                self.current_machine_state.write_to_tape(current_config)
                steps += 1
            else:
                break

        final_machine_run_state=Machine_Run_State(self.current_machine_state.tape,self.current_machine_state.head_position,self.current_machine_state.state)
        self.reset_turing_machine()
        return final_machine_run_state


    def given_state_is_in_acceptance(self,state):
        return state in self.accept_states

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


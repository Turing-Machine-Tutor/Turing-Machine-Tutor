# from Tape import Tape
from machine_run_state import Machine_Run_State




class TuringMachine:
    def __init__(self, states, input_alphabet, tape_symbols, blank, transitions, initial_state, accept_states, reject_states):
        self.states = set(states)
        self.input_alphabet = set(input_alphabet)
        self.tape_alphabet = set(tape_symbols)
        self.transitions = transitions
        self.initial_state = initial_state
        self.accept_states = set(accept_states) ##list
        self.reject_states = set(reject_states) ##list
        self.blank = blank
        self.current_machine_state=Machine_Run_State(list(),0,initial_state)

    def run_step(self, configuration):
        self.current_machine_state.execute_config(configuration)
        new_machine_run_state = Machine_Run_State(self.current_machine_state.tape.copy(),
                                                self.current_machine_state.head_position,
                                                self.current_machine_state.state)
        return new_machine_run_state


    def contains_chars(self, input_string):
        for ch in input_string:
            if(ch not in self.input_alphabet):
                return False
        return True

    def get_config(self):
        symbol = self.current_machine_state.tape[self.current_machine_state.head_position]
        state=self.current_machine_state.state
        config = self.transitions[(state,symbol)]
        return config


    def reset_turing_machine(self):
        self.current_machine_state.tape = list()
        self.current_machine_state.head_position = 0
        self.current_machine_state.state = self.initial_state

    def run(self, input_string,head_position=0):
        max_steps=100*len(input_string)
       # self.reset_turing_machine()
        self.current_machine_state.put_word_on_tape(input_string)
        self.current_machine_state.head_position= head_position
        steps = 0

        if not self.contains_chars(input_string):
            raise Exception("input string contains char not from the alphabet.")
            ##return Configuration(''.join(tape), head_position,current_state in self.accept_states) ## @@@@ current_state in self.accept_states why boolean it should be state?


        while self.current_machine_state.state not in self.accept_states and self.current_machine_state.state not in self.reject_states and steps < max_steps:
            current_symbol = self.current_machine_state.tape[self.current_machine_state.head_position]
            if(current_symbol not in self.tape_alphabet):
                raise Exception("error on input: tape contains symbol not in tape alphabet.")
                ##return tape, -1, current_state # return head_position as -1
            if (self.current_machine_state.state, current_symbol) in self.transitions:
                current_config=self.transitions[(self.current_machine_state.state, current_symbol)]
                ##self.current_machine_state.write_to_tape(current_config)
                self.current_machine_state.execute_config(current_config)
                steps += 1
            else:
                break

        final_machine_run_state=Machine_Run_State(self.current_machine_state.tape,self.current_machine_state.head_position,self.current_machine_state.state)
        self.reset_turing_machine()
        return final_machine_run_state


    def given_state_is_in_acceptance(self,state):
        return state in self.accept_states

    # def run_combined(self, input_string,head_position): ##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ head=0?
    #       max_steps=100*len(input_string)
    #       self.reset_turing_machine()
    #       self.current_machine_state.head_position=head_position
    #       self.current_machine_state.put_word_on_tape(input_string)
    #       steps = 0
    #
    #       while self.current_machine_state.state not in self.accept_states and self.current_machine_state.state not in self.reject_states and steps < max_steps:
    #           current_symbol = self.current_machine_state.tape[head_position]
    #
    #           if (self.current_machine_state.state, current_symbol) in self.transitions:
    #               current_config=self.transitions[(self.current_machine_state.state, current_symbol)]
    #
    #               self.current_machine_state.execute_config(current_config)
    #               steps += 1
    #           else:
    #               break
    #
    #       final_machine_run_state = Machine_Run_State(self.current_machine_state.tape,
    #                                                   self.current_machine_state.head_position,
    #                                                   self.current_machine_state.state)
    #
    #       return final_machine_run_state
    #       #return ''.join(tape), current_state in self.accept_states, head_position
    #      ## return ''.join(tape), current_state, head_position







import time
from IPython.display import display, clear_output

from machine_run_state import Machine_Run_State


class TuringMachineVisualizer:
    def __init__(self, turing_machine):
        self.tm = turing_machine
        self.steps = [] ##type is Machine_Run_State


    def run_and_visualize(self, input_string, max_steps=10):
        clear_output(wait=True) # clear first output of getting user input
        # Reset visualization steps
        self.steps = []
        if not self.tm.contains_chars(input_string, self.tm.input_alphabet):
            self.steps.append("input string contains char not from the alphabet.")
            return self.steps
        self.tm.current_machine_state.put_word_on_tape(input_string)
        new_machine_run_state = Machine_Run_State(self.tm.current_machine_state.tape.copy(),
                                                  self.tm.current_machine_state.head_position,
                                                  self.tm.current_machine_state.state)
        new_machine_run_state.put_word_on_tape(input_string)
        self.steps.append(new_machine_run_state)
        # Run the Turing machine and capture visualization steps for a limited number of steps
        for step in range(max_steps):
            if((self.tm.current_machine_state.state in self.tm.accept_states) or (self.tm.current_machine_state.state in self.tm.reject_states)):
              self.steps.append(self.tm.current_machine_state)
              break
            current_config=self.tm.get_config()
            self.steps.append(self.tm.run_step(current_config))

        if self.tm.current_machine_state.state in self.tm.accept_states:
            self.steps.append("reached accept state")
        elif self.tm.current_machine_state.state in self.tm.reject_states:
            self.steps.append("reached reject state")
        else:
            self.steps.append("turing machine stoped before finishing the run on the given input")
        return self.steps

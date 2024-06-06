import os
import sys
# Add the parent directory of mypackage to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
from IPython.display import display, clear_output
 ##@@@@@@@@@@@@@@@@@@@@@@222 if you run sandbox remove this turing_machine_tutor.
##@@@@@@@@@@@@@@@@@@@@@@222 if you run test put this turing_machine_tutor.
from turing_machine_tutor.CombinedTuringMachine import CombinedTuringMachine
from turing_machine_tutor.TuringMachine import TuringMachine
from turing_machine_tutor.machine_run_state import Machine_Run_State
from turing_machine_tutor.IFTuringMachine import IFTuringMachine

class TuringMachineVisualizer:
    def __init__(self, turing_machine):
        if not(isinstance(turing_machine,IFTuringMachine) or isinstance(turing_machine,CombinedTuringMachine) or isinstance(turing_machine,TuringMachine)):
            raise Exception("TM cannot be Not (TuringMachine / IFTuringMachine / CombinedTuringMachine) Object")
        self.tm = turing_machine
        self.steps = [] ##type is Machine_Run_State


    def run_and_visualize(self, input_string, max_steps=10,head_position=0):
        if(isinstance(self.tm,IFTuringMachine)):
            return self.run_and_visualize_if_turing_machine(input_string)
        elif(isinstance(self.tm,CombinedTuringMachine)):
            return self.run_and_visualize_combined_turing_machine(input_string)
        elif(isinstance(self.tm,TuringMachine)):
            #clear_output(wait=True)  # clear first output of getting user input
            # Reset visualization steps
            self.steps = []
            if not self.tm.contains_chars(input_string):
                self.steps.append("rejected input, input string contains char not from the alphabet.")
                return self.steps
            self.tm.reset_turing_machine()
            self.tm.current_machine_state.head_position=head_position
            self.tm.current_machine_state.put_word_on_tape(input_string)
            new_machine_run_state = Machine_Run_State(self.tm.current_machine_state.tape.copy(),
                                                      self.tm.current_machine_state.head_position,
                                                      self.tm.current_machine_state.state)
            new_machine_run_state.put_word_on_tape(input_string)
            self.steps.append(new_machine_run_state)
            # Run the Turing machine and capture visualization steps for a limited number of steps
            for step in range(max_steps):
                if ((self.tm.current_machine_state.state in self.tm.accept_states) or (
                        self.tm.current_machine_state.state in self.tm.reject_states)):
                    self.steps.append(self.tm.current_machine_state)
                    break
                current_config = self.tm.get_config()
                # new change here
                if current_config == "halt":
                    symbol = self.tm.current_machine_state.tape[self.tm.current_machine_state.head_position]
                    state=self.tm.current_machine_state.state
                    self.steps.append("TM halted at (state: "+str(state)+", symbol: "+str(symbol)+") with no valid transition.")
                    break
                else:
                    self.steps.append(self.tm.run_step(current_config))

            if self.tm.current_machine_state.state in self.tm.accept_states:
                self.steps.append("reached accept state") # To do: add name at the first of line
            elif self.tm.current_machine_state.state in self.tm.reject_states:
                self.steps.append("reached reject state") # To do: add name at the first of line
            else:
                self.steps.append("turing machine halted at non accepting state")
            return self.steps


    def run_and_visualize_combined_turing_machine(self, input_string,head_position=0):
        clear_output(wait=True)  # clear first output of getting user input
        # Reset visualization steps
        self.steps = []
        first_step_is_over_flag = 0
        machine_run_state=None
        self.tm.turing_machines[0].reset_turing_machine() ## only reset first machine
        cond = False
        #index = 0
        index_tm_name = 0
        while not cond:
            for turing_machine in self.tm.turing_machines:
                visualizer = TuringMachineVisualizer(turing_machine)
                if not turing_machine.contains_chars(input_string):
                    self.steps.append("rejected input, input string contains char not from the alphabet.")
                    return self.steps
                if first_step_is_over_flag==0:
                    try:
                        self.steps.append("starting with turing machine with the name: "+self.tm.turing_machines[index_tm_name].name)
                        self.steps=self.steps+visualizer.run_and_visualize(input_string, 5000,head_position)
                        index_tm_name += 1
                        if(index_tm_name < len(self.tm.turing_machines) and self.steps[-1] == "reached accept state"):
                            self.steps.append("proceeding to next turing machine with the name: "+self.tm.turing_machines[index_tm_name].name)
                        turing_machine.reset_turing_machine()
                        machine_run_state=turing_machine.run(input_string,head_position)
                    except Exception as e:
                        self.steps.append("reached reject state")
                        return self.steps
                    first_step_is_over_flag=1
                else:
                    try:
                        self.steps=self.steps+visualizer.run_and_visualize(machine_run_state.tape, 5000,machine_run_state.head_position)
                        index_tm_name += 1
                        if(index_tm_name < len(self.tm.turing_machines) and self.steps[-1] == "reached accept state"):
                            self.steps.append("proceeding to next turing machine with the name: "+self.tm.turing_machines[index_tm_name].name)
                        turing_machine.reset_turing_machine()
                        machine_run_state = turing_machine.run(machine_run_state.tape,machine_run_state.head_position)
                    except Exception as e:
                        self.steps.append("reached reject state")
                        return self.steps
                # self.steps.append("halted on "+self.tm.turing_machines_names[index] + " on acceptance state")
                # index += 1
            #index = 0

            # remove steps with tape [] 
            for s in self.steps:
                if(not isinstance(s,str)):
                    if(len(s.tape) == 0):
                        self.steps.remove(s)

            if (self.tm.while_condition == None):
                return self.steps

            self.steps.append("proceeding to next cond turing machine with the name: "+self.tm.while_condition.name)
            # self.tm.while_condition.run_and_visualize()
            ## run and visulaize While Condition Turing machine
            turing_machine = self.tm.while_condition
            visualizer = TuringMachineVisualizer(turing_machine)
            if not turing_machine.contains_chars(input_string):
                self.steps.append("rejected input, input string contains char not from the alphabet.")
                return self.steps
            if first_step_is_over_flag==0:
                try:
                    self.steps=self.steps+visualizer.run_and_visualize(input_string, 5000,head_position)
                    turing_machine.reset_turing_machine()
                    machine_run_state=turing_machine.run(input_string,head_position)
                except Exception as e:
                    self.steps.append("reached reject state")
                    return self.steps
                first_step_is_over_flag=1
            else:
                try:
                    self.steps=self.steps+visualizer.run_and_visualize(machine_run_state.tape, 5000,machine_run_state.head_position)
                    turing_machine.reset_turing_machine()
                    machine_run_state = turing_machine.run(machine_run_state.tape,machine_run_state.head_position)
                except Exception as e:
                    self.steps.append("reached reject state")
                    return self.steps
            if(self.tm.while_condition != None):
                cond = not self.tm.while_condition.given_state_is_in_acceptance(machine_run_state.state)
            else:
                cond = True
            if not cond:
                index_tm_name = 0
                self.steps.append("starting again with turing machine with the name: "+self.tm.turing_machines[index_tm_name].name)

        return self.steps


    def run_and_visualize_if_turing_machine(self, input_string):
        if_visualizer = TuringMachineVisualizer(self.tm.ifTm)
        if_visualizer.run_and_visualize(input_string, 5000)
        if if_visualizer.tm.current_machine_state.state in if_visualizer.tm.accept_states:
            then_visualizer = TuringMachineVisualizer(self.tm.thenTm)
            then_visualizer.run_and_visualize(input_string, 5000)
            return ["starting with turing machine with the name: "+self.tm.ifTm.name] + if_visualizer.steps + ["proceeding to next turing machine with the name: "+self.tm.thenTm.name] + then_visualizer.steps
        else:
            else_visualizer = TuringMachineVisualizer(self.tm.elseTm)
            else_visualizer.run_and_visualize(input_string, 5000)
            return ["starting with turing machine with the name: "+self.tm.ifTm.name] + if_visualizer.steps  + ["proceeding to next turing machine with the name: "+self.tm.elseTm.name] + else_visualizer.steps


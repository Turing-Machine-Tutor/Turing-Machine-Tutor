import os
import sys
# Add the parent directory of mypackage to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from turing_machine_tutor.TuringMachine import TuringMachine

class CombinedTuringMachine:
    def __init__(self, input_alphabet):
        #self.turing_machines_names = []
        self.turing_machines = []
        if(input_alphabet == None or not isinstance(input_alphabet,(list,set))):
            raise Exception("Please Enter a Valid input_alphabet")
        self.input_alphabet = set(input_alphabet)
        self.while_condition = None
        self.name = ""

    def add(self, new_turing_machine_name, new_turing_machine):
        if(new_turing_machine == None):
            raise Exception("TM cannot be None")
        if(not isinstance(new_turing_machine, TuringMachine)):
            raise Exception("TM cannot be Not Turing Machine Object")
        if(new_turing_machine_name == None or new_turing_machine_name == ""):
            raise Exception("Name cannot be None")
        if(not isinstance(new_turing_machine_name, str)):
            raise Exception("Name cannot be not str object")
        for tm in self.turing_machines:
            if(tm.name == new_turing_machine_name):
                raise Exception("Turing machine with this name already exists in the list")
        new_turing_machine.name = new_turing_machine_name
        self.turing_machines.append(new_turing_machine)
        #self.turing_machines_names.append(new_turing_machine_name)
    def get_input_alphabet(self):
        return self.input_alphabet
        # if(len(self.turing_machines) == 0):
        #     raise Exception("Cannot get input alphabet, please add at least one TM to the Combined Turing Machine")
        # return self.turing_machines[0].get_input_alphabet()
    def remove(self, name):
        if(name == None or name == ""):
            raise Exception("Name cannot be None")
        if(not isinstance(name, str)):
            raise Exception("Name cannot be not str object")
        for tm in self.turing_machines:
            if(tm.name == name):
                self.turing_machines.remove(tm)
                return
        raise Exception("Turing machine with this name doesn't exists in the list")
        

    def setTuringMachineWhileCondition(self, name, while_condition):
        if(while_condition == None):
            raise Exception("While TM cannot be None")
        if(not isinstance(while_condition, TuringMachine)):
            raise Exception("While TM cannot be Not Turing Machine Object")
        if(name == None or name == ""):
            raise Exception("Name cannot be None")
        if(not isinstance(name, str)):
            raise Exception("Name cannot be not str object")
        self.while_condition = while_condition
        self.while_condition.name = name

    def runHelper(self, turing_machines, head_position, result_tm, first_step_is_over_flag, machine_run_state):
        for tm in turing_machines:
            # Run the first Turing machine initially
            try:
                if first_step_is_over_flag==0:
                    machine_run_state = tm.run(result_tm,head_position)
                    first_step_is_over_flag=1
                else:
                    current_head_position=machine_run_state.head_position
                    result_tm = machine_run_state.tape.copy()
                    machine_run_state = tm.run(result_tm,current_head_position)

                if (machine_run_state.state in tm.accept_states):
                    continue
                elif (machine_run_state.state in tm.reject_states):
                    raise Exception("turing machine:  "+tm.name+ " halted on rejected state")
            except Exception as e:
                raise (e)
        return machine_run_state, first_step_is_over_flag , result_tm

    def run(self, input_str,head_position=0): ##if it is not given then it is 0, this what means the '=0'
        result_tm = input_str
        first_step_is_over_flag = 0
        machine_run_state=None
        if (self.while_condition == None):
            machine_run_state, first_step_is_over_flag , result_tm = self.runHelper(self.turing_machines, head_position, result_tm, first_step_is_over_flag,machine_run_state)
            return machine_run_state
        else:
            cond = False
            while not cond:
                machine_run_state, first_step_is_over_flag , result_tm = self.runHelper(self.turing_machines, head_position, result_tm, first_step_is_over_flag, machine_run_state)
                machine_run_state2 = self.while_condition.run(result_tm)
                cond = not self.while_condition.given_state_is_in_acceptance(machine_run_state2.state)
                if(cond):
                     return machine_run_state
                else:
                     machine_run_state = machine_run_state2
        
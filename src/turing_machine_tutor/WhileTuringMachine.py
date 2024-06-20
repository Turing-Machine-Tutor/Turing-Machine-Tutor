import os
import sys
# Add the parent directory of mypackage to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from turing_machine_tutor.TuringMachine import TuringMachine
from turing_machine_tutor.CombinedTuringMachine import CombinedTuringMachine

class WhileTuringMachine(CombinedTuringMachine):
    def __init__(self, condTMName:str,condTM : TuringMachine, doTMName:str, doTM : TuringMachine):
        super().__init__(condTM.input_alphabet)
        self.setTuringMachineWhileCondition(condTMName,condTM)
        self.add(doTMName, doTM)
    
    # def run(self, input_str,head_position=0):
    #     self.run(input_str,head_position)
    
    # def given_state_is_in_acceptance(self,state):
    #     return self.given_state_is_in_acceptance(state)
    # def get_input_alphabet(self):
    #     return self.get_input_alphabet()
    
    # def __str__(self):
    #     return self.__str__()

    def run(self, input_str,head_position=0): ##if it is not given then it is 0, this what means the '=0'
        result_tm = input_str
        first_step_is_over_flag = 0
        machine_run_state=None

        cond = False
        while not cond:
            machine_run_state2 = self.while_condition.run(result_tm)
            cond = not self.while_condition.given_state_is_in_acceptance(machine_run_state2.state)
            if(cond):
                return machine_run_state
            else:
                machine_run_state = machine_run_state2 # if need to save changes after the CondTM else put this line as a comment
            machine_run_state, first_step_is_over_flag , result_tm = self.runHelper(self.turing_machines, head_position, result_tm, first_step_is_over_flag, machine_run_state)

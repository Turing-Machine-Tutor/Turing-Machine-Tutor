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
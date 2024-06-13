import os
import sys
# Add the parent directory of mypackage to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from turing_machine_tutor.TuringMachine import TuringMachine
from turing_machine_tutor.CombinedTuringMachine import CombinedTuringMachine

class ConcatenateTM(CombinedTuringMachine):
    def __init__(self, ls : list):
        if not isinstance(ls,list):
            raise Exception("constructor parameter should be list!")
        if len(ls) == 0:
            raise Exception("constructor parameter should be list of minimum len of 1!")
        for l in ls:
            if not isinstance(l, tuple(str, TuringMachine)):
                raise Exception("every parameter in the list should be tuple(string TM name, TuringMachine object)")
        
        super().__init__(ls[0][1].input_alphabet)
        #self = CombinedTuringMachine(ls[0][1].input_alphabet)
        for l in ls:
            self.add(l[0], l[1])
        
    # def run(self, input_str,head_position=0):
    #     self.run(input_str,head_position)
    
    # def given_state_is_in_acceptance(self,state):
    #     return self.given_state_is_in_acceptance(state)
    
    # def get_input_alphabet(self):
    #     return self.get_input_alphabet()
    
    # def __str__(self):
    #     return self.__str__()
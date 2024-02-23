import random
import string
from TuringMachine import TuringMachine

class TuringMachineController:
    def __init__(self):
        self.turing_machines = {}

    def add_turing_machine(self, name, turing_machine:TuringMachine):
        self.turing_machines[name] = turing_machine

    def remove(self,name):
        if name in self.turing_machines.keys():
            self.turing_machines.pop(name)
        else:
            print("turing machine does not exists")

    def get_turing_machine(self,name):
        if name in self.turing_machines.keys():
            self.turing_machines[name]
        else:
            print("turing machine does not exists")

    def get_all_names(self):
        return self.turing_machines.keys()



    def run_turing_machine(self, name, input_string):
        try:
            return self.turing_machines[name].run(input_string)
        except Exception as e:
            print(e)


    def visualize(self,turing_name,input):
        raise Exception("to do")


    def validate_turing_machines(self,turing_name,function_object,extreme_cases,test_count=100,max_input_length=20):
        try:
            for _ in range(test_count): ## generate random words and test them
                for input_length in range(1,max_input_length):
                    alphabet = ''.join(self.turing_machines[turing_name].alphabet)
                    input_string = ''.join(random.choice(alphabet) for _ in range(input_length))
                    print("testing on input: "+input_string)
                    config=self.turing_machines[turing_name].run(input_string)
                    function_result=function_object(input_string) ## boolean function i guess
                    ##   result1, accepted1 = self.turing_machines[original].run(input_string)
                    ## result2, accepted2 = self.turing_machines[userTm].run(input_string)
                    # if (result1 != result2) or (accepted1 != accepted2):
                    if function_result!=config.state :
                        print(f"Validation failed for input: {input_string}")
                        return False
                    else :
                        print(f"Validation passed for input: {input_string}")
            print("Validation passed for all Turing machines.")
            return True
        except Exception as e:
            print(e)


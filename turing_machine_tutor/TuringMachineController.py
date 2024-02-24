import random
import string
from TuringMachine import TuringMachine
from TuringMachineVisualizer import TuringMachineVisualizer


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
        self.turing_machines[turing_name].reset_turing_machine()
        visualizer =TuringMachineVisualizer(self.turing_machines[turing_name])
        visualizer.run_and_visualize(input,5000)



    def validate_turing_machine(self,turing_name,function_object,extreme_cases,test_count=100,max_input_length=20):
        try:
            for _ in range(test_count): ## generate random words and test them
                for input_length in range(1,max_input_length):
                    alphabet = ''.join(self.turing_machines[turing_name].input_alphabet)
                    input_string = ''.join(random.choice(alphabet) for _ in range(input_length))
                    print("testing on input: "+input_string)
                    final_machine_state=self.turing_machines[turing_name].run(input_string)
                    function_result=function_object(input_string) ## boolean function i guess
                    is_in_acceptance_checker=self.turing_machines[turing_name].given_state_is_in_acceptance(final_machine_state.state)
                    if function_result!=is_in_acceptance_checker:
                        print(f"Validation failed for input: {input_string}")
                        return False
                    else :
                        print(f"Validation passed for input: {input_string}")
            print("testing extreme cases:\n ")
            for extreme_case in extreme_cases: ##test extreme cases
                final_machine_state = self.turing_machines[turing_name].run(extreme_case)
                function_result = function_object(input_string)
                is_in_acceptance_checker = self.turing_machines[turing_name].given_state_is_in_acceptance(final_machine_state.state)
                if function_result != is_in_acceptance_checker:
                    print(f"Validation failed for input: {extreme_case}")
                    return False
                else:
                    print(f"Validation passed for input: {extreme_case}")

            print("Validation passed for all Turing machines.")
            return True
        except Exception as e:
            print(e)


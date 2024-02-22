import random
import string

class TuringMachineLibrary:
    def __init__(self):
        self.turing_machines = {}

    def add_turing_machine(self, name, turing_machine): ## @@@ i think we should put ID instead of name, for the future when using DAL
        self.turing_machines[name] = turing_machine

    def run_turing_machine(self, name, input_string):
        if name in self.turing_machines:
            return self.turing_machines[name].run(input_string)
        else:
            return "Turing machine not found in the library."

    def validate_turing_machines(self,original, userTm, test_count=100, max_input_test_length=20):
        if original != userTm: # name of two turing machines
            for _ in range(test_count):
                for input_length in range(1,max_input_test_length):
                    alphabet = ''.join(self.turing_machines[original].alphabet)
                    input_string = ''.join(random.choice(alphabet) for _ in range(input_length))
                    print("testing on input: "+input_string)
                    result1, accepted1 = self.turing_machines[original].run(input_string)
                    result2, accepted2 = self.turing_machines[userTm].run(input_string)

                    if (result1 != result2) or (accepted1 != accepted2):
                        print(f"Validation failed between {original} and {userTm} for input: {input_string}")
                        return False
                    else:
                        print(f"Validation passed between {original} and {userTm} for input: {input_string}")
        print("Validation passed for all Turing machines.")
        return True


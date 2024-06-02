import random
import time
import os
import sys
# Add the parent directory of mypackage to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from turing_machine_tutor.TuringMachine import TuringMachine
from turing_machine_tutor.CombinedTuringMachine import CombinedTuringMachine
from turing_machine_tutor.IFTuringMachine import IFTuringMachine
from turing_machine_tutor.TuringMachineVisualizer import TuringMachineVisualizer
from turing_machine_tutor.Challenge import Challenge
from IPython.display import display, clear_output
import ast
import inspect


# imports for submission
import gspread
from google.colab import auth
from oauth2client.client import GoogleCredentials
from google.auth import default

class TuringMachineController:
    def __init__(self):
        self.turing_machines = {}
        self.challenges = dict()

    def add_turing_machine(self, name, turing_machine):
        if(turing_machine == None):
            raise Exception("TM cannot be None")
        if not(isinstance(turing_machine, TuringMachine) or isinstance(turing_machine, IFTuringMachine) or isinstance(turing_machine, CombinedTuringMachine) ):
            raise Exception("TM cannot be Not (TuringMachine / IFTuringMachine / CombinedTuringMachine) Object")
        if(name == None or name == ""):
            raise Exception("Name cannot be None")
        if(not isinstance(name, str)):
            raise Exception("Name cannot be not str object")
        if(name in self.turing_machines.keys()):
            raise Exception("Turing machine with this name already exists in the dict")
        turing_machine.name = name
        self.turing_machines[name] = turing_machine

    def remove(self,name):
        if(name == None or name == ""):
            raise Exception("Name cannot be None")
        if(not isinstance(name, str)):
            raise Exception("Name cannot be not str object")
        if name in self.turing_machines.keys():
            self.turing_machines.pop(name)
        else:
            raise Exception("Turing machine with this name doesn't exists in the dict")

    def get_turing_machine(self,name):
        if(name == None or name == ""):
            raise Exception("Name cannot be None")
        if(not isinstance(name, str)):
            raise Exception("Name cannot be not str object")
        if name in self.turing_machines.keys():
            return self.turing_machines[name]
        else:
            raise Exception("Turing machine with this name doesn't exists in the dict")

    def get_all_names(self):
        return self.turing_machines.keys()

    def run_turing_machine(self, name, input_string):
        try:
            output = self.turing_machines[name].run(input_string)
            try:
                print("tape:= " + ''.join(output.tape.copy()))
                print("accepted:= "+str(self.turing_machines[name].given_state_is_in_acceptance(output.state)))
            except Exception as e:
                print(e)
            return output
        except Exception as e:
            print(e)


    def visualize(self,turing_name,input):
        #self.turing_machines[turing_name].reset_turing_machine()
        visualizer =TuringMachineVisualizer(self.turing_machines[turing_name])
        steps = visualizer.run_and_visualize(input,5000)

        self.display_steps_of_visualizer(steps)


    def visualize_step_by_step(self,turing_name,machine_input):
        #self.turing_machines[turing_name].reset_turing_machine()
        visualizer =TuringMachineVisualizer(self.turing_machines[turing_name])
        steps= visualizer.run_and_visualize(machine_input,5000)
        user_input = "start"
        index=0
        step_counter=0

        # remove steps with tape [] 
        for s in steps:
            if(not isinstance(s,str)):
                if(len(s.tape) == 0):
                    steps.remove(s)

        while user_input.lower() !="stop":
            step_counter=self.display_step_at_index(steps,index,step_counter)
            if(step_counter==-1):
                return
            user_input = input("Press Enter to continue or type 'stop' to end: ")
            #clear_output(wait=True)
            index=index+1
            



    def display_step_at_index(self, steps,index,step_counter):
        if (isinstance(steps[index], str)):
            if index<len(steps)-1:
                print(steps[index])
                time.sleep(1)
                clear_output(wait=True)
                return step_counter + 1
            else:
                print(steps[index])
                time.sleep(1)
                clear_output(wait=True)
                return -1
        self.print_step(steps[index], step_counter)
        clear_output(wait=True)
        return step_counter + 1





    def display_steps_of_visualizer(self,steps):
        steps_counter=0
        for step in steps:
            # Display the tape as an array
            if(isinstance(step, str)):
                print(step)
                time.sleep(1)
                clear_output(wait=True)
                continue
            self.print_step(step,steps_counter)
            clear_output(wait=True)
            steps_counter=steps_counter+1
    

    def print_step(self, step, step_counter):
        tape_str = ' '.join(step.tape)

        head_position_str = ' ' * (2 * step.head_position) + '^'
        # Display current state and step number
        state_step_info = f"State: {step.state} | Step: {step_counter + 1}"
        if (len(step.tape) == 0):
            # print("proceeding to next turing machine")
            # time.sleep(0.5)  # Pause for a short duration to visualize each step
            # clear_output(wait=True)
            # print(f"Step: {step_counter + 1}")
            # time.sleep(1)  # Pause for a short duration to visualize each step
            # clear_output(wait=True)
            return
        # Print the visualization
        print(tape_str)
        print(head_position_str)
        print(state_step_info)
        print('-' * (2 * len(step.tape) + 1))  # Separator line
        time.sleep(1)  # Pause for a short duration to visualize each step
        clear_output(wait=True)


    def validate_turing_machineTA(self, name, test_count=100,max_input_length=20):
        turing_name = name
        
        if(turing_name == None or turing_name == ""):
            raise Exception("Name cannot be None")
        if(not isinstance(turing_name, str)):
            raise Exception("Name cannot be not str object")
        if turing_name not in self.turing_machines.keys():
            raise Exception("there is no turing machine with the name: "+turing_name)
        function_object = self.challenges[turing_name].function
        
        if(function_object == None):
            raise Exception("func cannot be None")
        if(not callable(function_object)):
            raise Exception("func cannot be not function object")
        try:
            if(not isinstance(function_object(""),bool)):
                raise Exception()
        except Exception as e:
            raise Exception("func cannot be function object that doesnt get string input and output True/False (boolean)")
        is_all_strings = lambda my_list: all(isinstance(item, str) and len(item) >= 1 for item in my_list)
        extreme_cases= self.challenges[turing_name].edge_cases
        if(extreme_cases == None):
            raise Exception("extreme_cases cannot be None")
        if((not isinstance(extreme_cases, (list,set))) or not is_all_strings(extreme_cases)):
            raise Exception("extreme_cases cannot contain a non string object")

        for _ in range(test_count): ## generate random words and test them
            for input_length in range(1,max_input_length):
                #print("My alphabet is : " + str(self.turing_machines[turing_name].get_input_alphabet()))
                alphabet = ''.join(self.turing_machines[turing_name].get_input_alphabet())
                input_string = ''.join(random.choice(alphabet) for _ in range(input_length))
                print("testing on input: "+input_string)
                final_machine_state=None
                try:
                    final_machine_state=self.turing_machines[turing_name].run(input_string)
                    #final_machine_state=self.turing_machines[turing_name].run("01")
                except Exception as e:
                    print(e)
                    final_machine_state = None
                function_result=function_object(input_string) ## boolean function i guess
                if (final_machine_state == None):
                    str_results = "func returned: " + str(function_result) + " TM returned: False" 
                    if function_result == False:
                        print(f"Validation passed for input: {input_string}")
                    else:
                        print(f"Validation failed for input: {input_string}" + " , " + str_results)
                        return False
                    continue
                if (isinstance(self.turing_machines[turing_name], TuringMachine)):
                    ##it is normal turing machine
                    is_in_acceptance_checker=self.turing_machines[turing_name].given_state_is_in_acceptance(final_machine_state.state)
                else:
                    ##it is combined_turing_machine
                    is_in_acceptance_checker = self.turing_machines[turing_name].turing_machines[-1].given_state_is_in_acceptance(
                        final_machine_state.state)
                if function_result!=is_in_acceptance_checker:
                    str_results = "func returned: " + str(function_result) + " TM returned: "+str(is_in_acceptance_checker) 
                    print(f"Validation failed for input: {input_string}" + " , " + str_results)
                    return False
                else :
                    print(f"Validation passed for input: {input_string}")
        print("testing extreme cases:\n ")
        for extreme_case in extreme_cases: ##test extreme cases
            final_machine_state=None
            try:
                final_machine_state = self.turing_machines[turing_name].run(extreme_case)
            except Exception as e:
                print(e)

            function_result = function_object(extreme_case)
            if (final_machine_state == None):
                if function_result == False:
                    print(f"Validation passed for input: {extreme_case}")
                else:
                    print(f"Validation failed for input: {extreme_case}")
                    return False
                continue
            is_in_acceptance_checker = self.turing_machines[turing_name].given_state_is_in_acceptance(final_machine_state.state)
            if function_result != is_in_acceptance_checker:
                print(f"Validation failed for input: {extreme_case}")
                return False
            else:
                print(f"Validation passed for input: {extreme_case}")

        print("Validation passed for all Turing machines.")
        return True

    # user can use this function
    def validate_turing_machine(self,turing_name,function_object,extreme_cases=[],test_count=100,max_input_length=20):
            if(turing_name == None or turing_name == ""):
                raise Exception("Name cannot be None")
            if(not isinstance(turing_name, str)):
                raise Exception("Name cannot be not str object")
            if turing_name not in self.turing_machines.keys():
                raise Exception("there is no turing machine with the name: "+turing_name)
            if(function_object == None):
                raise Exception("func cannot be None")
            if(not callable(function_object)):
                raise Exception("func cannot be not function object")
            try:
                if(not isinstance(function_object(""),bool)):
                    raise Exception()
                str_msg = self.validateFuncReturnOnlyBool(function_object)
                if(len(str_msg) > 0):
                    raise Exception("found error in func at line value: "+str_msg+" , func should return only True/False")
            except Exception as e:
                if(len(str(e)) > 0 and "found error in func at line value: " in str(e)):
                    raise e
                else:
                    raise Exception("func cannot be function object that doesnt get string input and output True/False (boolean)")
            is_all_strings = lambda my_list: all(isinstance(item, str) and len(item) >= 1 for item in my_list)
            if(extreme_cases == None):
                raise Exception("extreme_cases cannot be None")
            if((not isinstance(extreme_cases, (list,set))) or not is_all_strings(extreme_cases)):
                raise Exception("extreme_cases cannot contain a non string object")

            for _ in range(test_count): ## generate random words and test them
                for input_length in range(1,max_input_length):
                    #print("My alphabet is : " + str(self.turing_machines[turing_name].get_input_alphabet()))
                    alphabet = ''.join(self.turing_machines[turing_name].get_input_alphabet())
                    input_string = ''.join(random.choice(alphabet) for _ in range(input_length))
                    print("testing on input: "+input_string)
                    final_machine_state=None
                    try:
                        final_machine_state=self.turing_machines[turing_name].run(input_string)
                        #final_machine_state=self.turing_machines[turing_name].run("01")
                    except Exception as e:
                        print(e)
                        final_machine_state = None
                    function_result=function_object(input_string) ## boolean function i guess
                    if (final_machine_state == None):
                        str_results = "func returned: " + str(function_result) + " TM returned: False" 
                        if function_result == False:
                            print(f"Validation passed for input: {input_string}")
                        else:
                            print(f"Validation failed for input: {input_string}" + " , " + str_results)
                            return False
                        continue
                    if (isinstance(self.turing_machines[turing_name], TuringMachine)):
                        ##it is normal turing machine
                        is_in_acceptance_checker=self.turing_machines[turing_name].given_state_is_in_acceptance(final_machine_state.state)
                    else:
                        ##it is combined_turing_machine
                        is_in_acceptance_checker = self.turing_machines[turing_name].turing_machines[-1].given_state_is_in_acceptance(
                            final_machine_state.state)
                    if function_result!=is_in_acceptance_checker:
                        str_results = "func returned: " + str(function_result) + " TM returned: "+str(is_in_acceptance_checker) 
                        print(f"Validation failed for input: {input_string}" + " , " + str_results)
                        return False
                    else :
                        print(f"Validation passed for input: {input_string}")
            print("testing extreme cases:\n ")
            for extreme_case in extreme_cases: ##test extreme cases
                final_machine_state=None
                try:
                    final_machine_state = self.turing_machines[turing_name].run(extreme_case)
                except Exception as e:
                    print(e)

                function_result = function_object(extreme_case)
                if (final_machine_state == None):
                    if function_result == False:
                        print(f"Validation passed for input: {extreme_case}")
                    else:
                        print(f"Validation failed for input: {extreme_case}")
                        return False
                    continue
                is_in_acceptance_checker = self.turing_machines[turing_name].given_state_is_in_acceptance(final_machine_state.state)
                if function_result != is_in_acceptance_checker:
                    print(f"Validation failed for input: {extreme_case}")
                    return False
                else:
                    print(f"Validation passed for input: {extreme_case}")

            print("Validation passed for all Turing machines.")
            return True
    

    def add_challenge(self, turing_machine_name, turing_machine_description, function_that_accepts_the_language_of_tm,
                      edge_cases_list):
        challenge = Challenge(turing_machine_name, turing_machine_description, function_that_accepts_the_language_of_tm, edge_cases_list)
        if(turing_machine_name in self.challenges.keys()):
            raise Exception("challenge with this name already exists")
        self.challenges[turing_machine_name] = challenge

    def get_challenges(self):
        print("\n\ncurrent available challenges:\n")
        index = 1
        for key in self.challenges.keys():
            print(f"[{index}]turing machine name: {key}")
            print(f"description: {self.challenges[key].description}\n")
            index = index + 1

    def validateFuncReturnOnlyBool(self, func):
        # Get the source code of the function
        source_lines, _ = inspect.getsourcelines(func)
        source_code = ''.join(source_lines)

        # Parse the source code into an AST (Abstract Syntax Tree)
        tree = ast.parse(source_code)

        # Extract return statements from the AST
        for node in ast.walk(tree):
            if isinstance(node, ast.Return):
                # Get the value of the return statement if it exists
                if node.value is not None:
                    return_stmt = ast.unparse(node).strip()
                    if return_stmt not in ["return True", "return False"]:
                        return return_stmt
                else:
                    return "return"  # Empty return statement

        return ""  # All return statements are valid



    def log_results(self, TM, spreadsheet_url):
        # Authorize the Google Sheets API
        auth.authenticate_user()
        creds, _ = default()
        gc = gspread.authorize(creds)
        sheet = gc.open_by_url(spreadsheet_url).sheet1
        # Get User ID
        user_id = input("Please enter your ID number: ")
        #"""Log the test results to Google Sheets."""
        sheet.append_row([user_id, self.get_turing_machine(TM).__str__(), "Passed" if self.validate_turing_machineTA('0n1n') else "Failed"])
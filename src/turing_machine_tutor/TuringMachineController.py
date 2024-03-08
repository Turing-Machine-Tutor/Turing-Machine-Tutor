import random
import time

from TuringMachine import TuringMachine
from TuringMachineVisualizer import TuringMachineVisualizer
from turing_machine_tutor.Challenge import Challenge


class TuringMachineController:
    def __init__(self):
        self.turing_machines = {}
        self.challenges = dict()

    def add_turing_machine(self, name, turing_machine):
        turing_machine.name = name
        self.turing_machines[name] = turing_machine

    def remove(self,name):
        if name in self.turing_machines.keys():
            self.turing_machines.pop(name)
        else:
            print("turing machine does not exists")

    def get_turing_machine(self,name):
        if name in self.turing_machines.keys():
            return self.turing_machines[name]
        else:
            print("turing machine does not exists")

    def get_all_names(self):
        return self.turing_machines.keys()


    def run_turing_machine_with_while_condition(self,input_string,condition_machine_chekcer,combined_machine_name):
        try:
            machine_run_state=self.turing_machines[combined_machine_name].run(input_string,0)
            machine_run_state=condition_machine_chekcer.run(machine_run_state.tape)
            while not condition_machine_chekcer.given_state_is_in_acceptance(machine_run_state.state):
                machine_run_state = self.turing_machines[combined_machine_name].run(machine_run_state.tape,machine_run_state.head_position)
                machine_run_state=condition_machine_chekcer.run(machine_run_state.tape)
            return machine_run_state
        except Exception as e:
            print(e)



    def run_turing_machine(self, name, input_string):
        try:
            return self.turing_machines[name].run(input_string)
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
        user_input = input("Press Enter to continue or type 'stop' to end: ")
        index=0
        step_counter=0
        while user_input!="stop":
            step_counter=self.display_step_at_index(steps,index,step_counter)
            if(step_counter==-1):
                return
            index=index+1
            user_input = input("Press Enter to continue or type 'stop' to end: ")



    def display_step_at_index(self, steps,index,step_counter):
        if (isinstance(steps[index], str)):
            if index<len(steps)-1:
                print(steps[index])
                return step_counter + 1
            else:
                print(steps[index])
                return -1
        self.print_step(steps[index], step_counter)
        return step_counter + 1





    def display_steps_of_visualizer(self,steps):
        steps_counter=0
        for step in steps:
            # Display the tape as an array
            if(isinstance(step, str)):
                print(step)
                continue
            self.print_step(step,steps_counter)
            steps_counter=steps_counter+1


    def print_step(self, step, step_counter):
        tape_str = ' '.join(step.tape)

        head_position_str = ' ' * (2 * step.head_position) + '^'
        # Display current state and step number
        state_step_info = f"State: {step.state} | Step: {step_counter + 1}"
        if (len(step.tape) == 0):
            print("\n\n")
            print("proceeding to next turing machine")
            print(f"Step: {step_counter + 1}")
            time.sleep(1)  # Pause for a short duration to visualize each step
            print("\n\n\n")
            return
        # Print the visualization
        print(tape_str)
        print(head_position_str)
        print(state_step_info)
        print('-' * (2 * len(step.tape) + 1))  # Separator line
        time.sleep(1)  # Pause for a short duration to visualize each step
        print("\n\n\n")



    def validate_turing_machine(self,turing_name,function_object,extreme_cases,test_count=100,max_input_length=20):
            if turing_name not in self.turing_machines.keys():
                raise Exception("there is no turing machine with the name: ",turing_name)
            for _ in range(test_count): ## generate random words and test them
                for input_length in range(1,max_input_length):
                    alphabet = ''.join(self.turing_machines[turing_name].input_alphabet)
                    input_string = ''.join(random.choice(alphabet) for _ in range(input_length))
                    print("testing on input: "+input_string)
                    final_machine_state=None
                    try:
                        final_machine_state=self.turing_machines[turing_name].run(input_string)
                    except Exception as e:
                        print(e)
                    function_result=function_object(input_string) ## boolean function i guess
                    if (final_machine_state == None):
                        str_results = "func returned: " + str(function_result) + " TM returned: False" 
                        if function_result == False:
                            print(f"Validation passed for input: {input_string}")
                        else:
                            print(f"Validation failed for input: {input_string}" + " , " + str_results)
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
                    continue
                is_in_acceptance_checker = self.turing_machines[turing_name].given_state_is_in_acceptance(final_machine_state.state)
                if function_result != is_in_acceptance_checker:
                    print(f"Validation failed for input: {extreme_case}")
                    return False
                else:
                    print(f"Validation passed for input: {extreme_case}")

            print("Validation passed for all Turing machines.")
            return True

    # def validate_combined_turing_machine_with_while_condition(self,turing_name,function_object,extreme_cases,condition_machine_chekcer,test_count=100,max_input_length=20):
    #     try:
    #         if turing_name not in self.turing_machines.keys():
    #             raise Exception("there is no turing machine with the name: ", turing_name)
    #         for _ in range(test_count):  ## generate random words and test them
    #             for input_length in range(1, max_input_length):
    #                 alphabet = ''.join(self.turing_machines[turing_name].input_alphabet)
    #                 input_string = ''.join(random.choice(alphabet) for _ in range(input_length))
    #                 print("testing on input: " + input_string)
    #                 final_machine_state=self.run_turing_machine_with_while_condition(input_string,condition_machine_chekcer,turing_name)
    #                 function_result = function_object(input_string)  ## boolean function i guess
    #                 if(final_machine_state==None):
    #                     if function_result==False:
    #                         print(f"Validation passed for input: {input_string}")
    #                     else:
    #                         print(f"Validation failed for input: {input_string}")
    #                     continue
    #                 is_in_acceptance_checker = condition_machine_chekcer.given_state_is_in_acceptance(
    #                     final_machine_state.state)
    #                 if function_result != is_in_acceptance_checker:
    #                     print(f"Validation failed for input: {input_string}")
    #                     return False
    #                 else:
    #                     print(f"Validation passed for input: {input_string}")
    #         print("testing extreme cases:\n ")
    #         for extreme_case in extreme_cases:  ##test extreme cases
    #             final_machine_state=self.run_turing_machine_with_while_condition(extreme_case,condition_machine_chekcer,turing_name)
    #             function_result = function_object(extreme_case)
    #             if (final_machine_state == None):
    #                 if function_result == False:
    #                     print(f"Validation passed for input: {extreme_case}")
    #                 else:
    #                     print(f"Validation failed for input: {extreme_case}")
    #                 continue
    #             is_in_acceptance_checker = condition_machine_chekcer.given_state_is_in_acceptance(
    #                 final_machine_state.state)
    #             if function_result != is_in_acceptance_checker:
    #                 print(f"Validation failed for input: {extreme_case}")
    #                 return False
    #             else:
    #                 print(f"Validation passed for input: {extreme_case}")

    #         print("Validation passed for all Turing machines.")
    #         return True
    #     except Exception as e:
    #         print(e)

    def visualize_combined_machine_step_by_step(self, machine_name, input_string):
        #self.turing_machines[machine_name].reset_turing_machine()
        visualizer = TuringMachineVisualizer(self.turing_machines[machine_name])
        steps = visualizer.run_and_visualize(input_string, 5000)
        user_input = input("Press Enter to continue or type 'stop' to end: ")
        index = 0
        step_counter = 0
        while user_input != "stop":
            step_counter = self.display_step_at_index(steps, index, step_counter)
            if (step_counter == -1):
                return
            index = index + 1
            user_input = input("Press Enter to continue or type 'stop' to end: ")

    # def visualize_with_while_condition_machine(self, input_string,condition_machine_chekcer,combined_machine_name):
    #     try:
    #         visualizer = TuringMachineVisualizer(self.turing_machines[combined_machine_name])
    #         visualizer_while_machine = TuringMachineVisualizer(condition_machine_chekcer)
    #         steps = visualizer.run_and_visualize_combined_turing_machine(input_string)
    #         machine_run_state=steps[len(steps)-3]
    #         steps = steps+visualizer_while_machine.run_and_visualize(machine_run_state.tape, 500)
    #         machine_run_state=steps[len(steps)-3]
    #         while not condition_machine_chekcer.given_state_is_in_acceptance(machine_run_state.state):
    #             steps = steps+visualizer.run_and_visualize_combined_turing_machine(machine_run_state.tape,machine_run_state.head_position)
    #             machine_run_state = steps[len(steps) - 3]
    #             steps = steps + visualizer_while_machine.run_and_visualize(machine_run_state.tape, 500)
    #             machine_run_state = steps[len(steps) - 3]
    #         self.display_steps_of_visualizer(steps)
    #     except Exception as e:
    #         print(e)

    def add_challenge(self, turing_machine_name, turing_machine_description, function_that_accepts_the_language_of_tm,
                      edge_cases_list):
        challenge = Challenge(turing_machine_description, function_that_accepts_the_language_of_tm, edge_cases_list)
        self.challenges[turing_machine_name] = challenge

    def get_challenges(self):
        print("\n\ncurrent available challenges:\n")
        index = 1
        for key in self.challenges.keys():
            print(f"[{index}]turing machine name: {key}")
            print(f"description: {self.challenges[key].description}\n")
            index = index + 1





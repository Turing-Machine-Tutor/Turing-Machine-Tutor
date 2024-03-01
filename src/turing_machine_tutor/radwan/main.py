# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GY4-Y__U-qjOnkUcnQVnGx7U7spbwGaz
"""

import random
import string

class TuringMachine:
    def __init__(self, states, alphabet, tape_symbols, blank, transitions, initial_state, accept_states, reject_states):
        self.states = set(states)
        self.alphabet = set(alphabet)
        self.tape_symbols = set(tape_symbols)
        self.transitions = transitions
        self.initial_state = initial_state
        self.accept_states = set(accept_states) ##list
        self.reject_states = set(reject_states) ##list
        self.blank = blank

    def run_step(self, tape, head_position, current_state):
        # Check if the current state is an accepting or rejecting state
        if current_state in self.accept_states or current_state in self.reject_states:
            return tape, head_position, current_state

        # Retrieve the current symbol under the tape head
        current_symbol = tape[head_position] if 0 <= head_position < len(tape) else '_'
        if(current_symbol not in self.tape_symbols):
            print("error on input: tape contains symbol not in tape alphabet.")
            return tape, -1, current_state # return head_position as -1
        # Check if a transition is defined for the current state and symbol
        if (current_state, current_symbol) in self.transitions:
            new_state, write_symbol, move_direction = self.transitions[(current_state, current_symbol)]

            # Write the new symbol to the tape
            if 0 <= head_position < len(tape):
                tape[head_position] = write_symbol
            elif move_direction == 'R':
                tape.append(write_symbol)
            elif move_direction == 'L': ## why insert at -1?, the head is in the end it cant be lower than 0
                tape.insert(0, write_symbol)

            # Move the tape head according to the direction specified in the transition
            if move_direction == 'R':
                head_position += 1
                if head_position == len(tape):
                        tape.append(self.blank)  # Blank symbol for extending the tape to the right
            elif move_direction == 'L':
                head_position -= 1
                if head_position < 0: ##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ this isn't illegal? if the head is on 0 and the transition says to move left this means the turing machine is incorrect isn't it?
                        tape.insert(0, self.blank)  # Blank symbol for extending the tape to the left

            return tape, head_position, new_state
        else:
            # If no transition is defined, stay in the current state
            return tape, head_position, current_state

    def contains_chars(self, input_string, char_list):
        for ch in input_string:
            if(ch not in char_list):
                return False
        return True

    def run(self, input_string):
        max_steps=100*len(input_string)
        tape = list(input_string)
        head_position = 0
        current_state = self.initial_state
        steps = 0

        if not self.contains_chars(input_string, self.alphabet):
            print("input string contains char not from the alphabet.")## @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ exepction
            return ''.join(tape), current_state in self.accept_states


        while current_state not in self.accept_states and current_state not in self.reject_states and steps < max_steps:
            current_symbol = tape[head_position]

            if(current_symbol not in self.tape_symbols):
                print("error on input: tape contains symbol not in tape alphabet.") ## @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ this is should be exepection
                return tape, -1, current_state # return head_position as -1

            if (current_state, current_symbol) in self.transitions:
                new_state, new_symbol, move_direction = self.transitions[(current_state, current_symbol)]

                tape[head_position] = new_symbol

                if move_direction == 'R':
                    head_position += 1
                    if head_position == len(tape):
                        tape.append(self.blank)  # Blank symbol for extending the tape to the right
                elif move_direction == 'L':
                    head_position -= 1
                    if head_position < 0: ##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ this isn't illegal? if the head is on 0 and the transition says to move left this means the turing machine is incorrect isn't it?
                        tape.insert(0, self.blank)  # Blank symbol for extending the tape to the left

                current_state = new_state
                steps += 1
            else:
                break

        return ''.join(tape), current_state in self.accept_states

    def run_combined(self, input_string,head_position): ##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ head=0?
          max_steps=100*len(input_string)
          tape = list(input_string)
          #head_position = 0
          current_state = self.initial_state
          steps = 0

          while current_state not in self.accept_states and current_state not in self.reject_states and steps < max_steps:
              current_symbol = tape[head_position]

              if (current_state, current_symbol) in self.transitions:
                  new_state, new_symbol, move_direction = self.transitions[(current_state, current_symbol)]

                  tape[head_position] = new_symbol

                  if move_direction == 'R':
                      head_position += 1
                      if head_position == len(tape):
                          tape.append(self.blank)  # Blank symbol for extending the tape to the right
                  elif move_direction == 'L':
                      head_position -= 1
                      if head_position < 0:
                          tape.insert(0, self.blank)  # Blank symbol for extending the tape to the left

                  current_state = new_state
                  steps += 1
              else:
                  break

          #return ''.join(tape), current_state in self.accept_states, head_position
          return ''.join(tape), current_state, head_position

# Library to manage Turing machines / controller
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

# add 3 examples of turing machines and add them to library

# Example usage:
emptyString = TuringMachine(
    states={'q0', 'q1', 'rej', 'acc'},
    alphabet={'0', '1'},
    tape_symbols={'0', '1', '_'},
    blank = '_',
    transitions={
        ('q0', '0'): ('q1', '0', 'R'),
        ('q0', '1'): ('q1', '1', 'R'),
        ('q1', '0'): ('q0', '0', 'R'),
        ('q1', '1'): ('q0', '1', 'R'),
        ('q0', '_'): ('acc', '_', 'R'),
        ('q1', '_'): ('rej', '_', 'R'),
    },
    initial_state='q0',
    accept_states={'acc'},
    reject_states={'rej'}
)


# Create a Turing machine
tm1 = TuringMachine(
    states={'q0', 'q1', 'q2', 'q3'},
    alphabet={'0', '1'},
    tape_symbols={'0', '1', '_'},
    blank = '_',
    transitions={
        ('q0', '0'): ('q1', '0', 'R'),
        ('q0', '1'): ('q1', '1', 'R'),
        ('q1', '0'): ('q0', '0', 'R'),
        ('q1', '1'): ('q0', '1', 'R'),
        ('q0', '_'): ('q3', '_', 'R'),
        ('q1', '_'): ('q2', '_', 'R'),
    },
    initial_state='q0',
    accept_states={'q3'},
    reject_states={'q2'}
)

# Add the Turing machine to the library
library = TuringMachineLibrary()
library.add_turing_machine('emptyString', emptyString)
library.add_turing_machine('tm1',tm1)

# Run the Turing machine from the library
result, accepted = library.run_turing_machine('tm1', '000111')

# Display the result
print("Result:", result)
print("Accepted:", accepted)

# library.add_turing_machine('tm1', tm1)
# library.add_turing_machine('tm2', tm2)
# Add more Turing machines as needed

# Validate the Turing machines
validation_result = library.validate_turing_machines('emptyString','tm1')

# Display the validation result
print("Validation Result:", validation_result)

# import matplotlib.pyplot as plt
# from IPython.display import display, clear_output
# import time

# class TuringMachineVisualizer:
#     def __init__(self, turing_machine):
#         self.tm = turing_machine
#         self.steps = []

#     def visualize_step(self, tape, head_position, current_state):
#         # Add a step to the list for visualization
#         self.steps.append((tape, head_position, current_state))

#     def display_steps(self):
#         for step, (tape, head_position, current_state) in enumerate(self.steps):
#             # Display the tape as an array
#             tape_str = ' '.join(tape)
#             head_position_str = ' ' * (2 * head_position) + '^'

#             # Display current state and step number
#             state_step_info = f"State: {current_state} | Step: {step + 1}"

#             # Print the visualization
#             print(tape_str)
#             print(head_position_str)
#             print(state_step_info)
#             print('-' * (2 * len(tape) + 1))  # Separator line
#             time.sleep(0.5)  # Pause for a short duration to visualize each step
#             clear_output(wait=True)

#     def run_and_visualize(self, input_string):
#         # Reset visualization steps
#         self.steps = []

#         # Run the Turing machine and capture visualization steps

#         #tape, head_position, current_state = self.tm.run(input_string)
#         tape = "100000001"
#         head_position = 1
#         current_state = 'q0'
#         self.visualize_step(tape, head_position, current_state)

#         # Display the visualization steps
#         self.display_steps()

# # Example usage:

# # Assuming you have defined a Turing machine (tm) and added it to the library

# # Create an instance of the Turing machine visualizer
# visualizer = TuringMachineVisualizer(tm1)

# # Run and visualize the Turing machine on a given input
# visualizer.run_and_visualize("001100")

# Turing machine for the language {0^n1^n}
anbn_turing_machine = TuringMachine(
    states={'q0', 'q1', 'q2', 'q3', 'q4'},
    alphabet={'0', '1'},
    tape_symbols={'0', '1', 'X', 'Y', 'B'},
    blank='B',
    transitions={
        ('q0', '0'): ('q1', 'X', 'R'),  # Move right and replace 0 with X
        ('q0', 'Y'): ('q3', 'Y', 'R'),  # Skip Y
        ('q1', '0'): ('q1', '0', 'R'),  # Continue moving right over 0
        ('q1', '1'): ('q2', 'Y', 'L'),  # Move left and replace 1 with Y
        ('q1', 'Y'): ('q1', 'Y', 'R'),  # Skip Y
        ('q2', '0'): ('q2', 'X', 'R'),  # Continue moving right over 0
        ('q2', 'X'): ('q2', 'X', 'R'),  # Continue moving right over X
        ('q2', 'Y'): ('q3', 'Y', 'R'),  # Move left over Y
        ('q3', 'Y'): ('q3', 'Y', 'R'),  # Skip Y
        ('q3', 'B'): ('q4', 'B', 'R')   # Accept if B is encountered after Y
    },
    initial_state='q0',
    accept_states={'q4'},
    reject_states={'q5'}
)

#import matplotlib.pyplot as plt
#from IPython.display import display, clear_output
import time


def clear_output(*ignored_args, **ignored_kwargs):
    pass


class TuringMachineVisualizer:
    def __init__(self, turing_machine):
        self.tm = turing_machine
        self.steps = []

    def visualize_step(self, tape, head_position, current_state):
        # Add a step to the list for visualization
        self.steps.append((tape, head_position, current_state))

    def display_steps(self):
        for step, (tape, head_position, current_state) in enumerate(self.steps):
            # Display the tape as an array
            tape_str = ' '.join(tape)
            head_position_str = ' ' * (2 * head_position) + '^'

            # Display current state and step number
            state_step_info = f"State: {current_state} | Step: {step + 1}"

            # Print the visualization
            print(tape_str)
            print(head_position_str)
            print(state_step_info)
            print('-' * (2 * len(tape) + 1))  # Separator line
            time.sleep(1)  # Pause for a short duration to visualize each step
            clear_output(wait=True)

    def run_and_visualize(self, input_string, max_steps=10):
        clear_output(wait=True) # clear first output of getting user input
        # Reset visualization steps
        self.steps = []

        if not self.tm.contains_chars(input_string, self.tm.alphabet):
            print("input string contains char not from the alphabet.")
            return


        # Run the Turing machine and capture visualization steps for a limited number of steps
        for step in range(max_steps):
            # tape, head_position, current_state = self.tm.run_step(input_string)
            if step == 0: ## @@@@@@@@@@@@@@@@@@@@@@@@2222 why are there cases?
              tape = input_string
              head_position = 0
              current_state = self.tm.initial_state
            elif step == 1:
              tape, head_position, current_state = self.tm.run_step(list(input_string), 0, self.tm.initial_state)
            else:
              tape, head_position, current_state = self.tm.run_step(list(tape), head_position, current_state)

            tape = ''.join(tape)


            ## @@@@@@@@@@@@@@@@@@@@@@@22 if i am in accept or reject it will visualize twice, here and in line 381
            if(current_state in self.tm.accept_states):
              self.visualize_step(tape, head_position, current_state)
              # time.sleep(0.5)  # Pause for a short duration to visualize each step
              # print("reached accept state")
              break
            if(current_state in self.tm.reject_states):
              self.visualize_step(tape, head_position, current_state)
              # time.sleep(0.5)  # Pause for a short duration to visualize each step
              # print("reached reject state")
              break

            #tape = "11111"
            #head_position = 1
            #current_state = 'q2'
            self.visualize_step(tape, head_position, current_state)

          # Display the visualization steps
        self.display_steps()

        # stop if reached acc or rej state
        if current_state in self.tm.accept_states:
          print("reached accept state")
          #break
        elif current_state in self.tm.reject_states:
          print("reached reject state")
          #break
        else:
            print("turing machine stoped before finishing the run on the given input")
          # # Prompt the user to continue or stop
          # user_input = input("Press Enter to continue or type 'stop' to end: ")
          # if user_input.lower() == 'stop':
          #     break






    # step by step implementation
    def run_and_visualize_step_by_step(self, input_string, max_steps=10):
        clear_output(wait=True) # clear first output of getting user input
        # Reset visualization steps
        self.steps = []

        if not self.tm.contains_chars(input_string, self.tm.alphabet):
            print("input string contains char not from the alphabet.")
            return

        # Run the Turing machine and capture visualization steps for a limited number of steps
        for step in range(max_steps):
            # tape, head_position, current_state = self.tm.run_step(input_string)
            if step == 0:
              tape = input_string
              head_position = 0
              current_state = self.tm.initial_state
            elif step == 1:
              tape, head_position, current_state = self.tm.run_step(list(input_string), 0, self.tm.initial_state)
            else:
              tape, head_position, current_state = self.tm.run_step(list(tape), head_position, current_state)

            tape = ''.join(tape)



            if(current_state in self.tm.accept_states):
              self.visualize_step(tape, head_position, current_state)
              # time.sleep(0.5)  # Pause for a short duration to visualize each step
              # print("reached accept state")
              break
            if(current_state in self.tm.reject_states):
              self.visualize_step(tape, head_position, current_state)
              # time.sleep(0.5)  # Pause for a short duration to visualize each step
              # print("reached reject state")
              break

            #tape = "11111"
            #head_position = 1
            #current_state = 'q2'
            self.visualize_step(tape, head_position, current_state)

          # Display the visualization steps
        isFinished = self.display_steps_step_by_step()

        # stop if reached acc or rej state
        if isFinished:
          if current_state in self.tm.accept_states:
            print("reached accept state")
            #break
          if current_state in self.tm.reject_states:
            print("reached reject state")
        else:
            print("turing machine stoped before finishing the run on the given input")

    def display_steps_step_by_step(self):
        for step, (tape, head_position, current_state) in enumerate(self.steps):
            # Display the tape as an array
            tape_str = ' '.join(tape)
            head_position_str = ' ' * (2 * head_position) + '^'

            # Display current state and step number
            state_step_info = f"State: {current_state} | Step: {step + 1}"

            # Print the visualization
            print(tape_str)
            print(head_position_str)
            print(state_step_info)
            print('-' * (2 * len(tape) + 1))  # Separator line
            time.sleep(1)  # Pause for a short duration to visualize each step

            # Prompt the user to continue or stop
            user_input = input("Press Enter to continue or type 'stop' to end: ")
            if user_input.lower() == 'stop':
                return 0
                break

            clear_output(wait=True)
        return 1
# Example usage:

# Assuming you have defined a Turing machine (tm) and added it to the library

# Create an instance of the Turing machine visualizer
#visualizer = TuringMachineVisualizer(tm1) # Example 1
visualizer = TuringMachineVisualizer(anbn_turing_machine) # Example 2


# Prompt the user for input string
input_string = input("Enter the input string: ")

# Run and visualize the Turing machine on the given input for a specified number of steps
visualizer.run_and_visualize(input_string) # option 1 -> max steps is not passed as argument to function then set it to initial max steps=10
#visualizer.run_and_visualize(input_string, 20) #option 2 -> also give function max steps to run turing machine on

# todo: fix visualizing steps to first calculate all step and then to show animation bassed on user input
# todo: implement combined turing machine behavior and run and test on two turing machines with input and see if it works
# Prompt the user for input string
input_string = input("Enter the input string: ")
# Run and visualize the Turing machine step by step
visualizer.run_and_visualize_step_by_step(input_string)

class CombinedTuringMachine:
    def __init__(self):
        self.turing_machines_names = []
        self.turing_machines = []

    def myshit(self):
        print("my shit")
    def add(self, new_turing_machine_name, new_turing_machine):
        self.turing_machines.append(new_turing_machine)
        self.turing_machines_names.append(new_turing_machine_name)

    def run(self, input_str):
        result_tm = input_str
        head_position = 0
        for tm in self.turing_machines:
            # Run the first Turing machine initially
            result_tm , state_tm, head_position = tm.run_combined(result_tm, head_position)

            if(state_tm in tm.accept_states):
                print("turing machine: "+self.turing_machines_names[self.turing_machines.index(tm)] +" halted on accepeted state")
                continue
            elif(state_tm in tm.reject_states):
              print("turing machine: "+self.turing_machines_names[self.turing_machines.index(tm)] +" halted on rejected state")
              return result_tm, False
            # todo: cunstruct another function of run for combined turing machines that will also return the head position, and then run the next turing machine
            # with the resulted tape values from tm_privious with the resulted head position and initial state of tm_next

            # Switch to the second Turing machine
            # Run the second Turing machine with the tape contents and head position of T1

        return result_tm, True

    def run_while_my_tm_condition(self, input_str, turing_machine_condition):
        head_position = 0
        result_combined = input_str
        continue_this = True
        output, accepted = turing_machine_condition.run(result_combined)
        while continue_this and accepted:
            result_combined, continue_this, head_position = self.run_while_my_condition(result_combined, head_position)
            output, accepted = turing_machine_condition.run(result_combined)
        return output


    def run_while_my_condition(self, input_str, head_position):
        result_tm = input_str
        # head_position = 0
        for tm in self.turing_machines:
            # Run the first Turing machine initially
            result_tm , state_tm, head_position = tm.run_combined(result_tm, head_position)

            # # delete these prints later
            # print("-------------")
            # print(str(result_tm) + " | " + str(state_tm) + " | " + str(head_position))
            # print("-------------")

            if(state_tm in tm.accept_states):
                print("turing machine: "+self.turing_machines_names[self.turing_machines.index(tm)] +" halted on accepeted state")
                continue
            elif(state_tm in tm.reject_states):
              print("turing machine: "+self.turing_machines_names[self.turing_machines.index(tm)] +" halted on rejected state")
              return result_tm, False, head_position
            # todo: cunstruct another function of run for combined turing machines that will also return the head position, and then run the next turing machine
            # with the resulted tape values from tm_privious with the resulted head position and initial state of tm_next

            # Switch to the second Turing machine
            # Run the second Turing machine with the tape contents and head position of T1

        return result_tm, True, head_position

# Example usage
# https://cstaleem.com/turing-machine-for-0n1n
step1 = TuringMachine(
    states={'q0', 'q1', 'q2'},
    alphabet={'0', '1'},
    tape_symbols={'0', '1', 'X', 'Y', 'B'},
    blank='B',
    transitions={
        ('q0', '0'): ('q2', 'X', 'R'),  # Step 1 change 0 to X
        ('q0', '1'): ('q3', '1', 'S'),
        ('q0', 'X'): ('q3', 'X', 'S'),
        ('q0', 'Y'): ('q3', 'Y', 'S'),
        ('q0', 'B'): ('q3', 'B', 'S')
    },
    initial_state='q0',
    accept_states={'q2'},
    reject_states={'q3'}
)

step2 = TuringMachine(
    states={'q0', 'q1', 'q2'},
    alphabet={'0', '1'},
    tape_symbols={'0', '1', 'X', 'Y', 'B'},
    blank='B',
    transitions={
        ('q0', '0'): ('q0', '0', 'R'),  # Step 2 move right to the first 1
        ('q0', '1'): ('q2', '1', 'S'),  # if you do not find symbol 1, reject the language
        ('q0', 'X'): ('q0', 'X', 'R'),
        ('q0', 'Y'): ('q0', 'Y', 'R'),
        ('q0', 'B'): ('q3', 'B', 'S')
    },
    initial_state='q0',
    accept_states={'q2'},
    reject_states={'q3'}
)

step3 = TuringMachine(
    states={'q0', 'q1', 'q2'},
    alphabet={'0', '1'},
    tape_symbols={'0', '1', 'X', 'Y', 'B'},
    blank='B',
    transitions={
        ('q0', '0'): ('q3', '0', 'S'),  # Step 3 change 1 to Y
        ('q0', '1'): ('q2', 'Y', 'L'),
        ('q0', 'X'): ('q3', 'X', 'S'),
        ('q0', 'Y'): ('q3', 'Y', 'S'),
        ('q0', 'B'): ('q3', 'B', 'S')
    },
    initial_state='q0',
    accept_states={'q2'},
    reject_states={'q3'}
)

step4 = TuringMachine(
    states={'q0', 'q1', 'q2'},
    alphabet={'0', '1'},
    tape_symbols={'0', '1', 'X', 'Y', 'B'},
    blank='B',
    transitions={
        ('q0', '0'): ('q0', '0', 'L'),  # Step 4 Move Left to Leftmost 0
        ('q0', '1'): ('q3', '1', 'S'),
        ('q0', 'X'): ('q2', 'X', 'R'),
        ('q0', 'Y'): ('q0', 'Y', 'L'),
        ('q0', 'B'): ('q3', 'B', 'R')
    },
    initial_state='q0',
    accept_states={'q2'},
    reject_states={'q3'}
)

#step 5 repeat steps number 01 to 04 until no more 0 and 1 remain in the input tape

step6 = TuringMachine(
    states={'q0', 'q1', 'q2'},
    alphabet={'0', '1'},
    tape_symbols={'0', '1', 'X', 'Y', 'B'},
    blank='B',
    transitions={
        ('q0', '0'): ('q3', '0', 'S'),  # Step 6 check if all turing machine tape is X and Y ( there is no 1 and 0 left on the tape)
        ('q0', '1'): ('q3', '1', 'S'),
        ('q0', 'X'): ('q0', 'X', 'R'),
        ('q0', 'Y'): ('q0', 'Y', 'R'),
        ('q0', 'B'): ('q2', 'B', 'S')
    },
    initial_state='q0',
    accept_states={'q2'},
    reject_states={'q3'}
)

combined_tm = CombinedTuringMachine()
combined_tm.add('step1', step1)
combined_tm.add('step2', step2)
combined_tm.add('step3', step3)
combined_tm.add('step4', step4)

input_str = input("Enter the input string: ")

head_position = 0 # initial head position is 0
result_combined, continue_this, head_position = combined_tm.run_while_my_condition(input_str, head_position)

# print("result Combined")
# print(result_combined)
# print("continue this")
# print(continue_this)


# note this while condition is equal to the other while condition
#while continue_this and ('1' in result_combined or '0' in result_combined): # step 5 example
output, accepted = step6.run(result_combined)
while continue_this and not accepted: # step 5 example
    result_combined, continue_this, head_position = combined_tm.run_while_my_condition(result_combined, head_position)
    output, accepted = step6.run(result_combined)

output, accepted = step6.run(result_combined)

print("steps 1 to 5 results")
print(f"Input: {input_str}")
print(f"Combined Result, continue_this: {result_combined, continue_this}")



print("step 6 result")
# Display the result
print("Result:", output)
print("Accepted:", accepted)

#example input: 000000000000111111111111


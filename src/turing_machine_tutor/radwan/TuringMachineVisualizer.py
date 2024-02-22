import time
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
##diojdsiojsfodsfjsdffdsdsfdfdsfdsoi
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
class CombinedTuringMachine:
    def __init__(self):
        self.turing_machines_names = []
        self.turing_machines = []



    def add(self, new_turing_machine_name, new_turing_machine):
        self.turing_machines.append(new_turing_machine)
        self.turing_machines_names.append(new_turing_machine_name)

    def run(self, input_str,head_position):
        result_tm = input_str
        first_step_is_over_flag = 0
        machine_run_state=None
        for tm in self.turing_machines:
            # Run the first Turing machine initially
            try:
                if first_step_is_over_flag==0:
                    tm.current_machine_state.head_position=head_position
                    machine_run_state = tm.run(result_tm)
                    first_step_is_over_flag=1
                else:
                    tm.current_machine_state.head_position=machine_run_state.head_position
                    result_tm = machine_run_state.tape.copy()
                    machine_run_state = tm.run(result_tm)
            except Exception as e:
                raise (e)

            if (machine_run_state.state in tm.accept_states):
                continue
            elif (machine_run_state.state in tm.reject_states):
                raise Exception("turing machine:  "+self.turing_machines_names[self.turing_machines.index(tm)] + " halted on rejected state")

        return machine_run_state

    def run_while_my_tm_condition(self, input_str, turing_machine_condition):
        head_position = 0
        result_combined = input_str
        continue_this = True
        output, accepted = turing_machine_condition.run(result_combined)
        while continue_this and accepted:
            result_combined, continue_this, head_position = self.run_while_my_condition(result_combined, head_position)
            output, accepted = turing_machine_condition.run(result_combined)
        return output


    def run_while_my_condition(self, tape, head_position):
        result_tm = tape.tape_symbols
        steps=list()
        # head_position = 0
        for tm in self.turing_machines:
            # Run the first Turing machine initially
            machine_run_state = tm.run_combined(result_tm, head_position)

            if(machine_run_state.state in tm.accept_states):
                ##print("turing machine: "+self.turing_machines_names[self.turing_machines.index(tm)] +" halted on accepeted state")
                steps.append("turing machine: "+self.turing_machines_names[self.turing_machines.index(tm)] +" halted on accepeted state")
                continue
            elif(machine_run_state.state in tm.reject_states):
              ##print("turing machine: "+self.turing_machines_names[self.turing_machines.index(tm)] +" halted on rejected state")
              steps.append("turing machine: "+self.turing_machines_names[self.turing_machines.index(tm)] +" halted on rejected state")
              return steps
            # todo: cunstruct another function of run for combined turing machines that will also return the head position, and then run the next turing machine
            # with the resulted tape values from tm_privious with the resulted head position and initial state of tm_next

            # Switch to the second Turing machine
            # Run the second Turing machine with the tape contents and head position of T1

        return steps
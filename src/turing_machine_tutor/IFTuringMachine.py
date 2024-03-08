import TuringMachine

class IFTuringMachine:
    def __init__(self):
        self.name = ""
        self.ifTm = None
        #self.ifName = ""
        self.thenTm = None
        #self.thenName = ""
        self.elseTm = None
        #self.elseName = ""

    def setIfTM(self, tm, name):
        self.ifTm = tm
        self.ifTm.name = name
        #self.ifName = name
    def setThenTM(self, tm, name):
        self.thenTm = tm
        self.thenTm.name = name
        #self.thenName = name
    def setElseTM(self, tm, name):
        self.elseTm = tm
        self.elseTm.name = name
        #self.elseName = name

    def run(self, input_str):
        # first run ifTm
        machine_run_state = self.ifTm.run(input_str)
        if (machine_run_state.state in self.ifTm.accept_states):
            # then run thenTm
            machine_run_state = self.thenTm.run(input_str)
            return machine_run_state
        else:
            # else run elseTm
            machine_run_state = self.elseTm.run(input_str)
            return machine_run_state
        
    
        
class Machine_Run_State:
    def __init__(self, tape,head_position ,state):
        self.tape=tape   ## type is Tape
        self.head_position = head_position  ## type is int
        self.state = state  ## type is State




    def try_me(self,function):

        return function(1)




    def write_to_tape(self, config):
        if 0 <= self.head_position < len(self.tape):
            self.tape[self.head_position] = config.symbol
        elif config.action == 'R':
            self.tape.append(config.symbol)
            self.head_position += 1
            if self.head_position == len(self.tape):
                self.tape.append("B")
        elif config.action == 'L':
            self.tape.insert(0, config.symbol)
            self.head_position -= 1
            if self.head_position < 0:  ##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ this isn't illegal? if the head is on 0 and the transition says to move left this means the turing machine is incorrect isn't it?
                self.tape.insert(0, "B")



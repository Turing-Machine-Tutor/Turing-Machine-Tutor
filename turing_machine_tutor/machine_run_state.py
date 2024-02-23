class Machine_Run_State:
    def __init__(self, tape,head_position ,state):
        self.tape=tape   ## type is Tape
        self.head_position = head_position  ## type is int
        self.state = state  ## type is State



    def try_me(self,function):

        return function(1)

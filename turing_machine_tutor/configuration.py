class Configuration:
    def __init__(self, tape, head_position,state):
        self.tape=tape   ## type is Tape
        self.head_position=head_position ## type is int
        self.state = state  ## type is State

    def get_head_position(self):
        return self.head_position

    def get_state(self):
        return self.state

    def get_tape(self):
        return self.tape

    def try_me(self,function):

        return function(1)


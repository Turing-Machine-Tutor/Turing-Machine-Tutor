class Configuration:
    def __init__(self, tape, new_symbol,state,head_position):
        self.tape=tape   ## type is Tape
        self.symbol=new_symbol ## symbol is string - one char
        self.state = state  ## type is State

        self.head_position = head_position  ## type is int


    def try_me(self,function):

        return function(1)


class Configuration:
    def __init__(self, state, new_symbol,action):
        self.state = state  ## type is State
        self.symbol=new_symbol ## symbol is string - one char
        self.action=action ## Action is string - one char L,R,S





    def try_me(self,function):

        return function(1)


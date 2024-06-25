class Call_Turing_Machine:
    def __init__(self, TM_name, tm, list_of_tapes_indexes, return_state):
        self.TM_name = TM_name  ## type is State
        self.tm = tm
        self.list_of_tapes_indexes=list_of_tapes_indexes ## symbol is string - one char
        #self.call_state=call_state ## Action is string - one char L,R,S
        self.return_state = return_state
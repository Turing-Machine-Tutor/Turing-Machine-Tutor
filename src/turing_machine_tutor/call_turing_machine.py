class call_turing_machine:
    def __init__(self, TM_name,list_of_tapes_indexes,call_state,return_state):
        self.TM_name = TM_name
        self.list_of_tapes_indexes=list_of_tapes_indexes
        self.call_state=call_state
        self.return_state = return_state
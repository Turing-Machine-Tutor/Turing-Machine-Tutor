class Challenge:
    def __init__(self, name ,turing_machine_description, function_that_accepts_the_language_of_tm, edge_cases_list):
        if(name == None or name == ""):
                raise Exception("Name cannot be None")
        if(not isinstance(name, str)):
            raise Exception("Name cannot be not str object")
        if(turing_machine_description == None or turing_machine_description == ""):
            raise Exception("turing_machine_description cannot be None")
        if(not isinstance(turing_machine_description, str)):
            raise Exception("turing_machine_description cannot be not str object")
        if(function_that_accepts_the_language_of_tm == None):
            raise Exception("func cannot be None")
        if(not callable(function_that_accepts_the_language_of_tm)):
            raise Exception("func cannot be not function object")
        try:
            if(not isinstance(function_that_accepts_the_language_of_tm(""),bool)):
                raise Exception()
        except Exception as e:
            raise Exception("func cannot be function object that doesnt get string input and output True/False (boolean)")
        is_all_strings = lambda my_list: all(isinstance(item, str) and len(item) >= 1 for item in my_list)
        if(edge_cases_list == None):
            raise Exception("edge_cases_list cannot be None")
        if((not isinstance(edge_cases_list, (list,set))) or not is_all_strings(edge_cases_list)):
            raise Exception("edge_cases_list cannot contain a non string object")
        
        self.name = name
        self.description=turing_machine_description
        self.function=function_that_accepts_the_language_of_tm
        self.edge_cases=edge_cases_list

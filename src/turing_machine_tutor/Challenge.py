import ast
import inspect

class Challenge:
    def __init__(self, name, input_alphabet ,turing_machine_description, function_that_accepts_the_language_of_tm, edge_cases_list):
        is_all_strings_of_len1 = lambda my_list: all(isinstance(item, str) and len(item) == 1 for item in my_list)

        if(name == None or name == ""):
                raise Exception("Name cannot be None")
        if(not isinstance(name, str)):
            raise Exception("Name cannot be not str object")
        if(input_alphabet == None or len(input_alphabet) == 0 or (not isinstance(input_alphabet, (list,set))) or (not is_all_strings_of_len1(input_alphabet))):
                raise Exception("input_alphabet cannot be None / empty list, and must be all string in list of len = 1")
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
            str_msg = self.validateFuncReturnOnlyBool(function_that_accepts_the_language_of_tm)
            if(len(str_msg) > 0):
                raise Exception("found error in func at line value: "+str_msg+" , func should return only True/False")
        except Exception as e:
            if(len(str(e)) > 0 and "found error in func at line value: " in str(e)):
                raise e
            else:
                raise Exception("func cannot be function object that doesnt get string input and output True/False (boolean)")
        is_all_strings = lambda my_list: all(isinstance(item, str) and len(item) >= 1 for item in my_list)
        if(edge_cases_list == None):
            raise Exception("edge_cases_list cannot be None")
        if((not isinstance(edge_cases_list, (list,set))) or not is_all_strings(edge_cases_list)):
            raise Exception("edge_cases_list cannot contain a non string object")
        
        self.name = name
        self.input_alphabet = set(input_alphabet)
        self.description=turing_machine_description
        self.function=function_that_accepts_the_language_of_tm
        self.edge_cases=edge_cases_list

        self.mustPass = None
        self.mustFail = None

    def get_input_alphabet(self):
        if(self.input_alphabet == None):
            raise Exception("Cannot get input alphabet, please construct the challenge first")
        return self.input_alphabet
        
    def MustPass(self, pass_list):
        is_all_strings = lambda my_list: all(isinstance(item, str) and len(item) >= 1 for item in my_list)
        if(pass_list == None):
            raise Exception("pass_list cannot be None")
        if((not isinstance(pass_list, (list,set))) or not is_all_strings(pass_list)):
            raise Exception("pass_list cannot contain a non string object")

        for l in pass_list:
            if(self.function(l) == False):
                raise Exception("the word: "+str(l)+", return false instead of true with the challege's fucntion.")
        self.mustPass = pass_list

    def MustFail(self, fail_list):
        is_all_strings = lambda my_list: all(isinstance(item, str) and len(item) >= 1 for item in my_list)
        if(fail_list == None):
            raise Exception("fail_list cannot be None")
        if((not isinstance(fail_list, (list,set))) or not is_all_strings(fail_list)):
            raise Exception("fail_list cannot contain a non string object")

        for l in fail_list:
            if(self.function(l) == False):
                raise Exception("the word: "+str(l)+", return true instead of false with the challege's fucntion.")
        self.mustFail = fail_list


    def validateFuncReturnOnlyBool(self, func):
        # Get the source code of the function
        source_lines, _ = inspect.getsourcelines(func)
        source_code = ''.join(source_lines)

        # Parse the source code into an AST (Abstract Syntax Tree)
        tree = ast.parse(source_code)

        # Extract return statements from the AST
        for node in ast.walk(tree):
            if isinstance(node, ast.Return):
                # Get the value of the return statement if it exists
                if node.value is not None:
                    return_stmt = ast.unparse(node).strip()
                    if return_stmt not in ["return True", "return False"]:
                        return return_stmt
                else:
                    return "return"  # Empty return statement

        return ""  # All return statements are valid
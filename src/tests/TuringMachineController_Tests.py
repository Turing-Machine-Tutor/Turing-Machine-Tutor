import os
import sys
# Add the parent directory of mypackage to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from turing_machine_tutor.TuringMachine import TuringMachine
from turing_machine_tutor.CombinedTuringMachine import CombinedTuringMachine
from turing_machine_tutor.machine_run_state import Machine_Run_State
from turing_machine_tutor.configuration import Configuration
from turing_machine_tutor.IFTuringMachine import IFTuringMachine
from turing_machine_tutor.TuringMachineController import TuringMachineController
import unittest
# Purpose: Verify that individual units of code (functions, methods, or classes) work as intended.


class TestTuringMachineController(unittest.TestCase):
    # test TM Controller add_turing_machine function
    def test_TuringMachineController_Add_WithNotValid1TM(self):
        notValid_list = [None, "", [], 5, 'asd']
        for n_v in notValid_list:
            try:
                result = TuringMachineController()
                result.add_turing_machine("test", n_v)
            except Exception as e:
                if n_v == None:
                    self.assertEqual("TM cannot be None", str(e))
                else:
                    self.assertEqual("TM cannot be Not (TuringMachine / IFTuringMachine / CombinedTuringMachine) Object", str(e))
    ###############################################################################################################
    # test TM Controller add_turing_machine function
    def test_TuringMachineController_Add_WithNotValid2TM(self):
        step1 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Configuration('q2', 'X', 'R'),  # Step 1 change 0 to X
                ('q0', '1'): Configuration('q3', '1', 'S'),
                ('q0', 'X'): Configuration('q3', 'X', 'S'),
                ('q0', 'Y'): Configuration('q3', 'Y', 'S'),
                ('q0', 'B'): Configuration('q3', 'B', 'S')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )
        notValid_list = [None, "", '']
        for n_v in notValid_list:
            try:
                result = TuringMachineController()
                result.add_turing_machine(n_v, step1)
            except Exception as e:
                self.assertEqual("Name cannot be None", str(e))
    ###############################################################################################################
    # test Combined TM add function
    def test_TuringMachineController_Add_WithNotValid3TM(self):
        step1 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Configuration('q2', 'X', 'R'),  # Step 1 change 0 to X
                ('q0', '1'): Configuration('q3', '1', 'S'),
                ('q0', 'X'): Configuration('q3', 'X', 'S'),
                ('q0', 'Y'): Configuration('q3', 'Y', 'S'),
                ('q0', 'B'): Configuration('q3', 'B', 'S')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )
        notValid_list = [5, [55], {5}]
        for n_v in notValid_list:
            try:
                result = TuringMachineController()
                result.add_turing_machine(n_v, step1)
            except Exception as e:
                self.assertEqual("Name cannot be not str object", str(e))
    ###############################################################################################################
    # test Combined TM add function
    def test_TuringMachineController_Add_WithNotValid4TM(self):
        step1 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Configuration('q2', 'X', 'R'),  # Step 1 change 0 to X
                ('q0', '1'): Configuration('q3', '1', 'S'),
                ('q0', 'X'): Configuration('q3', 'X', 'S'),
                ('q0', 'Y'): Configuration('q3', 'Y', 'S'),
                ('q0', 'B'): Configuration('q3', 'B', 'S')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )
        notValid_list = ["add1", "add1"]
        for n_v in notValid_list:
            try:
                result = TuringMachineController()
                result.add_turing_machine(n_v, step1)
            except Exception as e:
                self.assertEqual("Turing machine with this name already exists in the dict", str(e))
    ###############################################################################################################


    # test TuringMachineController function
    def test_TuringMachineController_Remove_WithNotValid1TM(self):
        notValid_list = [None, ""]
        for n_v in notValid_list:
            try:
                result = TuringMachineController()
                result.remove(n_v)
            except Exception as e:
                self.assertEqual("Name cannot be None", str(e))
    ###############################################################################################################
    # test TuringMachineController remove function
    def test_TuringMachineController_Remove_WithNotValid2TM(self):
        notValid_list = [5, [5], {"55"}]
        for n_v in notValid_list:
            try:
                result = TuringMachineController()
                result.remove(n_v)
            except Exception as e:
                self.assertEqual("Name cannot be not str object", str(e))
    ###############################################################################################################
    # test TuringMachineController remove function
    def test_TuringMachineController_Remove_WithNotValid3TM(self):
        notValid_list = ["test1", "test2", "a"]
        for n_v in notValid_list:
            try:
                result = TuringMachineController()
                result.remove(n_v)
            except Exception as e:
                self.assertEqual("Turing machine with this name doesn't exists in the dict", str(e))
    ###############################################################################################################
    # test TuringMachineController remove function
    def test_TuringMachineController_Remove_ValidTM(self):
        step1 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Configuration('q2', 'X', 'R'),  # Step 1 change 0 to X
                ('q0', '1'): Configuration('q3', '1', 'S'),
                ('q0', 'X'): Configuration('q3', 'X', 'S'),
                ('q0', 'Y'): Configuration('q3', 'Y', 'S'),
                ('q0', 'B'): Configuration('q3', 'B', 'S')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )
        Valid_list = ["test1"]
        for v in Valid_list:
            try:
                result = TuringMachineController()
                result.add_turing_machine(v,step1)
                result.remove(v)
            except Exception as e:
                self.fail("remove should succeded, shouldn't throw exception")
    ###############################################################################################################
    # test TuringMachineController get function
    def test_TuringMachineController_Get_ValidTM(self):
        step1 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Configuration('q2', 'X', 'R'),  # Step 1 change 0 to X
                ('q0', '1'): Configuration('q3', '1', 'S'),
                ('q0', 'X'): Configuration('q3', 'X', 'S'),
                ('q0', 'Y'): Configuration('q3', 'Y', 'S'),
                ('q0', 'B'): Configuration('q3', 'B', 'S')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )
        Valid_list = ["test1"]
        for v in Valid_list:
            try:
                result = TuringMachineController()
                result.add_turing_machine(v,step1)
                self.assertEqual(result.get_turing_machine(v),step1) 
            except Exception as e:
                self.fail("remove should succeded, shouldn't throw exception")
    ###############################################################################################################
    # test TuringMachineController get function
    def test_TuringMachineController_Get_NotValidTM1(self):
        step1 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Configuration('q2', 'X', 'R'),  # Step 1 change 0 to X
                ('q0', '1'): Configuration('q3', '1', 'S'),
                ('q0', 'X'): Configuration('q3', 'X', 'S'),
                ('q0', 'Y'): Configuration('q3', 'Y', 'S'),
                ('q0', 'B'): Configuration('q3', 'B', 'S')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )
        notValid_list = [None, ""]
        result = TuringMachineController()
        result.add_turing_machine("test1",step1)
        for n_v in notValid_list:
            try:
                result.get_turing_machine(n_v) 
            except Exception as e:
                self.assertEqual("Name cannot be None", str(e))
    ###############################################################################################################
    # test TuringMachineController get function
    def test_TuringMachineController_Get_NotValidTM2(self):
        step1 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Configuration('q2', 'X', 'R'),  # Step 1 change 0 to X
                ('q0', '1'): Configuration('q3', '1', 'S'),
                ('q0', 'X'): Configuration('q3', 'X', 'S'),
                ('q0', 'Y'): Configuration('q3', 'Y', 'S'),
                ('q0', 'B'): Configuration('q3', 'B', 'S')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )
        notValid_list = [5, [5], {"55"}]
        result = TuringMachineController()
        result.add_turing_machine("test1",step1)
        for n_v in notValid_list:
            try:
                result.get_turing_machine(n_v) 
            except Exception as e:
                self.assertEqual("Name cannot be not str object", str(e))
    ###############################################################################################################
    # test TuringMachineController get function
    def test_TuringMachineController_Get_NotValidTM3(self):
        step1 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Configuration('q2', 'X', 'R'),  # Step 1 change 0 to X
                ('q0', '1'): Configuration('q3', '1', 'S'),
                ('q0', 'X'): Configuration('q3', 'X', 'S'),
                ('q0', 'Y'): Configuration('q3', 'Y', 'S'),
                ('q0', 'B'): Configuration('q3', 'B', 'S')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )
        notValid_list = ["test1", "test2", "a"]
        result = TuringMachineController()
        result.add_turing_machine("test0",step1)
        for n_v in notValid_list:
            try:
                result.get_turing_machine(n_v) 
            except Exception as e:
                self.assertEqual("Turing machine with this name doesn't exists in the dict", str(e))
     ###############################################################################################################
    # test TuringMachineController run function with TuringMachine object
    def test_TuringMachineController_Run_withValidTuringMachine(self):
        try:
            TM1 = TuringMachine(
            states={'q0', 'q1', 'q2'},
            input_alphabet={'0', '1'},
            tape_symbols={'0', '1', 'B'},
            transitions={
                ('q0', '0'): Configuration('q0', '0', 'R'),  
                ('q0', '1'): Configuration('q0', '0', 'R'),
                ('q0', 'B'): Configuration('q1', 'B', 'R')
            },
            initial_state='q0',
            accept_states={'q1'},
            reject_states={'q2'}
            )
            result = TuringMachineController()
            result.add_turing_machine("test", TM1)
            res = result.run_turing_machine("test", "001").tape
            res = ''.join(res)
            res = res.replace('B','')
            self.assertEqual(res, "000")
        except Exception as e:
            self.fail("TuringMachine() raised Exception: "+str(e)+", with valid TuringMachine and valid input unexpectedly!")
    
                
     ###############################################################################################################
    # test TuringMachineController run function with IFTuringMachine object
    def test_TuringMachineController_Run_withValidIFTuringMachine(self):
        ifTm = TuringMachine( # condition if input legth is less than 4 accept else reject
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'},
    input_alphabet={'0', '1'},
    tape_symbols={'0', '1', 'B'},
    transitions={
        ('q0', '0'): Configuration('q1', '0', 'R'),  
        ('q0', '1'): Configuration('q1', '1', 'R'),

        ('q1', '0'): Configuration('q2', '0', 'R'),
        ('q1', '1'): Configuration('q2', '1', 'R'),

        ('q2', '0'): Configuration('q3', '0', 'R'),  
        ('q2', '1'): Configuration('q3', '0', 'R'),
        
        ('q3', '0'): Configuration('q6', '0', 'R'),
        ('q3', '1'): Configuration('q6', '1', 'R'),
        ('q3', 'B'): Configuration('q5', 'B', 'S')
    },
    initial_state='q0',
    accept_states={'q5'},
    reject_states={'q6'}
)
        
        thenTm = TuringMachine( # condition if input legth is less than 4 change every 1 to 0
    states={'q0', 'q1', 'q2'},
    input_alphabet={'0', '1'},
    tape_symbols={'0', '1', 'B'},
    transitions={
        ('q0', '0'): Configuration('q0', '0', 'R'),  
        ('q0', '1'): Configuration('q0', '0', 'R'),
        ('q0', 'B'): Configuration('q1', 'B', 'R')
    },
    initial_state='q0',
    accept_states={'q1'},
    reject_states={'q2'}
)

        elseTm = TuringMachine( # condition if input legth is less than 4 change every 0 to 1
    states={'q0', 'q1', 'q2'},
    input_alphabet={'0', '1'},
    tape_symbols={'0', '1', 'B'},
    transitions={
        ('q0', '0'): Configuration('q0', '1', 'R'),  
        ('q0', '1'): Configuration('q0', '1', 'R'),
        ('q0', 'B'): Configuration('q1', 'B', 'R')
    },
    initial_state='q0',
    accept_states={'q1'},
    reject_states={'q2'}
)

        try:
            res = TuringMachineController()
            result = IFTuringMachine()
            result.setIfTM(ifTm, "myIf")
            result.setThenTM(thenTm,"mythen")
            result.setElseTM(elseTm,"myelse")
            res.add_turing_machine("myIFTM", result)
            self.assertEqual(''.join((res.run_turing_machine("myIFTM","001").tape)).replace('B',''),"000")
            self.assertEqual(''.join((res.run_turing_machine("myIFTM","001011").tape)).replace('B',''),"111111")
        except Exception as e:
            self.fail("TuringMachine() raised Exception: "+str(e)+", with valid TuringMachine and valid input unexpectedly!")
    
                
     ###############################################################################################################
    # test TuringMachineController run function with CombinedTuringMachine object
    def test_TuringMachineController_Run_withValidCombinedTuringMachineCombined(self):
        try:
            step1 = TuringMachine(
                states={'q0', 'q1', 'q2', 'q3'},
                input_alphabet={'0', '1', 'X', 'Y', 'B'},
                tape_symbols={'0', '1', 'X', 'Y', 'B'},
                transitions={
                    ('q0', '0'): Configuration('q2', 'X', 'R'),  # Step 1 change 0 to X
                    ('q0', '1'): Configuration('q3', '1', 'S'),
                    ('q0', 'X'): Configuration('q3', 'X', 'S'),
                    ('q0', 'Y'): Configuration('q3', 'Y', 'S'),
                    ('q0', 'B'): Configuration('q3', 'B', 'S')
                },
                initial_state='q0',
                accept_states={'q2'},
                reject_states={'q3'}
            )
            step2 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1', 'X', 'Y', 'B'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): Configuration('q0', '0', 'R'),  # Step 2 move right to the first 1
                ('q0', '1'): Configuration('q2', '1', 'S'),  # if you do not find symbol 1, reject the language
                ('q0', 'X'): Configuration('q0', 'X', 'R'),
                ('q0', 'Y'): Configuration('q0', 'Y', 'R'),
                ('q0', 'B'): Configuration('q3', 'B', 'S')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )

            step3 = TuringMachine(
                states={'q0', 'q1', 'q2', 'q3'},
                input_alphabet={'0', '1', 'X', 'Y', 'B'},
                tape_symbols={'0', '1', 'X', 'Y', 'B'},
                transitions={
                    ('q0', '0'): Configuration('q3', '0', 'S'),  # Step 3 change 1 to Y
                    ('q0', '1'): Configuration('q2', 'Y', 'L'),
                    ('q0', 'X'): Configuration('q3', 'X', 'S'),
                    ('q0', 'Y'): Configuration('q3', 'Y', 'S'),
                    ('q0', 'B'): Configuration('q3', 'B', 'S')
                },
                initial_state='q0',
                accept_states={'q2'},
                reject_states={'q3'}
            )

            step4 = TuringMachine(
                states={'q0', 'q1', 'q2', 'q3'},
                input_alphabet={'0', '1', 'X', 'Y', 'B'},
                tape_symbols={'0', '1', 'X', 'Y', 'B'},
                transitions={
                    ('q0', '0'): Configuration('q0', '0', 'L'),  # Step 4 Move Left to Leftmost 0
                    ('q0', '1'): Configuration('q3', '1', 'S'),
                    ('q0', 'X'): Configuration('q2', 'X', 'R'),
                    ('q0', 'Y'): Configuration('q0', 'Y', 'L'),
                    ('q0', 'B'): Configuration('q3', 'B', 'R')
                },
                initial_state='q0',
                accept_states={'q2'},
                reject_states={'q3'}
            )

            #step 5 repeat steps number 01 to 04 until no more 0 and 1 remain in the input tape
            step5 = TuringMachine(
                states={'q0', 'q1', 'q2', 'q3'},
                input_alphabet={'0', '1', 'X', 'Y', 'B'},
                tape_symbols={'0', '1', 'X', 'Y', 'B'},
                transitions={
                    ('q0', '0'): Configuration('q2', '0', 'S'),  # Step 6 check if all turing machine tape is X and Y ( there is no 1 and 0 left on the tape)
                    ('q0', '1'): Configuration('q2', '1', 'S'),
                    ('q0', 'X'): Configuration('q0', 'X', 'R'),
                    ('q0', 'Y'): Configuration('q0', 'Y', 'R'),
                    ('q0', 'B'): Configuration('q3', 'B', 'S')
                },
                initial_state='q0',
                accept_states={'q2'},
                reject_states={'q3'}
            )
            step6 = TuringMachine(
                states={'q0', 'q1', 'q2', 'q3'},
                input_alphabet={'0', '1', 'X', 'Y', 'B'},
                tape_symbols={'0', '1', 'X', 'Y', 'B'},
                transitions={
                    ('q0', '0'): Configuration('q3', '0', 'S'),  # Step 6 check if all turing machine tape is X and Y ( there is no 1 and 0 left on the tape)
                    ('q0', '1'): Configuration('q3', '1', 'S'),
                    ('q0', 'X'): Configuration('q0', 'X', 'R'),
                    ('q0', 'Y'): Configuration('q0', 'Y', 'R'),
                    ('q0', 'B'): Configuration('q2', 'B', 'S')
                },
                initial_state='q0',
                accept_states={'q2'},
                reject_states={'q3'}
            )

            combined_tm = CombinedTuringMachine()
            combined_tm.add('Change 0 to X', step1)
            combined_tm.add('Move Right To First 1', step2)
            combined_tm.add('Change 1 to Y', step3)
            combined_tm.add('Move Left to Leftmost 0', step4)
            # test without cond
            result = TuringMachineController()
            result.add_turing_machine("myCombined", combined_tm)
            res = result.run_turing_machine("myCombined", "0011")
            res = ''.join(res.tape)
            res = res.replace('B','')
            self.assertEqual(res, "X0Y1")
            # test with while cond
            result.remove("myCombined")
            combined_tm.setTuringMachineWhileCondition("0 or 1 in tape", step5)
            result.add_turing_machine("myCombined", combined_tm)
            res = result.run_turing_machine("myCombined", "0011")
            res = ''.join(res.tape)
            res = res.replace('B','')
            self.assertEqual(res, "XXYY")
            #self.assertEqual(result, "XXYY")
        except Exception as e:
            self.fail("TuringMachine() raised Exception: "+str(e)+", with valid TuringMachine and valid input unexpectedly!")    
     ###############################################################################################################
    # todo: test Visualize:  1.Normal Turing Machine, 2.IFTuringMachine, 3.TuringMachineCombined
            
    # todo: test Validate:  1.Normal Turing Machine with (Valid Func/ not Valid Func), 2.IFTuringMachine with (Valid Func/ not Valid Func), 3.TuringMachineCombined with (Valid Func/ not Valid Func)

if __name__ == '__main__':
    unittest.main()

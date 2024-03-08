import os
import sys
# Add the parent directory of mypackage to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from turing_machine_tutor.TuringMachine import TuringMachine
from turing_machine_tutor.machine_run_state import Machine_Run_State
from turing_machine_tutor.configuration import Configuration

import unittest
# Purpose: Verify that individual units of code (functions, methods, or classes) work as intended.


class TestTuringMachine(unittest.TestCase):
    # test Valid TM Constructor
    def test_TM_Constructor_withValidTuringMachine(self):
        try:
            result = TuringMachine(
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
        except Exception as e:
            self.fail("TuringMachine() raised Exception: "+e+", with valid TuringMachine input unexpectedly!")
    ###############################################################################################################
            
    # test Valid TM Constructor
    def test_TM_Constructor_withValidTuringMachine(self):
        not_valid_initial_state = [          ''       ,        None            ,    'q0']
        not_valid_states = [{'q0', 'q1', 'q2'},          {'q0', 'q1', 'q2'}    , {'q3', 'q1', 'q2'}]
        for index in range(0,2):

            try: 
                TuringMachine(
                states=not_valid_states[index],
                input_alphabet={'0', '1'},
                tape_symbols={'0', '1', 'B'},
                transitions={
                    ('q0', '0'): Configuration('q0', '0', 'R'),  
                    ('q0', '1'): Configuration('q0', '0', 'R'),
                    ('q0', 'B'): Configuration('q1', 'B', 'R')
                },
                initial_state=not_valid_initial_state[index],
                accept_states={'q1'},
                reject_states={'q2'}
                )
                self.fail("should throw exception")
            except Exception as e:
                self.assertEquals("initial_state cannot be None / empty string", str(e))

        for index in range(2,3):
            try:
                TuringMachine(
                states=not_valid_states[index],
                input_alphabet={'0', '1'},
                tape_symbols={'0', '1', 'B'},
                transitions={
                    ('q0', '0'): Configuration('q0', '0', 'R'),  
                    ('q0', '1'): Configuration('q0', '0', 'R'),
                    ('q0', 'B'): Configuration('q1', 'B', 'R')
                },
                initial_state=not_valid_initial_state[index],
                accept_states={'q1'},
                reject_states={'q2'}
                )
                self.fail("should throw exception")
            except Exception as e:
                self.assertEquals("initial state must be in states", str(e))
    ###############################################################################################################

    

    # def test_add_negative_numbers(self):
    #     result = add(-2, 3)
    #     self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
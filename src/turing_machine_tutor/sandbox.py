import os
import sys
# Add the parent directory of mypackage to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from turing_machine_tutor.CombinedTuringMachine import CombinedTuringMachine
from turing_machine_tutor.TuringMachine import TuringMachine
from turing_machine_tutor.TuringMachineController import TuringMachineController
from turing_machine_tutor.next import next
from turing_machine_tutor.IFTuringMachine import IFTuringMachine
from turing_machine_tutor.WhileTuringMachine import WhileTuringMachine
from turing_machine_tutor.ConcatenateTM import ConcatenateTM



# # def test_me(number):
# #     if number==1:
# #         return "one"
# #     if number==2:
# #         return "two"
# #     if number==3:
# #         return "three"
# #     return


# # ok=next(1,2,3)
# # print(ok.try_me(test_me))

#
# emptyString = TuringMachine(
#     states={'q0', 'q1', 'rej', 'acc'},
#     input_alphabet={'0', '1'},
#     tape_symbols={'0', '1', '_'},
#     blank = '_',
#     transitions={
#         ('q0', '0'): next('q1', '0', 'R'),
#         ('q0', '1'): next('q1', '1', 'R'),
#         ('q1', '0'): next('q0', '0', 'R'),
#         ('q1', '1'): next('q0', '1', 'R'),
#         ('q0', '_'): next('acc', '_', 'R'),
#         ('q1', '_'): next('rej', '_', 'R'),
#     },
#     initial_state='q0',
#     accept_states={'acc'},
#     reject_states={'rej'}
# )


# Create a Turing machine
# tm1 = TuringMachine(
#     states={'q0', 'q1', 'q2', 'q3'},
#     input_alphabet={'0', '1'},
#     tape_symbols={'0', '1', 'B'},
#     transitions={
#         ('q0', '0'): next('q1', '0', 'R'),
#         ('q0', '1'): next('q1', '1', 'R'),
#         ('q1', '0'): next('q0', '0', 'R'),
#         ('q1', '1'): next('q0', '1', 'R'),
#         ('q0', 'B'): next('q3', 'B', 'R'),
#         ('q1', 'B'): next('q2', 'B', 'R'),
#     },
#     initial_state='q0',
#     accept_states={'q3'},
#     reject_states={'q2'}
# )

# anbn_turing_machine = TuringMachine(
#     states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
#     input_alphabet={'0', '1'},
#     tape_symbols={'0', '1', 'X', 'Y', 'B'},
#     transitions={
#         ('q0', '0'): next('q1', 'X', 'R'),  # Move right and replace 0 with X
#         ('q1', '0'): next('q1', '0', 'R'),  # Continue moving right over 0
#         ('q1', 'Y'): next('q1', 'Y', 'R'),  # Skip Y
#         ('q1', '1'): next('q2', 'Y', 'L'),  # Move left and replace 1 with Y
#         ('q2', 'Y'): next('q2', 'Y', 'L'),  # Continue moving left over Y
#         ('q2', '0'): next('q2', '0', 'L'),  # Continue moving left over 0
#         ('q2', 'X'): next('q0', 'X', 'R'),  # Move right to find the next 0 after 1s
#         ('q0', 'Y'): next('q0', 'Y', 'R'),  # Skip Y in the process
#         ('q0', 'B'): next('q4', 'B', 'R'),   # Accept if B is encountered after checking
#         ('q0', '1'): next('q5', 'B', 'R'),
#         ('q1', 'B'): next('q5', 'B', 'L')
#     },
#     initial_state='q0',
#     accept_states={'q4'},
#     reject_states={'q5'}
# )


# controller = TuringMachineController()
# # controller.add_turing_machine('emptyString', emptyString)
# # controller.add_turing_machine('tm1',tm1)
# controller.add_turing_machine('0n1n',anbn_turing_machine)

# # # # Run the Turing machine from the library
# # # mrs= controller.run_turing_machine('tm1', '000111')
# # # print(tm1.given_state_is_in_acceptance(mrs.state))
# # # mrs= controller.run_turing_machine('0n1n', '0000011111')
# # # print(anbn_turing_machine.given_state_is_in_acceptance(mrs.state))


# def is_0n1n(input_str):
#     stack = []

#     for symbol in input_str:
#         if symbol == '0':
#             stack.append('0')
#         elif symbol == '1':
#             if not stack:
#                 return False  # There are more '1's than '0's
#             stack.pop()
#         else:
#             return False  # Invalid symbol

#     return True
# #

# controller.add_challenge("0n1n","turing machine that accepts 0n1n",is_0n1n,{"0011","01"});
# controller.add_challenge("random_shit","turing machine that accepts 0n1n",is_0n1n,{"0011","01"});
# controller.add_challenge("random_shit_2","turing machine that accepts 0n1n",is_0n1n,{"0011","01"});
# controller.get_challenges()
# # controller.validate_turing_machine('0n1n',is_0n1n,{"0011"})
# # # controller.visualize('0n1n',"01")
# # # controller.visualize_step_by_step('0n1n',"01")





# step1 = TuringMachine(
#     states={'q0', 'q1', 'q2','q3'},
#     input_alphabet={'0', '1', 'X', 'Y', 'B'},
#     tape_symbols={'0', '1', 'X', 'Y', 'B'},
#     transitions={
#         ('q0', '0'): next('q2', 'X', 'R'),  # Step 1 change 0 to X
#         ('q0', '1'): next('q3', '1', 'S'),
#         ('q0', 'X'): next('q3', 'X', 'S'),
#         ('q0', 'Y'): next('q3', 'Y', 'S'),
#         ('q0', 'B'): next('q3', 'B', 'S')
#     },
#     initial_state='q0',
#     accept_states={'q2'},
#     reject_states={'q3'}
# )

# step2 = TuringMachine(
#     states={'q0', 'q1', 'q2','q3'},
#     input_alphabet={'0', '1', 'X', 'Y', 'B'},
#     tape_symbols={'0', '1', 'X', 'Y', 'B'},
#     transitions={
#         ('q0', '0'): next('q0', '0', 'R'),  # Step 2 move right to the first 1
#         ('q0', '1'): next('q2', '1', 'S'),  # if you do not find symbol 1, reject the language
#         ('q0', 'X'): next('q0', 'X', 'R'),
#         ('q0', 'Y'): next('q0', 'Y', 'R'),
#         ('q0', 'B'): next('q3', 'B', 'S')
#     },
#     initial_state='q0',
#     accept_states={'q2'},
#     reject_states={'q3'}
# )

# step3 = TuringMachine(
#     states={'q0', 'q1', 'q2','q3'},
#     input_alphabet={'0', '1', 'X', 'Y', 'B'},
#     tape_symbols={'0', '1', 'X', 'Y', 'B'},
#     transitions={
#         ('q0', '0'): next('q3', '0', 'S'),  # Step 3 change 1 to Y
#         ('q0', '1'): next('q2', 'Y', 'L'),
#         ('q0', 'X'): next('q3', 'X', 'S'),
#         ('q0', 'Y'): next('q3', 'Y', 'S'),
#         ('q0', 'B'): next('q3', 'B', 'S')
#     },
#     initial_state='q0',
#     accept_states={'q2'},
#     reject_states={'q3'}
# )

# step4 = TuringMachine(
#     states={'q0', 'q1', 'q2','q3'},
#     input_alphabet={'0', '1', 'X', 'Y', 'B'},
#     tape_symbols={'0', '1', 'X', 'Y', 'B'},
#     transitions={
#         ('q0', '0'): next('q0', '0', 'L'),  # Step 4 Move Left to Leftmost 0
#         ('q0', '1'): next('q3', '1', 'S'),
#         ('q0', 'X'): next('q2', 'X', 'R'),
#         ('q0', 'Y'): next('q0', 'Y', 'L'),
#         ('q0', 'B'): next('q3', 'B', 'R')
#     },
#     initial_state='q0',
#     accept_states={'q2'},
#     reject_states={'q3'}
# )

# #step 5 repeat steps number 01 to 04 until no more 0 and 1 remain in the input tape
# step5 = TuringMachine(
#     states={'q0', 'q1', 'q2','q3'},
#     input_alphabet={'0', '1', 'X', 'Y', 'B'},
#     tape_symbols={'0', '1', 'X', 'Y', 'B'},
#     transitions={
#         ('q0', '0'): next('q2', '0', 'S'),  # Step 6 check if all turing machine tape is X and Y ( there is no 1 and 0 left on the tape)
#         ('q0', '1'): next('q2', '1', 'S'),
#         ('q0', 'X'): next('q0', 'X', 'R'),
#         ('q0', 'Y'): next('q0', 'Y', 'R'),
#         ('q0', 'B'): next('q3', 'B', 'S')
#     },
#     initial_state='q0',
#     accept_states={'q2'},
#     reject_states={'q3'}
# )
# step6 = TuringMachine(
#     states={'q0', 'q1', 'q2','q3'},
#     input_alphabet={'0', '1', 'X', 'Y', 'B'},
#     tape_symbols={'0', '1', 'X', 'Y', 'B'},
#     transitions={
#         ('q0', '0'): next('q3', '0', 'S'),  # Step 6 check if all turing machine tape is X and Y ( there is no 1 and 0 left on the tape)
#         ('q0', '1'): next('q3', '1', 'S'),
#         ('q0', 'X'): next('q0', 'X', 'R'),
#         ('q0', 'Y'): next('q0', 'Y', 'R'),
#         ('q0', 'B'): next('q2', 'B', 'S')
#     },
#     initial_state='q0',
#     accept_states={'q2'},
#     reject_states={'q3'}
# )

# combined_tm = CombinedTuringMachine({'0', '1', 'X', 'Y', 'B'})
# combined_tm.add('step1', step1)
# combined_tm.add('step2', step2)
# combined_tm.add('step3', step3)
# combined_tm.add('step4', step4)
# combined_tm.setTuringMachineWhileCondition("myCond",step5)
# controller.add_turing_machine('combined_shit',combined_tm)

# # # #----------------------------testing combine_tm_with_conidition---------------------------

# controller.validate_turing_machine('combined_shit',is_0n1n,{"0011"})
# mrs=controller.run_turing_machine('combined_shit',"0011")
# mrs=controller.run_turing_machine('combined_shit', "0011")
# print("at end tape is:  ",mrs.tape)

# print(step6.given_state_is_in_acceptance(step6.run(mrs.tape.copy()).state))
# controller.visualize('combined_shit', "0011")
# controller.submit()

# # #----------------------------------------------------------------------------------------


# #to do: DONE

# #controller.visualize_step_by_step('combined_shit', "0011")





# # #----------------------------testing combine_tm------------------------------------------

# # #mrs= controller.run_turing_machine('combined_shit','01')

# # # print("fuck you is:   ",combined_tm.turing_machines[-1].given_state_is_in_acceptance(mrs.state))
# # # controller.validate_turing_machine('combined_shit',is_0n1n,{"0011"})
# # # controller.visualize('combined_shit',"01")
# # #controller.visualize_combined_machine_step_by_step('combined_shit',"01")

# # #----------------------------------------------------------------------------------------


# # #--------------------------If Turing machine----------------------------------------------
# ifTm = TuringMachine( # condition if input legth is less than 4 accept else reject
#     states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'},
#     input_alphabet={'0', '1'},
#     tape_symbols={'0', '1', 'B'},
#     transitions={
#         ('q0', '0'): next('q1', '0', 'R'),  
#         ('q0', '1'): next('q1', '1', 'R'),

#         ('q1', '0'): next('q2', '0', 'R'),
#         ('q1', '1'): next('q2', '1', 'R'),

#         ('q2', '0'): next('q3', '0', 'R'),  
#         ('q2', '1'): next('q3', '0', 'R'),
        
#         ('q3', '0'): next('q6', '0', 'R'),
#         ('q3', '1'): next('q6', '1', 'R'),
#         ('q3', 'B'): next('q5', 'B', 'S')
#     },
#     initial_state='q0',
#     accept_states={'q5'},
#     reject_states={'q6'}
# )

# #ifTm.run("01")

# # controller = TuringMachineController()
# # controller.add_turing_machine("if", ifTm)
# # mrs =  controller.run_turing_machine("if", "010")
# # print(mrs.tape)
# # print(ifTm.given_state_is_in_acceptance(mrs.state))

# thenTm = TuringMachine( # condition if input legth is less than 4 change every 1 to 0
#     states={'q0', 'q1', 'q2'},
#     input_alphabet={'0', '1'},
#     tape_symbols={'0', '1', 'B'},
#     transitions={
#         ('q0', '0'): next('q0', '0', 'R'),  
#         ('q0', '1'): next('q0', '0', 'R'),
#         ('q0', 'B'): next('q1', 'B', 'R')
#     },
#     initial_state='q0',
#     accept_states={'q1'},
#     reject_states={'q2'}
# )

# elseTm = TuringMachine( # condition if input legth is less than 4 change every 0 to 1
#     states={'q0', 'q1', 'q2'},
#     input_alphabet={'0', '1'},
#     tape_symbols={'0', '1', 'B'},
#     transitions={
#         ('q0', '0'): next('q0', '1', 'R'),  
#         ('q0', '1'): next('q0', '1', 'R'),
#         ('q0', 'B'): next('q1', 'B', 'R')
#     },
#     initial_state='q0',
#     accept_states={'q1'},
#     reject_states={'q2'}
# )

# if1 = IFTuringMachine()
# if1.setIfTM(ifTm,"if1")
# if1.setThenTM(thenTm,"then1")
# if1.setElseTM(elseTm, "else1")

# controller = TuringMachineController()
# # controller.add_turing_machine("if", if1)
# # mrs =  controller.run_turing_machine("if", "011")
# # print(mrs.tape)
# # print(ifTm.given_state_is_in_acceptance(mrs.state))

# #controller.visualize_step_by_step("if", "01111111")

# simple_turing_machine = TuringMachine(
#     states={'q0', 'q1','q2'},
#     input_alphabet={'0', '1'},
#     tape_symbols={'0', '1', 'B'},
#     transitions={
#         ('q0', '0'): next('q1', '1', 'R'),  # if encountered 0 put 1 and move right
#         ('q0', '1'): next('q0', '1', 'R'),  # if encountered 1 just move right
#         ('q0', 'B'): next('q1', 'B', 'S'),  # if encountered 1 just move right
#         ('q1', '0'): next('q1', '0', 'S'),  # after reaching q1 don't do anything
#         ('q1', '1'): next('q1', '1', 'S'),  # after reaching q1 don't do anything
#         ('q1', 'B'): next('q1', 'B', 'S'),  # after reaching q1 don't do anything

#     },
#     initial_state='q0',
#     accept_states={'q1'},
#     reject_states={'q2'}
# )


# simple_turing_machine_2 = TuringMachine(
#     states={'q0', 'q1','q2'},
#     input_alphabet={'0', '1'},
#     tape_symbols={'0', '1', 'B'},
#     transitions={
#         ('q0', '0'): next('q0', '0', 'R'),  # if encountered 0 put 1 and move right
#         ('q0', '1'): next('q1', '0', 'R'),  # if encountered 1 just move right
#         ('q0', 'B'): next('q1', 'B', 'S'),  # if encountered 1 just move right
#         ('q1', '0'): next('q1', '0', 'S'),  # after reaching q1 don't do anything
#         ('q1', '1'): next('q1', '1', 'S'),  # after reaching q1 don't do anything
#         ('q1', 'B'): next('q1', 'B', 'S'),  # after reaching q1 don't do anything

#     },
#     initial_state='q0',
#     accept_states={'q1'},
#     reject_states={'q2'}
# )


# while_machine = TuringMachine(
#     states={'q0', 'q1','q2'},
#     input_alphabet={'0', '1'},
#     tape_symbols={'0', '1', 'B'},
#     transitions={
#         ('q0', '0'): next('q0', '0', 'R'),  # if encountered 0 put 1 and move right
#         ('q0', '1'): next('q0', '1', 'R'),  # if encountered 1 just move right
#         ('q0', 'B'): next('q1', 'B', 'S'),  # if encountered 1 just move right
#     },
#     initial_state='q0',
#     accept_states={'q1'},
#     reject_states={'q2'}
# )


# ifcond_machine= TuringMachine( ## if first letter is 1
#     states={'q0', 'q1','q2'},
#     input_alphabet={'0', '1'},
#     tape_symbols={'0', '1', 'B'},
#     transitions={
#         ('q0', '0'): next('q2', '0', 'S'),
#         ('q0', '1'): next('q1', '1', 'R'),
#         ('q0', 'B'): next('q2', 'B', 'S'),

#     },
#     initial_state='q0',
#     accept_states={'q1'},
#     reject_states={'q2'}
# )


# combined_tm = CombinedTuringMachine()
# combined_tm.setTuringMachineWhileCondition(while_machine,"condition")
# combined_tm.add("step1",simple_turing_machine)
# combined_tm.add("step2",simple_turing_machine_2)

# controller.add_turing_machine("shit",simple_turing_machine)
# controller.add_turing_machine("shit2",combined_tm)


# if_machine=IFTuringMachine() #if first letter is 1 then convert first 0 to 1 else convert first 1 to 0

# if_machine.setIfTM(ifcond_machine,"ifcond")
# if_machine.setThenTM(simple_turing_machine,"convert_0_to_1")
# if_machine.setElseTM(simple_turing_machine_2,"convert_1_to_0")

# controller.add_turing_machine("ifshit",if_machine)

# controller.visualize("ifshit","10")



########################################################################################
# step1 = TuringMachine(
#             states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
#             input_alphabet={'0', '1'},
#             tape_symbols={'0', '1', 'X', 'Y', 'B'},
#             transitions={
#                 ('q0', '0'): next('q1', 'X', 'R'),  # Step 1 change 0 to X
#                 ('q0', 'Y'): next('q3', 'Y', 'R'),
#                 ('q1', '0'): next('q1', '0', 'R'),
#                 ('q1', '1'): next('q2', 'Y', 'L'),
#                 ('q1', 'Y'): next('q1', 'Y', 'R'),
#                 ('q2', '0'): next('q2', '0', 'L'),
#                 ('q2', 'X'): next('q0', 'X', 'R'),
#                 ('q2', 'Y'): next('q2', 'Y', 'L'),
#                 ('q3', 'Y'): next('q3', 'Y', 'R'),
#                 ('q3', 'B'): next('q4', 'B', 'L')
#             },
#             initial_state='q0',
#             accept_states={'q4'},
#             reject_states={'q5'}
#         )

# combined_tm = CombinedTuringMachine({'0', '1'})
# combined_tm.add('an_bn', step1)
# result = TuringMachineController()
# result.add_turing_machine("myCombined", combined_tm)

# def is_0n1n(s):
#     if(len(s) < 2):
#         return False
#     elif(len(s) == 2 and s != "01"):
#         return False
#     elif(len(s) == 2 and s == "01"):
#         return True
#     st = s.split('01')
#     if(len(st) != 2):
#         return False
#     if(len(st[0]) != len(st[1])):
#         return False
#     for i in st[0]:
#         if i != '0':
#             return False
#     for i in st[1]:
#         if i != '1':
#             return False
#     return True

#     return not stack  # Check if the stack is empty at the end
# def notValidFunc(asd):
#     return True

# res = result.validate_turing_machine("myCombined",is_0n1n)
# #self.assertEqual(res,True)
# print(res)
# #print(result.run_turing_machine("myCombined", "01"))
# #res = result.validate_turing_machine("myCombined",notValidFunc)
# #self.assertEqual(res,False)


# try:
#     step1 = TuringMachine(
#         states={'q0', 'q1', 'q2', 'q3'},
#         input_alphabet={'0', '1', 'X', 'Y', 'B'},
#         tape_symbols={'0', '1', 'X', 'Y', 'B'},
#         transitions={
#             ('q0', '0'): next('q2', 'X', 'R'),  # Step 1 change 0 to X
#             ('q0', '1'): next('q3', '1', 'S'),
#             ('q0', 'X'): next('q3', 'X', 'S'),
#             ('q0', 'Y'): next('q3', 'Y', 'S'),
#             ('q0', 'B'): next('q3', 'B', 'S')
#         },
#         initial_state='q0',
#         accept_states={'q2'},
#         reject_states={'q3'}
#     )
#     step2 = TuringMachine(
#     states={'q0', 'q1', 'q2', 'q3'},
#     input_alphabet={'0', '1', 'X', 'Y', 'B'},
#     tape_symbols={'0', '1', 'X', 'Y', 'B'},
#     transitions={
#         ('q0', '0'): next('q0', '0', 'R'),  # Step 2 move right to the first 1
#         ('q0', '1'): next('q2', '1', 'S'),  # if you do not find symbol 1, reject the language
#         ('q0', 'X'): next('q0', 'X', 'R'),
#         ('q0', 'Y'): next('q0', 'Y', 'R'),
#         ('q0', 'B'): next('q3', 'B', 'S')
#     },
#     initial_state='q0',
#     accept_states={'q2'},
#     reject_states={'q3'}
# )

#     step3 = TuringMachine(
#         states={'q0', 'q1', 'q2', 'q3'},
#         input_alphabet={'0', '1', 'X', 'Y', 'B'},
#         tape_symbols={'0', '1', 'X', 'Y', 'B'},
#         transitions={
#             ('q0', '0'): next('q3', '0', 'S'),  # Step 3 change 1 to Y
#             ('q0', '1'): next('q2', 'Y', 'L'),
#             ('q0', 'X'): next('q3', 'X', 'S'),
#             ('q0', 'Y'): next('q3', 'Y', 'S'),
#             ('q0', 'B'): next('q3', 'B', 'S')
#         },
#         initial_state='q0',
#         accept_states={'q2'},
#         reject_states={'q3'}
#     )

#     step4 = TuringMachine(
#         states={'q0', 'q1', 'q2', 'q3'},
#         input_alphabet={'0', '1', 'X', 'Y', 'B'},
#         tape_symbols={'0', '1', 'X', 'Y', 'B'},
#         transitions={
#             ('q0', '0'): next('q0', '0', 'L'),  # Step 4 Move Left to Leftmost 0
#             ('q0', '1'): next('q3', '1', 'S'),
#             ('q0', 'X'): next('q2', 'X', 'R'),
#             ('q0', 'Y'): next('q0', 'Y', 'L'),
#             ('q0', 'B'): next('q3', 'B', 'R')
#         },
#         initial_state='q0',
#         accept_states={'q2'},
#         reject_states={'q3'}
#     )

#     #step 5 repeat steps number 01 to 04 until no more 0 and 1 remain in the input tape
#     step5 = TuringMachine(
#         states={'q0', 'q1', 'q2', 'q3'},
#         input_alphabet={'0', '1', 'X', 'Y', 'B'},
#         tape_symbols={'0', '1', 'X', 'Y', 'B'},
#         transitions={
#             ('q0', '0'): next('q2', '0', 'S'),  # Step 6 check if all turing machine tape is X and Y ( there is no 1 and 0 left on the tape)
#             ('q0', '1'): next('q2', '1', 'S'),
#             ('q0', 'X'): next('q0', 'X', 'R'),
#             ('q0', 'Y'): next('q0', 'Y', 'R'),
#             ('q0', 'B'): next('q3', 'B', 'S')
#         },
#         initial_state='q0',
#         accept_states={'q2'},
#         reject_states={'q3'}
#     )
#     step6 = TuringMachine(
#         states={'q0', 'q1', 'q2', 'q3'},
#         input_alphabet={'0', '1', 'X', 'Y', 'B'},
#         tape_symbols={'0', '1', 'X', 'Y', 'B'},
#         transitions={
#             ('q0', '0'): next('q3', '0', 'S'),  # Step 6 check if all turing machine tape is X and Y ( there is no 1 and 0 left on the tape)
#             ('q0', '1'): next('q3', '1', 'S'),
#             ('q0', 'X'): next('q0', 'X', 'R'),
#             ('q0', 'Y'): next('q0', 'Y', 'R'),
#             ('q0', 'B'): next('q2', 'B', 'S')
#         },
#         initial_state='q0',
#         accept_states={'q2'},
#         reject_states={'q3'}
#     )

#     combined_tm = CombinedTuringMachine({'0', '1'})
#     combined_tm.add('Change 0 to X', step1)
#     combined_tm.add('Move Right To First 1', step2)
#     combined_tm.add('Change 1 to Y', step3)
#     combined_tm.add('Move Left to Leftmost 0', step4)
#     # test without cond
#     result = TuringMachineController()
#     result.add_turing_machine("myCombined", combined_tm)
#     res = result.run_turing_machine("myCombined", "0011")
#     print(res)
#     res = ''.join(res.tape)
#     res = res.replace('B','')
#     # test with while cond
#     result.remove("myCombined")
#     combined_tm.setTuringMachineWhileCondition("0 or 1 in tape", step5)
#     result.add_turing_machine("myCombined", combined_tm)
#     res = result.run_turing_machine("myCombined", "0011")
#     res = ''.join(res.tape)
#     res = res.replace('B','')
#     #self.assertEqual(result, "XXYY")
# except Exception as e:
#     print("NO")






# # language 0^n_1^n_2_0^n_1^n
# step1 = TuringMachine( 
#             states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
#             input_alphabet={'0', '1', '2', 'X', 'Y', 'B','Z'},
#             tape_symbols={'0', '1', '2', 'X', 'Y', 'B','Z'},
#             transitions={
#                 ('q0', '0'): next('q1', 'X', 'R'),  # Step 1 change 0 to X
#                 ('q0', 'Y'): next('q3', 'Y', 'R'),
#                 ('q1', '0'): next('q1', '0', 'R'),
#                 ('q1', '1'): next('q2', 'Y', 'L'),
#                 ('q1', 'Y'): next('q1', 'Y', 'R'),
#                 ('q2', '0'): next('q2', '0', 'L'),
#                 ('q2', 'X'): next('q0', 'X', 'R'),
#                 ('q2', 'Y'): next('q2', 'Y', 'L'),
#                 ('q3', 'Y'): next('q3', 'Y', 'R'),
#                 ('q3', 'B'): next('q4', 'B', 'S'),

#                 ('q3', '2'): next('q4', '2', 'S')
#             },
#             initial_state='q0',
#             accept_states={'q4'},
#             reject_states={'q5'}
#         )
# cond = TuringMachine( #current head pos equals 0
#             states={'q0', 'q1', 'q2', 'q3'},
#             input_alphabet={'0', '1','2' , 'X', 'Y', 'B','Z'},
#             tape_symbols={'0', '1','2', 'X', 'Y', 'B','Z'},
#             transitions={
#                 ('q0', 'X'): next('q0', 'X', 'R'),
#                 ('q0', 'Y'): next('q0', 'Y', 'R'),
#                 ('q0', '2'): next('q2', 'Z', 'R'),
#                 ('q0', 'Z'): next('q0', 'Z', 'R')
#             },
#             initial_state='q0',
#             accept_states={'q2'},
#             reject_states={'q3'}
#         )

# combined_tm = CombinedTuringMachine({'0', '1', '2'})
# combined_tm.add('find_a_n_b_n', step1)
# #combined_tm.add('Move Left to Leftmost 0', step4)

# #you want to repeat steps number 01 to 04 until no more 0 and 1 remain in the input tape
# combined_tm.setTuringMachineWhileCondition("2 still in tape", cond)
# controller = TuringMachineController()
# ####################important step!!!! dont forget!!!##########################
# controller.add_turing_machine('OccurenceOf0==1',combined_tm)
# ###############################################################################

# controller.run_turing_machine('OccurenceOf0==1', "01201")

# # def check_zeros_equal_ones(input_str):
# #     if(len(input_str) == 0):
# #       return False
# #     if(str(input_str[0]) != "0"):
# #         return False
# #     count_0 = input_str.count('0')
# #     count_1 = input_str.count('1')
# #     return count_0 == count_1

# # controller.validate_turing_machine('OccurenceOf0==1', check_zeros_equal_ones)

##########################################################################

controller = TuringMachineController()

# ifTm = TuringMachine(  # condition if input legth is less than 4 accept else reject
#         states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'},
#         input_alphabet={'0', '1'},
#         tape_symbols={'0', '1', 'B'},
#         transitions={
#             ('q0', '0'): next('q1', '0', 'R'),
#             ('q1', '1'): next('q3', '1', 'R'),
#             ('q3', 'B'): next('q3', 'B', 'L'),
#             ('q3', '1'): next('q3', '1', 'L'),
#             ('q3', '0'): next('q3', '0', 'L'),
#         },
#         initial_state='q0',
#         accept_states={'q5'},
#         reject_states={'q6'}
#     )

# controller.add_turing_machine("shit",ifTm)
# controller.visualize("shit","01")

# def is_0n1n(s):
#     if(len(s) < 2):
#         return False
#     elif(len(s) == 2 and s != "01"):
#         return False
#     elif(len(s) == 2 and s == "01"):
#         return True
#     st = s.split('01')
#     if(len(st) != 2):
#         return False
#     if(len(st[0]) != len(st[1])):
#         return False
#     for i in st[0]:
#         if i != '0':
#             return False
#     for i in st[1]:
#         if i != '1':
#             return False
#     return True

# controller.add_challenge("0n1n","turing machine that accepts 0n1n",is_0n1n,{"02","01"});

# controller.get_challenges()


##########################################################################


# # language 0^n_1^n_2_0^n_1^n (2_0^n_1^n_2_0^n_1^n)*
# step1 = TuringMachine(
#             states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
#             input_alphabet={'0', '1', '2', 'X', 'Y', 'B','Z'},
#             tape_symbols={'0', '1', '2', 'X', 'Y', 'B','Z'},
#             transitions={
#                 ('q0', '0'): next('q1', 'X', 'R'),  # Step 1 change 0 to X
#                 ('q0', 'Y'): next('q3', 'Y', 'R'),
#                 ('q1', '0'): next('q1', '0', 'R'),
#                 ('q1', '1'): next('q2', 'Y', 'L'),
#                 ('q1', 'Y'): next('q1', 'Y', 'R'),
#                 ('q2', '0'): next('q2', '0', 'L'),
#                 ('q2', 'X'): next('q0', 'X', 'R'),
#                 ('q2', 'Y'): next('q2', 'Y', 'L'),
#                 ('q3', 'Y'): next('q3', 'Y', 'R'),
#                 ('q3', 'B'): next('q4', 'B', 'S'),

#                 ('q3', '2'): next('q4', '2', 'S')
#             },
#             initial_state='q0',
#             accept_states={'q4'},
#             reject_states={'q5'}
#         )
# cond = TuringMachine( #current head pos equals 0
#             states={'q0', 'q1', 'q2', 'q3'},
#             input_alphabet={'0', '1','2' , 'X', 'Y', 'B','Z'},
#             tape_symbols={'0', '1','2', 'X', 'Y', 'B','Z'},
#             transitions={
#                 ('q0', 'X'): next('q0', 'X', 'R'),
#                 ('q0', 'Y'): next('q0', 'Y', 'R'),
#                 ('q0', '2'): next('q2', 'Z', 'R'),
#                 ('q0', 'Z'): next('q0', 'Z', 'R')
#             },
#             initial_state='q0',
#             accept_states={'q2'},
#             reject_states={'q3'}
#         )
# combined_tm = CombinedTuringMachine({'0', '1', '2'})
# combined_tm.add('find_a_n_b_n', step1)
# #combined_tm.add('Move Left to Leftmost 0', step4)

# #you want to repeat steps number 01 until no more 2 remain in the tape
# combined_tm.setTuringMachineWhileCondition("2 still in tape", cond)
# ####################important step!!!! dont forget!!!##########################
# controller.add_turing_machine('WhileCombined',combined_tm)


# #controller.run_turing_machine('WhileCombined', "001120011")

# controller.visualize('WhileCombined',"01201")
# def is_0n1n(s):
#     if(len(s) < 2):
#         return False
#     elif(len(s) == 2 and s != "01"):
#         return False
#     elif(len(s) == 2 and s == "01"):
#         return True
#     st = s.split('01')
#     if(len(st) != 2):
#         return False
#     if(len(st[0]) != len(st[1])):
#         return False
#     for i in st[0]:
#         if i != '0':
#             return False
#     for i in st[1]:
#         if i != '1':
#             return False
#     return True

# controller.add_challenge("0n1n", {'0','1'},"turing machine that accepts 0n1n",is_0n1n,{"02","01"})

# _0_pow_n_1_pow_n_TM = TuringMachine(
#             states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9'},
#             input_alphabet={'a', 'b'},
#             tape_symbols={'a', 'b', 'X', 'Y', 'B'},
#             transitions={
#                 ('q0', 'a'): next('q1', 'B', 'R'),  
#                 ('q0', 'b'): next('q2', 'B', 'R'),
#                 ('q0', 'B'): next('q8', 'B', 'S'),
#                 ('q1', 'a'): next('q3', 'a', 'R'),
#                 ('q1', 'b'): next('q3', 'b', 'R'),
#                 ('q1', 'B'): next('q8', 'B', 'S'),
#                 ('q2', 'a'): next('q4', 'a', 'R'),
#                 ('q2', 'b'): next('q4', 'b', 'R'),
#                 ('q2', 'B'): next('q8', 'B', 'S'),
#                 ('q3', 'a'): next('q3', 'a', 'R'),
#                 ('q3', 'b'): next('q3', 'b', 'R'),
#                 ('q3', 'B'): next('q5', 'B', 'L'),
#                 ('q4', 'a'): next('q4', 'a', 'R'),
#                 ('q4', 'b'): next('q4', 'b', 'R'),
#                 ('q4', 'B'): next('q6', 'B', 'L'),
#                 ('q5', 'a'): next('q7', 'B', 'L'),
#                 ('q6', 'b'): next('q7', 'B', 'L'),
#                 ('q7', 'a'): next('q7', 'a', 'L'),
#                 ('q7', 'b'): next('q7', 'b', 'L'),
#                 ('q7', 'B'): next('q0', 'B', 'R')

#             },
#             initial_state='q0',
#             accept_states={'q8'},
#             reject_states={'q9'}
#         )

# ## after you build it you need to add it to the controller and give it the same name  that was given by the TA:
# controller.add_turing_machine('0n1n', _0_pow_n_1_pow_n_TM)

# controller.visualize('0n1n','')
# #controller.submit()






# language 0^n_1^n_2_0^n_1^n (2_0^n_1^n_2_0^n_1^n)*
step1 = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
            input_alphabet={'0', '1', '2', 'X', 'Y', 'B','Z'},
            tape_symbols={'0', '1', '2', 'X', 'Y', 'B','Z'},
            transitions={
                ('q0', '0'): next('q1', 'X', 'R'),  # Step 1 change 0 to X
                ('q0', 'Y'): next('q3', 'Y', 'R'),
                ('q1', '0'): next('q1', '0', 'R'),
                ('q1', '1'): next('q2', 'Y', 'L'),
                ('q1', 'Y'): next('q1', 'Y', 'R'),
                ('q2', '0'): next('q2', '0', 'L'),
                ('q2', 'X'): next('q0', 'X', 'R'),
                ('q2', 'Y'): next('q2', 'Y', 'L'),
                ('q3', 'Y'): next('q3', 'Y', 'R'),
                ('q3', 'B'): next('q4', 'B', 'S'),

                ('q3', '2'): next('q4', '2', 'S')
            },
            initial_state='q0',
            accept_states={'q4'},
            reject_states={'q5'}
        )
cond = TuringMachine( #current head pos equals 0
            states={'q0', 'q1', 'q2', 'q3'},
            input_alphabet={'0', '1','2' , 'X', 'Y', 'B','Z'},
            tape_symbols={'0', '1','2', 'X', 'Y', 'B','Z'},
            transitions={
                ('q0', 'X'): next('q0', 'X', 'R'),
                ('q0', 'Y'): next('q0', 'Y', 'R'),
                ('q0', '2'): next('q2', 'Z', 'R'),
                ('q0', 'Z'): next('q0', 'Z', 'R')
            },
            initial_state='q0',
            accept_states={'q2'},
            reject_states={'q3'}
        )
dowhile = WhileTuringMachine("My Cond", cond, "My Do While", step1)
# combined_tm.add('find_a_n_b_n', step1)
#combined_tm.add('Move Left to Leftmost 0', step4)

#you want to repeat steps number 01 until no more 2 remain in the tape
# combined_tm.setTuringMachineWhileCondition("2 still in tape", cond)
####################important step!!!! dont forget!!!##########################
controller.add_turing_machine('doWhile',dowhile)


controller.run_turing_machine('doWhile', "001120011")
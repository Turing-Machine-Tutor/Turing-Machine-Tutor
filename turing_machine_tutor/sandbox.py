from TuringMachine import TuringMachine
from TuringMachineController import TuringMachineController
from configuration import Configuration



def test_me(number):
    if number==1:
        return "one"
    if number==2:
        return "two"
    if number==3:
        return "three"
    return


ok=Configuration(1,2,3)
print(ok.try_me(test_me))


emptyString = TuringMachine(
    states={'q0', 'q1', 'rej', 'acc'},
    input_alphabet={'0', '1'},
    tape_symbols={'0', '1', '_'},
    blank = '_',
    transitions={
        ('q0', '0'): Configuration('q1', '0', 'R'),
        ('q0', '1'): Configuration('q1', '1', 'R'),
        ('q1', '0'): Configuration('q0', '0', 'R'),
        ('q1', '1'): Configuration('q0', '1', 'R'),
        ('q0', '_'): Configuration('acc', '_', 'R'),
        ('q1', '_'): Configuration('rej', '_', 'R'),
    },
    initial_state='q0',
    accept_states={'acc'},
    reject_states={'rej'}
)


# Create a Turing machine
tm1 = TuringMachine(
    states={'q0', 'q1', 'q2', 'q3'},
    input_alphabet={'0', '1'},
    tape_symbols={'0', '1', 'B'},
    blank = 'B',
    transitions={
        ('q0', '0'): Configuration('q1', '0', 'R'),
        ('q0', '1'): Configuration('q1', '1', 'R'),
        ('q1', '0'): Configuration('q0', '0', 'R'),
        ('q1', '1'): Configuration('q0', '1', 'R'),
        ('q0', 'B'): Configuration('q3', 'B', 'R'),
        ('q1', 'B'): Configuration('q2', 'B', 'R'),
    },
    initial_state='q0',
    accept_states={'q3'},
    reject_states={'q2'}
)

anbn_turing_machine = TuringMachine(
    states={'q0', 'q1', 'q2', 'q3', 'q4'},
    input_alphabet={'0', '1'},
    tape_symbols={'0', '1', 'X', 'Y', 'B'},
    blank='B',
    transitions={
        ('q0', '0'): Configuration('q1', 'X', 'R'),  # Move right and replace 0 with X
        ('q1', '0'): Configuration('q1', '0', 'R'),  # Continue moving right over 0
        ('q1', 'Y'): Configuration('q1', 'Y', 'R'),  # Skip Y
        ('q1', '1'): Configuration('q2', 'Y', 'L'),  # Move left and replace 1 with Y
        ('q2', 'Y'): Configuration('q2', 'Y', 'L'),  # Continue moving left over Y
        ('q2', '0'): Configuration('q2', '0', 'L'),  # Continue moving left over 0
        ('q2', 'X'): Configuration('q0', 'X', 'R'),  # Move right to find the next 0 after 1s
        ('q0', 'Y'): Configuration('q0', 'Y', 'R'),  # Skip Y in the process
        ('q0', 'B'): Configuration('q4', 'B', 'R')   # Accept if B is encountered after checking
    },
    initial_state='q0',
    accept_states={'q4'},
    reject_states={'q5'}
)


controller = TuringMachineController()
controller.add_turing_machine('emptyString', emptyString)
controller.add_turing_machine('tm1',tm1)
controller.add_turing_machine('0n1n',anbn_turing_machine)

# Run the Turing machine from the library
mrs= controller.run_turing_machine('tm1', '000111')
print(tm1.given_state_is_in_acceptance(mrs.state))
mrs= controller.run_turing_machine('0n1n', '0000011111')
print(anbn_turing_machine.given_state_is_in_acceptance(mrs.state))


def is_0n1n(input_str):
    stack = []

    for symbol in input_str:
        if symbol == '0':
            stack.append('0')
        elif symbol == '1':
            if not stack:
                return False  # There are more '1's than '0's
            stack.pop()
        else:
            return False  # Invalid symbol

    return not stack

##controller.validate_turing_machine('0n0n',is_0n1n,{"00"})
controller.visualize('0n1n',"0011")


from tabulate import tabulate

from turing_machine_tutor.challenge import Challenge
from turing_machine_tutor.domain import Word, Letter, EMPTY
from turing_machine_tutor.examples.example import Example
from turing_machine_tutor.examples.intentional_bug import intentional_bug
from turing_machine_tutor.transition_table import RIGHT, LEFT, STAY
from turing_machine_tutor.turing_machine import TuringMachine
from turing_machine_tutor.turing_machine_builder import TuringMachineBuilder
from turing_machine_tutor.turing_machine_run import TuringMachineRun

alphabet = tuple(map(Letter, range(10)))


def is_leap_year(w: Word):
    """
    note: parameter needs to be a Word, of letters that are '0'-'9'.
    if N%4 == 0, it's a leap year, (ex: 2004, 1996)
    except if N%100 == 0, then it's not a leap year (1900, 2100),
    except if N%400 == 0, then it is a leap year (1600, 2000, 2400)
    """
    if not w:  # empty word
        return False
    if not all(sigma in alphabet for sigma in w):
        return False
    as_str = ''.join(map(str, w))
    as_int = int(as_str)
    if as_int % 4 != 0:
        return False
    if as_int % 100 != 0:
        return True
    return as_int % 400 == 0

_cases = (
    1981, 1901, 1903, 1993, 1997, 1924, 1934, 1962,
    1936, 1910, 1920, 1300, 1900, 1400, 1200, 2000, 2800, 1600, 2200,
    0,  # year 0 did not exist, but if it would, it should have been a leap year
    *range(1, 17),
    23, 24, 100, 156, 142, 980
)

def _challenge() -> Challenge:
    return Challenge(
        short_name="leap_years",
        description="""
        Write a machine that accepts a number (in decimal) if and only if it is a leap year.
        Note:
            Despite common misconception, not every year divisible by 4 is a leap year.
            For example, 2100 will not be a leap year. 
            The actual rule is:
            if N%4 == 0, it's a leap year, (ex: 2004, 1996)
            EXCEPT if N%100 == 0, then it's not a leap year (1900, 2100),
            EXCEPT if N%400 == 0, then it is a leap year (1600, 2000, 2400).
        Examples:
            2015, 2023 were not leap years (N % 4 != 0).
            2004 and 1996 were leap years (N % 4 == 0, N % 100 != 0)
            1900 and 1800 were not leap years (N % 100 == 0, N % 400 != 0)
            1600 and 2000 were leap years (N % 400 == 0)
        Note:
            You may assume the input has at least 4 digits. Years before 1000
            will be padded, such as 4 -> 0004, 14 -> 0014, 980 -> 0980.
            You will NOT be tested against un-padded inputs like 980, 014, 15, 09, 8.
        Note:
            As far as we are concerned, this is also true for years that were before this
            rule was introduces, for example 856 (which we write 0856). This is also true
            for year 0, which did not exist, but if it would exist, it should have been a leap year. 
        """,
        alphabet=alphabet,
        validator=is_leap_year,
        words=tuple(map(lambda x: f'{x:04}', _cases))
    )




def _machine() -> TuringMachine:
    B = "*"
    ZERO = alphabet[0]

    builder = TuringMachineBuilder()
    builder.blank_character = B
    builder.input_alphabet.extend(alphabet)
    builder.tape_alphabet.extend(alphabet)
    builder.tape_alphabet.append(B)

    q = [f"q{i}" for i in range(0, 8)]

    q0 = q[0]
    builder.initial_state = q0

    builder.states.extend(q)
    acc, rej = 'acc', 'rej'

    builder.states.extend((acc, rej))
    builder.accepting_state = acc
    builder.rejecting_state = rej

    # q0
    builder.delta.on_state(q[0]).on_letters(*alphabet).skip_right()
    builder.delta[q[0], B] = q[1], B, LEFT

    # q1
    odds = tuple(alphabet[i] for i in range(1, 10, 2))
    evens = tuple(alphabet[i] for i in range(0, 10, 2))

    builder.delta.on_state(q[1]).on_letters(*odds).change_state(rej)

    @intentional_bug(activated=True)
    def create_loop():
        builder.delta.on_state(q[1]).on_letters(*odds).change_state(q[1])

    builder.delta.on_state(q[1]).on_letters('0').change_state(q[4], LEFT)
    builder.delta.on_state(q[1]).on_letters('4', '8').change_state(q[2], LEFT)
    builder.delta.on_state(q[1]).on_letters('2', '6').change_state(q[3], LEFT)

    # q2
    builder.delta.on_state(q[2]).on_letters(*evens).change_state(acc)  # 1924
    builder.delta.on_state(q[2]).on_letters(*odds).change_state(rej)  # 1934

    @intentional_bug(activated=False)
    def flip_q2():
        builder.delta.on_state(q[2]).on_letters(*evens).change_state(rej)  # 1924

    # q3
    builder.delta.on_state(q[3]).on_letters(*evens).change_state(rej)  # 1962
    builder.delta.on_state(q[3]).on_letters(*odds).change_state(acc)  # 1936

    # q4 (that's the interesting one!)

    non_zero_evens = tuple(d for d in evens if d != ZERO)
    builder.delta.on_state(q[4]).on_letters(*non_zero_evens).change_state(acc)  # 1920
    builder.delta.on_state(q[4]).on_letters(*odds).change_state(rej)  # 1910

    builder.delta[q[4], ZERO] = q[5], ZERO, LEFT

    # q5 (interesting-er)

    builder.delta.on_state(q[5]).on_letters(*odds).change_state(rej)  # 1900, 1300
    builder.delta.on_state(q[5]).on_letters('0', '4', '8').change_state('q6', LEFT)
    builder.delta.on_state(q[5]).on_letters('2', '6').change_state('q7', LEFT)

    # q6
    for d in odds:
        builder.delta[q[6], d] = rej, d, STAY  # 1400
    for d in evens:
        builder.delta[q[6], d] = acc, d, STAY  # 2000, 2800

    builder.delta.on_state(q[6]).on_letters(*odds).change_state(rej)  # 1400
    builder.delta.on_state(q[6]).on_letters(*evens).change_state(acc)  # 2000, 2800

    # q7
    builder.delta.on_state(q[7]).on_letters(*odds).change_state(acc)  # 1600
    builder.delta.on_state(q[7]).on_letters(*evens).change_state(rej)  # 2200

    return builder.build(fill_missing_transitions=True)





def _example() -> Example:
    return Example(
        challenge=_challenge(),
        machine=_machine(),
    )


leap_years = _example()

if __name__ == '__main__':
    print(leap_years.challenge.test_machine(leap_years.machine).pretty_str(sort_column=3, sort_desc=True))

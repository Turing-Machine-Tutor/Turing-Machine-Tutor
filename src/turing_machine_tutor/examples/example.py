import string

from attr import define, field

from turing_machine_tutor.challenge import Challenge
from turing_machine_tutor.domain import Word
from turing_machine_tutor.transition_table import TransitionTable, TransitionTableEntryKey, \
    TransitionTableEntryValue, L, R, S
from turing_machine_tutor.turing_machine import TuringMachine


@define(frozen=True)
class Example:
    challenge: Challenge
    machine: TuringMachine

"""

def _palindrome() -> Example: ...


palindrome = _palindrome()


def _even_numbers() -> Example: ...


even_numbers = _even_numbers()

=
"""
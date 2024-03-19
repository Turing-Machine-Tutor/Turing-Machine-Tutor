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
def _0n1n() -> Example: ...


example_0n1n = _0n1n()


def _palindrome() -> Example: ...


palindrome = _palindrome()


def _even_numbers() -> Example: ...


even_numbers = _even_numbers()


def _regular_language() -> Example: ...


regular_language = _regular_language()


def _leap_years() -> Example: ...


leap_year = _leap_years()


def _anagram() -> Example:
    az = tuple(string.ascii_lowercase)
    B = "_"
    crossed_out = "~"
    ws = " "
    sep = "#"
    input_alphabet = az + (ws, sep)
    delta: dict[TransitionTableEntryKey, TransitionTableEntryValue] = {}

    q_find_leftmost_R = 'q_find_leftmost_R'
    q_find_leftmost_L = 'q_find_leftmost_L'
    q_found_on_left = {
        l: f'q_found_on_left_{l}'
        for l in az
    }
    q_find_on_right = {
        l: f'q_find_on_right_{l}'
        for l in az
    }

    delta[TransitionTableEntryKey(state=q_find_leftmost_R, letter=sep)] = TransitionTableEntryValue(
        direction=L, letter=sep, state=q_find_leftmost_R
    )

    for l in az + (ws,):
        delta[TransitionTableEntryKey(state=q_find_leftmost_R, letter=l)] = TransitionTableEntryValue(
            direction=L, letter=l, state=q_find_leftmost_R
        )

    for l in az:
        delta[TransitionTableEntryKey(state=q_find_leftmost_L, letter=l)] = TransitionTableEntryValue(
            direction='R', letter=crossed_out, state=q_found_on_left[l]
        )

    q_acc, q_rej = 'q_acc', 'q_rej'
    tm = TuringMachine(
        input_alphabet=input_alphabet,
        tape_alphabet=input_alphabet + (B, crossed_out),
        blank_character=B,
        states={
            *(q_found_on_left.values()), *(q_find_on_right.values()),
            q_find_leftmost_R, q_find_leftmost_L,
            q_acc, q_rej
        },
        initial_state=q_find_leftmost_L,
        accepting_state=q_acc, rejecting_state=q_rej,
        delta=delta
    )


anagram = _anagram()
"""
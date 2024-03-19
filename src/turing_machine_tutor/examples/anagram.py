from string import ascii_uppercase
from typing import Union

from simple_chalk import chalk
from tabulate import tabulate

from turing_machine_tutor.challenge import Challenge
from turing_machine_tutor.domain import Word, Letter
from turing_machine_tutor.examples.example import Example
from turing_machine_tutor.transition_table import RIGHT, LEFT
from turing_machine_tutor.turing_machine import TuringMachine
from turing_machine_tutor.turing_machine_builder import TuringMachineBuilder
from turing_machine_tutor.turing_machine_run import TuringMachineRun

SEPARATOR, SPACE = "|", " "
AZ = tuple(ascii_uppercase)

def is_letter(x: Union[str, Letter]):
    return str(x) in AZ


def _second(it):
    next(it)
    return next(it)


def is_anagram(word: Word):
    if 2 != sum(1 for x in word if x == SEPARATOR):
        return False
    index_of = _second(i for (i, x) in enumerate(word) if x == SEPARATOR)
    left, right = word[1:index_of], word[index_of+1:]
    return sorted(filter(is_letter, left)) == sorted(filter(is_letter, right))

_CASES = [
    Word(w.upper()) for w in (
        "|ELVIS|LIVES", "|THE EYES|THEY SEE",
        "|NOT AN|ANAGRAM", "|the engine of a film|the fine game of nil",
        "|the meaning of life|the fine game of nil",
        "|Turing Machine|Chaim Retuning",
        "|sub|subset", "|subset|sub",
        "|bus|subset", "|subset|bets"
    )
]

LANGUAGE_ALPHABET = AZ + (SEPARATOR, SPACE)

challenge = Challenge(
    short_name="anagram",
    description=f"""
    Write a machine over the alphabet {'A', ..., 'Z', ' ', '|'}
    Which accepts inputs of the form '|w1|w2' if w1 is an anagram of w2.
    Anagrams are phrases that can be rearranged into each other, such as
    "ELVIS|LIVES", "THE EYES|THEY SEE". Spaces are ignored, so you should
    also accept "THE EYES|THEYSEE" or "THE EYES|TH E Y S EE".
    Notice:
        the input also starts with a |. This is {chalk.bold.underline('for your convenience')}.
        You {chalk.bold.underline('may')} rely on all tests being of the form '|w1|w2'. 
    """,
    alphabet=LANGUAGE_ALPHABET,
    validator=is_anagram,
    words=_CASES
)

def _machine() -> TuringMachine:

    builder = TuringMachineBuilder()

    BLANK = "`"

    builder.blank_character = BLANK
    builder.input_alphabet.extend(LANGUAGE_ALPHABET)
    builder.tape_alphabet.extend(LANGUAGE_ALPHABET)
    builder.tape_alphabet.extend((BLANK, ))

    seeking_start, finding_next, find_next = 'seeking_start', 'finding_next', 'find_next'
    seek_start = 'seek_start'
    ensuring_right_done = 'ensuring_right_done'
    look_for = {sigma:f"look_for_{sigma}" for sigma in AZ}
    looking_for = {sigma:f"looking_for_{sigma}" for sigma in AZ}
    acc, rej = "acc", "rej"
    builder.states.extend((seek_start, seeking_start, find_next, finding_next, ensuring_right_done, acc, rej))
    builder.states.extend(look_for.values())
    builder.states.extend(looking_for.values())
    builder.accepting_state, builder.rejecting_state = acc, rej

    # seeking_start
    builder.initial_state = seeking_start
    builder.delta.on_state(seeking_start).on_letters('|').change_state(finding_next, direction=RIGHT)
    builder.delta.on_state(seeking_start).on_letters(*AZ, ' ').skip_left()

    builder.delta.on_state(seek_start).on_letters(*AZ, SPACE).skip_left()
    builder.delta.on_state(seek_start).on_letters(SEPARATOR).change_state(seeking_start, direction=LEFT)


    # finding_next
    builder.delta.on_state(finding_next).on_letters(' ').skip_right()

    # finding_next, look_for, looking_for
    for sigma in AZ:
        builder.delta[finding_next, sigma] = look_for[sigma], SPACE, RIGHT
        builder.delta.on_state(finding_next).on_letters(sigma).\
            change_state(look_for[sigma], direction=RIGHT, write=SPACE)
        builder.delta.on_state(finding_next).on_letters(SPACE).skip_right()
        builder.delta.on_state(finding_next).on_letters(SEPARATOR).change_state(ensuring_right_done)

        builder.delta.on_state(look_for[sigma]).on_letters(*AZ, SPACE).skip_right()
        builder.delta.on_state(look_for[sigma]).on_letters(SEPARATOR).change_state(looking_for[sigma], RIGHT)

        space_and_letters_excl_sigma = (SPACE, ) + tuple(sigma2 for sigma2 in AZ if sigma2 != sigma)
        builder.delta.on_state(looking_for[sigma]).on_letters(*space_and_letters_excl_sigma).skip_right()
        builder.delta.on_state(looking_for[sigma]).on_letters(sigma).change_state(seek_start, write=SPACE)

    # ensuring_right_done
    builder.delta.on_state(ensuring_right_done).on_letters(SPACE, SEPARATOR).skip_right()
    builder.delta.on_state(ensuring_right_done).on_letters(BLANK).change_state(acc)

    return builder.build(fill_missing_transitions=True)

anagram = Example(
    challenge=challenge,
    machine=_machine()
)

if __name__ == '__main__':
    machine = anagram.machine
    run = TuringMachineRun(machine, Word("|ELVIS|LIVES"))
    while not run.is_terminal:
        print("\n\n")
        print(run.pretty_str())
        run.step()
    print("\n\n")

    print(run.pretty_str())

    print(anagram.challenge.test_machine(anagram.machine).pretty_str(sort_column=3, sort_desc=True))

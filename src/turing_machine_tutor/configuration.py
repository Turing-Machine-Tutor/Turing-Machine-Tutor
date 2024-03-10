from attr import frozen

from turing_machine_tutor.domain import State, Letter, Word
from turing_machine_tutor.turing_machine import TuringMachine
from tabulate import *


@frozen
class TuringMachineRunConfiguration:
    state: State
    tape: tuple[Letter, ...]
    head_index: int

    def tape_as_tuples(self) -> tuple[tuple[Letter, ...], Letter, tuple[Letter, ...]]:
        tape, i = self.tape, self.head_index
        return tape[:i], tape[i], tape[i+1:]

    def pretty_str(self):
        first_row = [""] * len(self.tape)
        first_row[self.head_index] = self.state + "\n🔽"
        return tabulate([first_row, self.tape], tablefmt="grid")


class TuringMachineRun:
    def __init__(self, machine: TuringMachine, word: Word):
        self._word = word
        self._machine = machine
        self._config = TuringMachineRunConfiguration(
            state = self._machine.initial_state,
            head_index = 0,
            tape = tuple(word) + (self._machine.blank_character, )
        )
        self._undo_stack = []

    @property
    def configuration(self):
        return self._config

    def step(self):


if __name__ == '__main__':
    config = TuringMachineRunConfiguration(
        state=State('q2'),
        tape=tuple(map(Letter, "HELLO WORLD_")),
        head_index=3
    )
    print(config.pretty_str())

from attr import define

from turing_machine_tutor.domain import State, Letter, Word
from turing_machine_tutor.transition_table import TransitionTableEntryKey, Direction, R, L, S, transition_table
from turing_machine_tutor.turing_machine import TuringMachine
from tabulate import *

from turing_machine_tutor.util.mutate_tuple import mutate_tuple


@define(frozen=True)
class TuringMachineRunConfiguration:
    state: State
    tape: tuple[Letter, ...]
    head_index: int

    def tape_as_tuples(self) -> tuple[tuple[Letter, ...], Letter, tuple[Letter, ...]]:
        tape, i = self.tape, self.head_index
        return tape[:i], tape[i], tape[i + 1:]

    def pretty_str(self):
        first_row = [""] * len(self.tape)
        first_row[self.head_index] = self.state + "\n🔽"
        return tabulate([first_row, self.tape], tablefmt="grid", stralign="center")

    @property
    def letter_on_head(self):
        return self.tape[self.head_index]


_direction_to_dx: dict[Direction, int] = {
    R: 1, L: -1, S: 0
}

_direction_to_arrow: dict[Direction, str] = {
    R: "▶", S: "🔽", L: "◀"
}


class TuringMachineRun:
    def __init__(self, machine: TuringMachine, word: Word):
        self._word = word
        self._machine = machine
        self._config = TuringMachineRunConfiguration(
            state=self._machine.initial_state,
            head_index=0,
            tape=tuple(word) + (self._machine.blank_character,)
        )
        self._history = []

    @property
    def configuration(self):
        return self._config

    @property
    def is_terminal(self):
        return self._config.state in self._machine.terminal_states

    def get_next_transition(self):
        conf = self._config
        return self._machine.get_transition(TransitionTableEntryKey(state=conf.state, letter=conf.letter_on_head))

    def step(self):
        if self.is_terminal:
            print("configuration is terminal - cannot step further.")
            return
        prev_config = self._config
        self._history.append(prev_config)
        transition = self.get_next_transition()
        new_tape = mutate_tuple(prev_config.tape, prev_config.head_index, transition.letter)
        new_index = prev_config.head_index + _direction_to_dx[transition.direction]
        while new_index + 1 >= len(new_tape):
            new_tape = new_tape + (self._machine.blank_character,)
        self._config = TuringMachineRunConfiguration(
            state=transition.state,
            tape=new_tape,
            head_index=new_index
        )

    def undo(self):
        self._config = self._history.pop()

    def pretty_str(self):
        ret = self._config.pretty_str()
        tran = self.get_next_transition()
        if tran:
            ret = ret + "\n" +\
                      f"({self._config.state}, {self._config.letter_on_head}) -> " \
                      f"({tran.state}, {tran.letter}, {_direction_to_arrow[tran.direction]})"
        return ret


if __name__ == '__main__':
    B = '_'
    table = {
        (q, str(bit)): (q_next, 'X', R)
        for bit in range(2)
        for q, q_next in {('q0', 'q1'), ('q1', 'q0')}
    }
    table['q0', 'X'] = ('rej', 'X', S)
    table['q1', 'X'] = ('rej', 'X', L)
    table[('q0', B)] = ('acc', B, R)
    table[('q1', B)] = ('rej', B, R)
    machine = TuringMachine(
        input_alphabet={'0', '1'},
        tape_alphabet={'0', '1', 'X', B},
        blank_character=B,
        states={'q0', 'q1', 'acc', 'rej'},
        initial_state='q0',
        accepting_state='acc',
        rejecting_state='rej',
        delta=table
    )
    run = TuringMachineRun(machine, Word(*map(Letter, "011100010")))
    while not run.is_terminal:
        print(run.pretty_str())
        run.step()
        print()
    print(run.configuration.pretty_str())

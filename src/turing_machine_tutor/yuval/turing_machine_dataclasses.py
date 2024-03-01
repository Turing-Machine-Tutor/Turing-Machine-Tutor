from dataclasses import *
from enum import Enum
from typing import FrozenSet


class SafeDataClass:
    def __post_init__(self):
        for field_ in fields(self):
            value = getattr(self, field_.name)
            object.__setattr__(self, field_.name, field_.type(value))


@dataclass(frozen=True)
class Letter(SafeDataClass):
    as_str: str


@dataclass(frozen=True)
class State(SafeDataClass):
    name: str


class Direction(Enum):
    Left = -1
    Stay = 0
    Right = 1

@dataclass(frozen=True)
class TransitionInput(SafeDataClass):
    state: State
    tape_letter: Letter


@dataclass(frozen=True)
class TuringMachine(SafeDataClass):
    name: str
    states: frozenset[State]
    input_alphabet: frozenset[Letter]
    tape_alphabet: frozenset[Letter]


if __name__ == '__main__':
    tm = TuringMachine(
        name="my thing",
        states = ["a", "b"],
        input_alphabet=["a", "b0"],
        tape_alphabet=["a"]
    )
    print(tm)
    print(tm.states)

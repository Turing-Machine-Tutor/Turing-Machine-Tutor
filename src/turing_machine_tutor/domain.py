from dataclasses import *
from typing import Iterable, Mapping, Union

from attr import define

from turing_machine_tutor.util.input_validation import assert_types


class Letter(str):
    ...


class Word(tuple[Letter]):
    def __new__(cls, *args: Union[tuple[Letter, ...], tuple[str]]):
        if len(args) == 1:
            arg = args[0]
            if isinstance(arg, Word):
                return arg
            elif isinstance(arg, str):
                args = tuple(map(Letter, arg))  # arg -> split to letters
        return super().__new__(cls, args)

    @property
    def is_empty(self):
        return len(self) == 0

    def __repr__(self):
        if self.is_empty:
            return "ε"
        return super(Word, self).__repr__()


EMPTY = Word()


class State(str):
    ...

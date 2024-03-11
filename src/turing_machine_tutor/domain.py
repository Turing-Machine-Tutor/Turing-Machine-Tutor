from dataclasses import *
from typing import Iterable, Mapping

from attr import define

from turing_machine_tutor.util.input_validation import assert_types


class Letter(str):
    ...


class Word(tuple[Letter]):
    def __new__(cls, *args: Letter):
        assert_types(Letter, args)
        return super().__new__(cls, args)

    def __init__(self, *args: Letter):
        pass

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

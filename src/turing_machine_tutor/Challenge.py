from typing import Callable

from attr import define, field

from turing_machine_tutor.domain import Word

from inspect import cleandoc as trim_indent  # use to trim multiline string

@define(frozen=True)
class Challenge:
    short_name: str
    description: str = field(converter=trim_indent)
    alphabet: tuple[str]
    validator: Callable[[Word], bool]

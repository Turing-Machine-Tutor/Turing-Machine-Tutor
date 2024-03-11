from collections import Callable

from attr import define

from turing_machine_tutor.domain import Word


@define(frozen=True)
class Challenge:
    short_name: str
    description: str
    alphabet: tuple[str]
    validator: Callable[[Word], bool]

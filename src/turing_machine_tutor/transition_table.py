from typing import Union, Mapping

from attr import frozen, field
from frozendict import frozendict

from turing_machine_tutor.domain import State, Letter

R, L, S = "R", "L", "S"
DIRECTIONS = frozenset({R, L, S})


@frozen
class TransitionTableEntryKey:
    state: State = field(converter=State)
    letter: Letter = field(converter=Letter)


def _validate_direction(_, __, value):
    if value not in DIRECTIONS:
        raise ValueError(f"direction must be {' | '.join(map(repr, DIRECTIONS))}")


@frozen
class TransitionTableEntryValue:
    state: State = field(converter=State)
    letter: Letter = field(converter=Letter)
    direction: Union[R, L, S] = field(validator=_validate_direction)



TransitionTable = frozendict[TransitionTableEntryKey, TransitionTableEntryValue]


def transition_table(
        entries: Mapping[TransitionTableEntryKey, TransitionTableEntryValue]
) -> TransitionTable:
    return frozendict({
        TransitionTableEntryKey(k): TransitionTableEntryValue(v)
        for k, v in entries.items()
    })

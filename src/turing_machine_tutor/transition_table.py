from typing import Union, Mapping, Any

from attr import define, field
from frozendict import frozendict

from turing_machine_tutor.domain import State, Letter

R, L, S = "R", "L", "S"
Direction = Union[R, L, S]
DIRECTIONS = frozenset({R, L, S})


@define(frozen=True)
class TransitionTableEntryKey:
    state: State = field(converter=State)
    letter: Letter = field(converter=Letter)


def _validate_direction(_, __, value):
    if value not in DIRECTIONS:
        raise ValueError(f"direction must be {' | '.join(map(repr, DIRECTIONS))}")


@define(frozen=True)
class TransitionTableEntryValue:
    state: State = field(converter=State)
    letter: Letter = field(converter=Letter)
    direction: Union[R, L, S] = field(validator=_validate_direction)


TransitionTable = frozendict[TransitionTableEntryKey, TransitionTableEntryValue]


def _key(k: Union[TransitionTableEntryKey, tuple[Any, Any]]) -> TransitionTableEntryKey:
    return k if isinstance(k, TransitionTableEntryKey) else TransitionTableEntryKey(state=k[0], letter=k[1])


def _value(v: Union[TransitionTableEntryValue, tuple[Any, Any]]) -> TransitionTableEntryKey:
    return v if isinstance(v, TransitionTableEntryKey) \
        else TransitionTableEntryValue(state=v[0], letter=v[1], direction=v[2])


def transition_table(
        entries: Mapping[TransitionTableEntryKey, TransitionTableEntryValue]
) -> TransitionTable:
    return frozendict({
        _key(k): _value(v)
        for k, v in entries.items()
    })

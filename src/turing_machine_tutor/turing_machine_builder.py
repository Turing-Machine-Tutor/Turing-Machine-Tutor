from typing import Union, MutableMapping, Iterator, AbstractSet, Optional, Iterable

from frozendict import frozendict

from turing_machine_tutor.domain import State, Letter
from turing_machine_tutor.transition_table import TransitionTableEntryKey, TransitionTableEntryValue, Direction, \
    TransitionTable, RIGHT, LEFT, STAY
from turing_machine_tutor.turing_machine import TuringMachine

_State = Union[str, State]
_Letter = Union[str, Letter]
_KT = Union[TransitionTableEntryKey, tuple[_State, _Letter]]
_VT = Union[TransitionTableEntryValue, tuple[_State, _Letter, Direction]]


def _ensure_key(k: _KT):
    if not isinstance(k, TransitionTableEntryKey):
        k = TransitionTableEntryKey(*k)
    return k


def _ensure_value(v: _VT):
    if not isinstance(v, TransitionTableEntryValue):
        v = TransitionTableEntryValue(*v)
    return v


class _TransitionTableBuilderStateHelper:
    def __init__(self, builder: 'TransitionTableBuilder', state: State):
        self._builder = builder
        self._state = state

    def on_letters(self, *letters: Letter):
        return _TransitionTableBuilderStateLettersHelper(self._builder, self._state, letters)


class _TransitionTableBuilderStateLettersHelper:
    def __init__(self, builder: 'TransitionTableBuilder', state: State, letters: tuple[Letter]):
        self._builder = builder
        self._state = state
        self._letters = letters

    def skip_right(self):
        for sigma in self._letters:
            self._builder[self._state, sigma] = self._state, sigma, RIGHT

    def skip_left(self):
        for sigma in self._letters:
            self._builder[self._state, sigma] = self._state, sigma, LEFT

    def change_state(self, state: State, direction: Direction = STAY, write: Union[str, Letter, None]=None):
        for sigma in self._letters:
            self._builder[self._state, sigma] = state, (sigma if write is None else write), direction


class TransitionTableBuilder(MutableMapping[TransitionTableEntryKey, TransitionTableEntryValue]):
    def __init__(self):
        self._dict: dict[TransitionTableEntryKey, TransitionTableEntryValue] = {}

    def __setitem__(self, k: _KT, v: _VT) -> None:
        self._dict[_ensure_key(k)] = _ensure_value(v)

    def __delitem__(self, k: _KT) -> None:
        del self._dict[_ensure_key(k)]

    def __getitem__(self, k: _KT) -> _VT:
        return self._dict[_ensure_key(k)]

    def __len__(self) -> int:
        return len(self._dict)

    def __iter__(self) -> Iterator[_KT]:
        return iter(self._dict)

    def __contains__(self, item: _KT) -> bool:
        return _ensure_key(item) in self._dict

    def __str__(self):
        return f"TransitionTableBuilder({self._dict})"

    def __repr__(self):
        return self.__str__()

    def keys(self):
        return self._dict.keys()

    def values(self):
        return self._dict.values()

    def items(self):
        return self._dict.items()

    def build(self,
              fill_missing_transitions: Optional[tuple[Iterable[State], Iterable[Letter], State]]
              ) -> TransitionTable:
        if fill_missing_transitions:
            states, letters, rej = fill_missing_transitions
            for q in states:
                for sigma in letters:
                    if (q, sigma) not in self:
                        self[(q, sigma)] = TransitionTableEntryValue(state=rej, letter=sigma, direction=STAY)
        return frozendict({k: v for k, v in self.items()})

    def on_state(self, state: Union[str, State]):
        """
        Note: if you want to use this with .accept_on or .reject_on,
        make sure you have set .accepting_state and .rejecting_state for
        this builder before doing so!
        """
        if not isinstance(state, State):
            state = State(state)
        return _TransitionTableBuilderStateHelper(self, state)


class TuringMachineBuilder:
    def __init__(self):
        self.input_alphabet: list[_Letter] = []
        self.tape_alphabet: list[_Letter] = []
        # noinspection PyTypeChecker
        self.blank_character: _Letter = None
        self.states: list[_State] = []
        self.accepting_state: _State = None
        self.rejecting_state: _State = None
        self.initial_state: _State = None
        self.delta: TransitionTableBuilder = TransitionTableBuilder()

    def build(self, fill_missing_transitions=False) -> TuringMachine:
        if self.blank_character is None:
            raise ValueError("must set blank_character")
        if self.rejecting_state is None:
            raise ValueError("must set rejecting_state")
        if self.accepting_state is None:
            raise ValueError("must set accepting_state")

        tape_alphabet = frozenset(map(Letter, self.tape_alphabet))
        states = frozenset(map(State, self.states))
        rejecting_state = State(self.rejecting_state)
        return TuringMachine(
            input_alphabet=frozenset(map(Letter, self.input_alphabet)),
            tape_alphabet=tape_alphabet,
            blank_character=Letter(self.blank_character),
            states=states,
            accepting_state=State(self.accepting_state),
            rejecting_state=rejecting_state,
            initial_state=State(self.initial_state),
            delta=self.delta.build(fill_missing_transitions=(
                (states, tape_alphabet, rejecting_state) if fill_missing_transitions else None
            ))
        )

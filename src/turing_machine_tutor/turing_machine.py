from typing import Callable, Any, Union

from attrs import define, field

from turing_machine_tutor.domain import Letter, State
from turing_machine_tutor.transition_table import TransitionTable, transition_table, TransitionTableEntryKey, \
    TransitionTableEntryValue


def _to_frozenset_with_cast(type_: type) -> Callable[[Any], frozenset]:
    return lambda it: frozenset(map(type_, it))


_to_frozenset_of_letters = _to_frozenset_with_cast(Letter)
_to_frozenset_of_states = _to_frozenset_with_cast(State)


@define(frozen=True, kw_only=True)
class TuringMachine:
    input_alphabet: frozenset[Letter] = field(converter=_to_frozenset_of_letters)
    tape_alphabet: frozenset[Letter] = field(converter=_to_frozenset_of_letters)
    blank_character: Letter = field(converter=Letter)
    states: frozenset[State] = field(converter=_to_frozenset_of_states)
    initial_state: State = field(converter=State)
    accepting_state: State = field(converter=State)
    rejecting_state: State = field(converter=State)
    delta: TransitionTable = field(converter=transition_table)

    @property
    def terminal_states(self):
        return {self.accepting_state, self.rejecting_state}

    @property
    def non_terminal_states(self):
        return self.states.difference(self.terminal_states)

    def get_transition(self, *args: Union[tuple[Any, Any], tuple[tuple], TransitionTableEntryKey]):
        k: TransitionTableEntryKey
        if len(args) > 1:
            k = TransitionTableEntryKey(state=args[0], letter=args[1])
        elif not isinstance(args[0], TransitionTableEntryKey):
            k = TransitionTableEntryKey(state=args[0][0], letter=args[0][1])
        elif isinstance(args[0], TransitionTableEntryKey):
            k = args[0]
        else:
            raise ValueError(f"not understood: get_transition{args}")
        if k.state in self.terminal_states:
            return None
        return self.delta[k]

    def __attrs_post_init__(self):
        # alphabets and letters
        if not self.tape_alphabet.issuperset(self.input_alphabet):
            raise ValueError(
                f"tape_alphabet ({self.tape_alphabet}) "
                f"should be a superset of "
                f"input_alphabet ({self.input_alphabet})")
        if self.blank_character in self.input_alphabet:
            raise ValueError(f"blank_character {repr(self.blank_character)} should not be in input_alphabet")
        if self.blank_character not in self.tape_alphabet:
            raise ValueError(f"blank_character {repr(self.blank_character)} should be in tape_alphabet")
        if self.rejecting_state == self.accepting_state:
            raise ValueError(
                f"rejecting_state should not be the same "
                f"as accepting_state, but both were {self.rejecting_state}")

        # states
        if self.accepting_state not in self.states:
            raise ValueError(f"accepting_state {self.accepting_state} should be in states {self.states}")
        if self.rejecting_state not in self.states:
            raise ValueError(f"rejecting_state {self.rejecting_state} should be in states {self.states}")
        if self.initial_state not in self.states:
            raise ValueError(f"initial_state {self.initial_state} should be in states {self.states}")

        # transition table
        k: TransitionTableEntryKey
        v: TransitionTableEntryValue

        for (k, v) in self.delta.items():
            if k.state not in self.states:
                raise ValueError(
                    f"found transition {k} -> {v} "
                    f"but {k.state} is not in state set {self.states}"
                )
            if k.letter not in self.tape_alphabet:
                raise ValueError(
                    f"found transition {k} -> {v} "
                    f"but {k.state} is not in tape_alphabet set {self.states}"
                )
            if v.state not in self.states:
                raise ValueError(
                    f"found transition {k} -> {v} "
                    f"but {v.state} is not in state set {self.states}"
                )
            if v.letter not in self.tape_alphabet:
                raise ValueError(
                    f"found transition {k} -> {v} "
                    f"but {v.state} is not in tape_alphabet set {self.states}"
                )

        missing_transitions = set(
            k for k in (
                TransitionTableEntryKey(state, letter)
                for state in self.non_terminal_states
                for letter in self.tape_alphabet
            )
            if k not in self.delta
        )

        if missing_transitions:
            raise ValueError(f"missing transitions: {missing_transitions}")

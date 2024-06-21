from dataclasses import dataclass

import jsonpickle
import json
from TuringMachine import TuringMachine
from next import next
from builtins import next as first  # builtins have a method named next but we already have a function named next

@dataclass
class _TuringMachineSerialization:
    states: set
    input_alphabet: set
    tape_symbols: set
    transitions: list[tuple[tuple[str, str], next]]
    initial_state: str
    accept_states: set
    reject_states: set


def serialize_turing_machine(turing_machine: TuringMachine):
    ser = _TuringMachineSerialization(
        states=turing_machine.states,
        input_alphabet=turing_machine.input_alphabet,
        tape_symbols=turing_machine.tape_alphabet,
        transitions=list(turing_machine.transitions.items()),
        initial_state=turing_machine.initial_state,
        accept_states=turing_machine.accept_states,
        reject_states=turing_machine.reject_states
    )
    return jsonpickle.encode(ser)


def _first_key_of(transitions):
    for k in transitions:
        return k
    return None


def _to_dict(items):
    return {k: v for k, v in items}


def deserialize_turing_machine(serialized_turing_machine):
    ser: _TuringMachineSerialization = jsonpickle.decode(serialized_turing_machine)
    tm = TuringMachine(
        states=ser.states,
        input_alphabet=ser.input_alphabet,
        tape_symbols=ser.tape_symbols,
        transitions=_to_dict(ser.transitions),
        initial_state=ser.initial_state,
        accept_states=ser.accept_states,
        reject_states=ser.reject_states
    )
    return tm


def _demonstrate_serialization_and_deserialization():
    tm = TuringMachine(
            states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
            input_alphabet={'0', '1'},
            tape_symbols={'0', '1', 'X', 'Y', 'B'},
            transitions={
                ('q0', '0'): next('q1', 'X', 'R'),  # Step 1 change 0 to X
                ('q0', 'Y'): next('q3', 'Y', 'R'),
                ('q1', '0'): next('q1', '0', 'R'),
                ('q1', '1'): next('q2', 'Y', 'L'),
                ('q1', 'Y'): next('q1', 'Y', 'R'),
                ('q2', '0'): next('q2', '0', 'L'),
                ('q2', 'X'): next('q0', 'X', 'R'),
                ('q2', 'Y'): next('q2', 'Y', 'L'),
                ('q3', 'Y'): next('q3', 'Y', 'R'),
                ('q3', 'B'): next('q4', 'B', 'L')
            },
            initial_state='q0',
            accept_states={'q4'},
            reject_states={'q5'}
        )

    serialized_tm = serialize_turing_machine(tm)
    print(serialized_tm)

    deserialized_tm = deserialize_turing_machine(serialized_tm)
    print(deserialized_tm)

if __name__ == "__main__":
    _demonstrate_serialization_and_deserialization()
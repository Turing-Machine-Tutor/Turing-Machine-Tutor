# Exercise 1 - basic Turing Machines

This code installs the library and checks it was set up correctly. Do not modify this code block.

```python
!git clone <git address> --branch 1.0.0
!  # more steps to include things...

import turing_machine_tutor as tmt

tmt.assert_version('1.0.0')  # ensure v1.0.0
```

```txt
Output [1]: 
You are running Turing Machine Tutor, version 1.0.0. Happy Turing-ing!
```

Upload `exercise1_tests.py`. You may read it if you want, but do not modify it. Your submission will be ran with the `exercise1_tests.py` file as provided to you.

Run this following code block (and do not modify it):

```python
import exercise1_tests as ex1
```

## Example

Let $\Sigma = \{0\},\;L = \{w\in\Sigma^*: \; |w|=1\}$. The following code defines $M_{00}$ an **incorrect** Turing Machine for $L$.  

```python
B = '_'  # you may change this, but make sure you're consistent and careful with it!

M0 = {
    'input_alphabet': ('0',),
    'tape_alphabet': ('0', B),
    'blank_character': B,
    'states': ('q0', 'q1', 'q_acc', 'q_rej'),
    'accepting_state': 'q_acc',
    'rejecting_state': 'q_rej',
    'initial_state': 'q0',
    delta: {
        ('0', 'q0'): ('0', 'q1', 'R'),
        (B, 'q0'): ('0', 'q_rej', 'R'),
        
        ('0', 'q1'): ('0', 'q_acc', 'R'),
        (B, 'q1'): ('0', 'q_rej', 'R')
    }
}
```

Run the tester on it and see it doesn't pass all tests:

```python
ex1.example.test(M0)
```

```
Output [2]:

+------+----------+--------+--------+
| word | expected | actual | result |
+------+----------+--------+--------+
| Ɛ    | accept   | accept | pass   |
+------+----------+--------+--------+
| 0    | accept   | accept | pass   |
+------+----------+--------+--------+
| 00   | accept   | reject | fail   |
+------+----------+--------+--------+
| 1    | accept   | accept | pass   |
+------+----------+--------+--------+
| 10   | accept   | reject | fail   |
+------+----------+--------+--------+
| 101  | reject   | reject | pass   |
+------+----------+--------+--------+
| 11   | accept   | reject | fail   |
+------+----------+--------+--------+
| 111  | reject   | reject | pass   |
+------+----------+--------+--------+
5/8 tests passed
```

The following is a **correct** Turing machine for $L$. It also demonstrates using `TuringMachineBuilder` we have created for you. Run it and see the output.

```python
B = '_'  # you may change this, but make sure you're consistent and careful with it!

def build_m01():
    builder = tmt.TuringMachineBuilder()
    builder.input_alphabet = ['0', '1']
    builder.blank_character = B 
    builder.tape_alphabet = ['0', '_']
    builder.states = ['q0', 'q1', 'q2', 'q_acc', 'q_rej']
    builder.accepting_state = q_acc
    builder.rejecting_state = q_rej
    builder.initial_state = q0
    
    for c in builder.input_alphabet:
        builder.delta[c, 'q0'] = 'q1', c, 'R'
        builder.delta[c, 'q1'] = 'q2', c, 'R'
        builder.delta[c, 'q2'] = 'q_rej', c, 'R'
    for i in ('q0', 'q1'):
    	builder.delta[B, 'q0'] =  'q_rej', B, 'R'
    builder.delta[B, 'q2'] = 'q_acc', B, 'R'
    return builder.build()

M01 = build_m01()
ex1.example.test(M01)
```



## Task 1 - a regular language

Create a Turing machine for the regular language $L=a^{2}a^*((cd)^*\cup (dc)^*)$.

```python

```

Run the tester:

```python
ex1.tast1.test(M1)
```



## Task 2 - a context-free language

## Task 3 - a non context-free language



## Task 4 - a machine for a DFA

Write the method `create_tm_for_dfa(dfa)` where `dfa` is a DFA. The DFA is given as a dictionary:

`initial: str, states: set[str], accepting_states: set[str], alphabet: set[str], delta: dict[tuple[str, str], str]`

```python
def create_tm_for_dfa(dfa):
    initial = dfa['initial']
    states = dfa['states']
    accepting_states = dfa['accepting_states']
    alphabet = dfa['alphabet']
    delta = dfa['delta']
    
```


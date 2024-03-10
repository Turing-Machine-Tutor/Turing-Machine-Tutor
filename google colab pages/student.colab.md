# `task1.py`

```python
import turing_machine_tutor as tmt
def tasks():
    import string
    import random
    
    def task1_isin(w):
        n = len(w)
        if n % 2 == 0:
            return False
        n /= 2
        expected = ('0',)*n + ('1',)*n
        return w == expected
    
    def generate_tests():
        # possibly also use random
        return ['0011', '0010', '01', '000111', '00110']
    
	task1 = tmt.Task(
        alphabet=['0','1']
    	name="0n1n",
        description="L=\{ 0^n1^n: n\in \mathbb{N} \}",
        test_method=task1_isin,
        test_generator=generate_tests
    )
    
	return [task1, ...]
```

# Colab file

## Useful Python concepts to know

* Sets (they are not lists!)
* Tuples (they are not lists!)
* kwargs
* Comperehesions
* f-strings

## Set up - don't change this code

Run this and upload `task1.tmt_task`.

```python
colab.upload()
```

```python

# TODO
import turing_machine_challenge as tmt

controller = TuringMachineController()
controller.import_tasks_from('task1.py', function_name='tasks')
```

Make sure it contains the challenges we have set up for you:

```python
controller.view_challenges()
```

| #    | Alphabet                    | Language                                                     |
| ---- | --------------------------- | ------------------------------------------------------------ |
| 1    | $\{ 0, 1 \}$                | $L=\{ 0^n1^n: n\in \mathbb{N} \}$                            |
| 2    | Letters `A`-`Z` (uppercase) | Palindromes of even size                                     |
| 3    | $\{ A,B,\dots, Z, @  \}$    | $L=\{ \sigma_1\dots\sigma_n@\sigma'_1\dots\sigma'_n \}$ where $\forall i: \sigma_i, \sigma'_i \neq @\wedge \sigma_i \neq \sigma'_i$ |

## How to build a Turing Machine

### Option 1 - plain Turing Machine

Use the constructor for `TuringMachine`:

```python
TuringMachine(
	states: set[str],
    input_alphabet: set[str],
    tape_alphabet: set[str],
    blank: str,
    
    # (state, letter) -> (state, letter, 'R' | 'L' | 'S')
    transitions: dict[tuple[str, str], tuple[str, str, str]],
    initial_state: str,
    accepting_state: str,
    rejecting_state: str
)
```

Wherever the expected type is `set`, you may use any Python Iterable, such as list or generator, but it's recommended to use set.

**Note: always** pass the arguments as keyword arguments (kwargs), that is, with `argname=`.  

### Important

This **does not** mean you need to write everything yourself. For example, some alphabets may have dozens of characters - you shouldn't have to write them yourself. The whole point of using Python is that you may understand the logic of how to build the Turing machine and have the code generate the machine for you. For example, the code below defines a random meaningless Turing machine that has dozens of states, input characters and tape characters.

```python
import random
import string
AZ = list(string.ascii_uppercase) #'A', 'B', ..., 'Z'
states = [f'q_{i}' for i in range(20)]
initial, acc, rej = 'q_0', 'q_12', 'q_14'
B = '_'
tape_characters = AZ + [B, '*']
def random_transition():
    return (random.choice(states), random.choice(tape_alphabet), random.choice())
delta = {
    (q, sigma): random_transition()
    for q 
}

tm = TuringMachine(
    states: set(states),
    input_alphabet: set(AZ),
    tape_alphabet: set(tape_characters),
    blank: B,
    transitions: delta,
    initial_state: 'q_0',
    accepting_state: 'q_14',
    rejecting_state: 'q_12'
)
```

Note: even though the transitions are defined randomly, they are only defined once. This does not mean that the same Turing machine may have a different transition for the same combination of state and letter. See the code below:

```python
tran = tm.delta['q_5', 'G']
ok = True
for _ in range(1000):
    if tm.delta['q_5', 'G'] == tran:
        ok = False
if ok:
    print("once the TM is created, the delta table does not change.")
else:
    print("This message should never be printed.")
```



You may also want to leave some transitions undefined, in which case they will go to the rejecting state. By default, the `TuringMachine` constructor expects you to have a **complete** transition table, but if you want it create a transition into the rejecting state for every missing entry in the transition table, add `complete_transitions_table=True` to the constructor call.

### Option 2 - combining Turing Machines

If you create two or more instances of TuringMachine, you may combine them:

```python
tm4 = tmt.combine(tm1, tm2, tm3, tm4)
```

### Option 3 - combining with while condition

```python
tmt_w = tmt.while_(tmt1, tmt2, tm3, tm4)
```

Notice the underscore in `while_`. This is because `while` is a reserved word in Python.

## Registering

Once you have your solution object, you may register it as the solution for the problem with the controller object:

```python
controller.register_solution('0n1n', tm1)
```

## View diagram

You may view your Machine as a diagram:

```python
tmt.diagrams.show(tm1)
```

## Running & visualizing

You may run a Turing machine on a word by creating an object representing it:

```python
run = controller.run('0n1n', '000110')
```

You may view the run's current configuration:

```
run.view_configuration()
```

Note that `run.terminated` will be False and `run.accepted` will be None:

```
run.terminated, run.accepted  # False, None
```

You may step through the run:

```
run.step()
```

And view the result:

```
run.view_configuartion()
```

You may run until termination:

```python
run.run_to_termination()
```

And then see it was complete:

```python
run.terminated, run.accepted  # True, False
```

### Testing

For every decidable language, there exist infinitely many Turing Machines that decide it. We do **not** check your Turing Machine by comparing it to a specific "one correct" Turing machine. Instead, we run it against a series of test inputs. 

You may test your Turing Machine with tests defined by the TA. Depending on the TA's decisions, the tests may either be constant and predefined, may be randomly generated, or a combination of both. Every machine needs to pass all its test to be considered correct; after all, if $L(M) \neq L$, then $M$ does not decide $L$!

Your Turing Machine needs to **decide** the problem and not only **accept** it. That means that it must terminate on **every** input over the input alphabet $\Sigma$. If $w\notin L$, it may **not** run forever.

**The halting problem**, learned in this course, proves that there is no algorithmic way to ensure a given machine $M$ terminates for every input. This means that there is no Turing machine $M_H$ that can look at the structure of a Turing machine $M$ and determines if it always terminates for any input - such a machine $M_H$ cannot exist. Likewise, since Python is Turing-complete (see: Church-Turing thesis), this means that we have no way to determine for every machine if it stops for every input in Python either, that is the following method **can not exist, no matter which great programmer will try**:

```python
def halts_for_every_possible_input(turing_machine): ...
```

**However,** we test if your machine terminates by limiting the amount of steps it's allowed to take. That is, for every task, the TA has defined a limit of steps, that if your machine doesn't halt, we assume it's probably stuck. If your machine was given a word with length 10 and takes one million steps, then perhaps it will terminate the next step, but probably not. And even if your machine will take one million and one steps to correctly decide a 10-character word, that probably means you have room for improvement.
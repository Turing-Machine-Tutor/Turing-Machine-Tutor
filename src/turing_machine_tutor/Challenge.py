from typing import Callable, Union, Optional

from attr import define, field
from tabulate import tabulate

from turing_machine_tutor.domain import Word

from inspect import cleandoc as trim_indent  # use to trim multiline string

from turing_machine_tutor.turing_machine import TuringMachine
from turing_machine_tutor.turing_machine_run import TuringMachineRun
from simple_chalk import chalk

_PASSED = chalk.green.bold("✔ PASSED")
_FAILED = chalk.red.bold("❌ FAILED")

DID_NOT_TERMINATE = "Did not terminate"


@define(frozen=True)
class SingleTestResult:
    word: Word
    expected: bool
    actual: Union[bool, str]
    run: TuringMachineRun

    @property
    def correct(self):
        return self.actual == self.expected

    def correctness_pretty_str(self):
        if self.correct:
            return _PASSED
        return _FAILED


def as_acc_rej(t: Union[bool, str]):
    return "Did not terminate" if t == DID_NOT_TERMINATE else "accept" if t else "reject"


@define
class MultiTestResult:
    results: tuple[SingleTestResult]

    @property
    def did_pass(self):
        return all(t.correct for t in self.results)

    @property
    def amount_passed(self):
        return sum(1 for t in self.results if t.correct)

    @property
    def test_amount(self):
        return len(self.results)

    @property
    def passed_ratio(self):
        return self.amount_passed / self.test_amount

    def pretty_str(self, sort_column: Optional[int] = None, sort_desc=False):
        table = [
            [i, res.word, as_acc_rej(res.expected), as_acc_rej(res.actual), res.correctness_pretty_str()]
            for (i, res) in enumerate(self.results)
        ]
        if sort_column is not None:
            table.sort(key=lambda row: row[sort_column], reverse=sort_desc)
        table_str = tabulate(table, headers=["#", "word", "expected", "actual", "result"], tablefmt="grid")
        bottom1 = f"passed {self.amount_passed}/{self.test_amount} tests ({self.passed_ratio * 100:.2f}%)"
        if self.did_pass:
            bottom2 = _PASSED + ": all tests passed. Good job!"
        else:
            bottom2 = _FAILED + f": some tests didn't pass. Must pass {chalk.bold.underline('all')} tests."
        return '\n'.join([table_str, bottom1, bottom2])


@define(frozen=True)
class Challenge:
    short_name: str
    description: str = field(converter=trim_indent)
    alphabet: tuple[str]
    validator: Callable[[Word], bool]
    words: tuple[Word] = field(converter=lambda x: tuple(map(Word, x)))

    def test_machine(self, machine: TuringMachine, step_limit=10000) -> MultiTestResult:
        return MultiTestResult(tuple(self._test_machine_on_word(machine, word, step_limit) for word in self.words))

    def _test_machine_on_word(self, machine: TuringMachine, word: Word, step_limit=10000) -> SingleTestResult:
        run = TuringMachineRun(machine, word)
        run.run_until_terminated(step_limit)
        actual = run.accepted if run.is_terminal else DID_NOT_TERMINATE
        expected = self.validator(word)
        return SingleTestResult(word=word, expected=expected, actual=actual, run=run)

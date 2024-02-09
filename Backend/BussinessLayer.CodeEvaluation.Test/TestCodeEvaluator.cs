using BussinessLayer.CodeEvaluation.Impl;
using BussinessLayer.CodeEvaluation.Interfaces;
using BussinessLayer.TuringMachines.Interfaces;

namespace BussinessLayer.CodeEvaluation.Test
{
    [TestFixture]
    public class Tests
    {
        [Test]
        public void TestTuringMachineCreation()
        {
            ICodeEvaluator e = new CodeEvaulator();
            string code = @"
def build():
    # Example Turing Machine parameters
    input_alphabet = ['0', '1']
    tape_alphabet = ['0', '1', 'B']  # B represents blank symbol
    blank = 'B'
    states = ['q0', 'q1', 'acc', 'rej']
    initial_state = 'q0'
    acc = 'acc'
    rej = 'rej'
    delta = {
        ('q0', '0'): ('0', 'q1', 'R'),
        ('q0', '1'): ('1', 'q1', 'R'),

        ('q1', '0'): ('0', 'q0', 'L'),
        ('q1', '1'): ('1', 'q0', 'L'),

        ('q0', 'B'): ('B', 'acc', 'S'),
        ('q1', 'B'): ('B', 'rej', 'S')
    }

    return {
        'input_alphabet': input_alphabet,
        'tape_alphabet': tape_alphabet,
        'blank': blank,
        'states': states,
        'initial_state': initial_state,
        'acc': acc,
        'rej': rej,
        'delta': delta
    }
";
            ITuringMachine res = e.Run(code);

            Assert.That(res, Is.Not.Null);

            Assert.That(res.InputAlphabet, Is.Not.Null);
            Assert.That(res.InputAlphabet.Count, Is.EqualTo(2));
            Assert.That(res.InputAlphabet, Contains.Item("0").And.Contains("1"));

            Assert.That(res.TapeAlphabet, Is.Not.Null);
            Assert.That(res.InputAlphabet.All(res.TapeAlphabet.Contains));
            Assert.That(res.TapeAlphabet.Count, Is.EqualTo(3));

            Assert.That(res.BlankCharacter, Is.EqualTo("B"));
            Assert.That(res.TapeAlphabet, Contains.Item("B"));

            Assert.That(res.InitialState, Is.EqualTo("q0"));
            Assert.That(res.RejectingState, Is.EqualTo("rej"));
            Assert.That(res.AcceptingState, Is.EqualTo("acc"));

            Assert.That(res.Delta, Is.Not.Null);
            Assert.That(res.Delta.Count, Is.EqualTo(res.TapeAlphabet.Count * res.NonTerminalStates.Count()));

            TransitionInput q0_B = new TransitionInput("q0", "B");
            Assert.That(res.Delta, Contains.Key(q0_B));
            Assert.That(res.Delta[q0_B], Is.EqualTo(new TransitionOutput("B", "acc", TransitionDirection.Stay)));
        }
    }
}

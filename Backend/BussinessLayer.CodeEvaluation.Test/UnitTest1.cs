using BussinessLayer.CodeEvaluation.Impl;
using BussinessLayer.CodeEvaluation.Interfaces;

namespace BussinessLayer.CodeEvaluation.Test
{
    [TestFixture]
    public class Tests
    {
        [Test]
        public void MyTest()
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
            var res = e.Run(code);
            
        }
    }
}

using BussinessLayer.TuringMachines.Impl;
using BussinessLayer.TuringMachines.Interfaces;
using NUnit.Framework;

namespace BussinessLayer.TuringMachines.Test
{
    [TestFixture]
    public class TuringMachineTest
    {
        [Test]
        public void TestCreation()
        {
            // L = {w over 0,1: |w| % 2 == 0 }
            string initial = "q_even";
            string acc = "q_acc";
            string rej = "q_rej";

            string[] states = { initial, "q_odd", acc, rej };
            string[] inputAlphabet = { "0", "1" };
            string blank = "B";
            string[] tapeAlphabet = { "0", "1", blank };

            var delta = TuringMachine.DeltaDictFromTuples(
                ("q_even", "0", "q_odd", "0", TransitionDirection.Right),
                ("q_even", "1", "q_odd", "1", TransitionDirection.Right),
                ("q_odd", "0", "q_even", "0", TransitionDirection.Right),
                ("q_odd", "1", "q_even", "1", TransitionDirection.Right),
                ("q_even", blank, acc, blank, TransitionDirection.Stay),
                ("q_odd", blank, rej, blank, TransitionDirection.Stay)
            );

            ITuringMachine machine = new TuringMachine(
                states: states, inputAlphabet: inputAlphabet, tapeAlphabet: tapeAlphabet,
                blankCharacter: blank, rejectingState: rej, acceptingState: acc,
                initialState: initial, delta: delta
            );

            Assert.That(
                machine.Transition(new("q_odd", "0")),
                Is.EqualTo(new TransitionOutput("q_even", "0", TransitionDirection.Right))
            );
            Assert.That(
                machine.Transition(new("q_odd", "B")),
                Is.EqualTo(new TransitionOutput(rej, blank, TransitionDirection.Stay))
            );
        }
    }
}

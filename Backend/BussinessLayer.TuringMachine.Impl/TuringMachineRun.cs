using BussinessLayer.TuringMachines.Interfaces;
using System.Collections.Immutable;
using System.Diagnostics;
using System.Diagnostics.CodeAnalysis;

namespace BussinessLayer.TuringMachines.Impl
{
    public class TuringMachineRun : ITuringMachineRun
    {
        public ITuringMachine TuringMachine { get; private init; }
        public IReadOnlyList<string> Input { get; private init; }

        public IReadOnlyList<string> Tape => tape;

        private List<string> tape;

        public string Blank => TuringMachine.BlankCharacter;

        public string State { get; private set; }

        public int TapeHeadIndex { get; private set; }

        public bool? Accepted =>
            Terminated ? State == TuringMachine.AcceptingState : null;

        public bool Terminated => TuringMachine.IsTerminalState(State);

        public string CurrentCharacter
        {
            get => Tape[TapeHeadIndex];
            private set => tape[TapeHeadIndex] = value;
        }

        public TuringMachineRun(
            ITuringMachine turingMachine,
            IReadOnlyList<string> input
        )
        {
            TuringMachine = turingMachine;
            input = input.ToImmutableList();
            tape = [.. input, Blank];
            Reset();
        }

        public void Reset()
        {
            tape = [.. Input, Blank];
            State = TuringMachine.InitialState;
            TapeHeadIndex = 0;
        }

        public void RunToCompletion(uint? stepLimit = null)
        {
            for (uint i = 0; (stepLimit == null || i < stepLimit) && !Terminated; i++)
            {
                Step();
            }
        }

        public void Step()
        {
            if (Terminated)
            {
                throw new InvalidOperationException("Turing machine terminated.");
            }
            TransitionInput current = new TransitionInput(State, CurrentCharacter);
            TransitionOutput next = TuringMachine.Transition(current);

            State = next.State;
            CurrentCharacter = next.TapeLetter;
            if (TapeHeadIndex == 0 && next.Direction == TransitionDirection.Left)
            {
                return;
            }
            TapeHeadIndex += (int)next.Direction;
        }
    }
}

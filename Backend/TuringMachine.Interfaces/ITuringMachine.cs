using System.Collections.ObjectModel;

namespace BussinessLayer.TuringMachines.Interfaces
{
    public enum TransitionDirection
    {
        Left = -1, Right = 1, Stay = 0
    }

    public record struct TransitionInput(string State, string TapeLetter)
    {
        public override string ToString() => $"(state={State}, letter={TapeLetter})";
    }
    public record struct TransitionOutput(
        string State, string TapeLetter,
        TransitionDirection Direction)
    {
        public override string ToString() => $"(toState={State}, write {TapeLetter}, {Direction})";
    }

    public interface ITuringMachine
    {
        public IReadOnlyList<string> States { get; }
        public IReadOnlyList<string> InputAlphabet { get;  }
        public IReadOnlyList<string> TapeAlphabet { get; }
        public string AcceptingState { get; }
        public string RejectingState { get; }
        public string InitialState { get; }
        public string BlankCharacter { get; }
        public IDeltaDict Delta { get; }

        public TransitionOutput Transition(TransitionInput input);
        public IEnumerable<string> NonTerminalStates { get; }
        public bool IsTerminalState(string state);
    }
}

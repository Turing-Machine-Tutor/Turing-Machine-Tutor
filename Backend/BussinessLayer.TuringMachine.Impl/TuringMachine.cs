using BussinessLayer.TuringMachines.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BussinessLayer.TuringMachines.Impl
{
    public partial class TuringMachine : ITuringMachine
    {
        public IReadOnlyList<string> States { get; private init; }
        public IReadOnlyList<string> InputAlphabet { get; private init; }
        public IReadOnlyList<string> TapeAlphabet { get; private init; }
        public string AcceptingState { get; private init; }
        public string RejectingState { get; private init; }
        public string InitialState { get; private init; }
        public string BlankCharacter { get; private init; }
        public IDeltaDict Delta { get; private init; }

        public IEnumerable<string> NonTerminalStates => States.Where(x => x != AcceptingState && x != RejectingState);


        public TuringMachine(IReadOnlyList<string> states, IReadOnlyList<string> inputAlphabet, IReadOnlyList<string> tapeAlphabet, string acceptingState, string rejectingState, string initialState, string blankCharacter, IDeltaDict delta)
        {
            States = states;
            InputAlphabet = inputAlphabet;
            TapeAlphabet = tapeAlphabet;
            AcceptingState = acceptingState;
            RejectingState = rejectingState;
            InitialState = initialState;
            BlankCharacter = blankCharacter;
            Delta = delta;
            Validate();
        }


        public TransitionOutput Transition(TransitionInput input)
        {
            return Delta[input];
        }

        public static IDeltaDict DeltaDictFromTuples(
            params (string state, string character, string nextState, string writeCharacter,  TransitionDirection direction)[] tuples    
        )
        {
            Dictionary<TransitionInput, TransitionOutput> res = new();
            foreach (var (state, character, nextState, writeCharacter, direction)
                in tuples )
            {
                TransitionInput input = new(state, character);
                TransitionOutput output = new(nextState, writeCharacter, direction);
                if(res.ContainsKey(input))
                {
                    TransitionOutput otherOutput = res[input];
                    throw new ArgumentException(
                        $"State-character tuple {input} has more than one " +
                        $"rule: {output}, {otherOutput}"
                    );
                }
                res[input] = output;
            }
            return res;
        }

        public bool IsTerminalState(string state) => 
            state.Equals(AcceptingState) || state.Equals(RejectingState);


        private partial void Validate();
    }
}

using BussinessLayer.TuringMachines.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BussinessLayer.TuringMachines.Impl
{
    public partial class TuringMachine
    {
        private partial void Validate()
        {
            List<ITuringMachineStructureProblem> problems = [];

            CheckTapeAlphabetSupersetOfInputAlphabet(problems);
            CheckBlank(problems);
            CheckNoNullStates(problems);
            CheckNoNullCharacters(problems);
            CheckMissingTransitions(problems);
            CheckLegalTransitions(problems);
            
            if(problems.Count > 0)
            {
                throw new TuringMachineStructureException(problems);
            }
        }

        private void CheckBlank(List<ITuringMachineStructureProblem> problems)
        {
            if(InputAlphabet.Contains(BlankCharacter))
            {
                problems.Add(null); // TODO
            }
        }

        private void CheckTapeAlphabetSupersetOfInputAlphabet(List<ITuringMachineStructureProblem> problems)
        {
            // TODO
        }

        private void CheckNoNullCharacters(List<ITuringMachineStructureProblem> problems)
        {
            if(TapeAlphabet.Contains(null))
            {
                problems.Add(new NullNotAllowedAsCharacter());
            }
        }

        private void CheckNoNullStates(List<ITuringMachineStructureProblem> problems)
        {
            if(States.Contains(null))
            {
                problems.Add(new NullNotAllowedAsState());
            }
        }

        private void CheckLegalTransitions(List<ITuringMachineStructureProblem> problems)
        {
            foreach(var (input, output) in Delta)
            {
                if(!TapeAlphabet.Contains(input.TapeLetter) || 
                    !NonTerminalStates.Contains(input.State))
                {
                    problems.Add(new MalformedTransitionInputInDelta(input.State, input.TapeLetter));
                }

                if(!TapeAlphabet.Contains(output.TapeLetter) || 
                    !States.Contains(output.State))
                {
                    problems.Add(
                        new MalformedTransitionOutputInDelta(output.State, output.TapeLetter)
                    );
                }
            }
        }

        private void CheckMissingTransitions(List<ITuringMachineStructureProblem> problems)
        {
            foreach (var state in NonTerminalStates)
            {
                foreach (var tapeCharacter in TapeAlphabet)
                {
                    TransitionInput input = new(state, tapeCharacter);
                    if (!Delta.ContainsKey(input))
                    {
                        problems.Add(new MissingTransitionInputInDelta(state, tapeCharacter));
                    }
                }
            }
        }
    }
}

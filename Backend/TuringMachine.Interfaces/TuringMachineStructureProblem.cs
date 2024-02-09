using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BussinessLayer.TuringMachines.Interfaces
{
    public class TuringMachineStructureException(IReadOnlyCollection<ITuringMachineStructureProblem> problems) : Exception
    {
        public IReadOnlyCollection<ITuringMachineStructureProblem> Problems { get; } = problems.ToList();
    }

    public interface ITuringMachineStructureProblem { }

    public record class MissingTransitionInputInDelta(
        string State, string Character 
    ): ITuringMachineStructureProblem;

    public record class MalformedTransitionInputInDelta(
        string State, string Character
    ) : ITuringMachineStructureProblem;

    public record class MalformedTransitionOutputInDelta(
        string State, string Character
    ): ITuringMachineStructureProblem;

    public record class TransitionInputIllegalState(
        TransitionInput Input, string State
    ) : ITuringMachineStructureProblem;

    public record class TransitionOutputIllegalState(
        TransitionOutput Output, string State
    ) : ITuringMachineStructureProblem;

    public record class TransitionInputStateIsTerminal(
        TransitionInput Input, string State
    ): ITuringMachineStructureProblem;


    public record class TransitionInputIllegalCharacter(
        TransitionInput Input, string Character
    ) : ITuringMachineStructureProblem;

    public record class TransitionOutputIllegalCharacter(
        TransitionOutput Output, string Character
    ) : ITuringMachineStructureProblem;

    public class NullNotAllowedAsState: ITuringMachineStructureProblem;
    public class NullNotAllowedAsCharacter: ITuringMachineStructureProblem;

}

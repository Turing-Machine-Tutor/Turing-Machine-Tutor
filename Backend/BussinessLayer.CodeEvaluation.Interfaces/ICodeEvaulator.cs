using BussinessLayer.TuringMachines.Interfaces;

namespace BussinessLayer.CodeEvaluation.Interfaces
{
    public interface ICodeEvaluator
    {
        ITuringMachine Run(string code);

    }
}

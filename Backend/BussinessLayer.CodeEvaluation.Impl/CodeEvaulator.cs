using BussinessLayer.CodeEvaluation.Interfaces;
using BussinessLayer.TuringMachines.Impl;
using BussinessLayer.TuringMachines.Interfaces;

namespace BussinessLayer.CodeEvaluation.Impl
{
    public class CodeEvaulator: ICodeEvaluator
    {

        public ITuringMachine Foo()
        {
            return new TuringMachine();
        }

    }
}

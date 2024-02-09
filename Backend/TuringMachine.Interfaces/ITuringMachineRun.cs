using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BussinessLayer.TuringMachines.Interfaces
{
    public interface ITuringMachineRun
    {
        public ITuringMachine TuringMachine { get; }
        public IReadOnlyList<string> Input { get; }

        public IReadOnlyList<string> Tape { get; }
        public string State { get; }
        public int TapeHeadIndex { get; }
        public string CurrentCharacter { get; }

        public bool? Accepted { get; }
        public bool Terminated { get; }

        public void Reset();
        public void Step();
        public void RunToCompletion(uint? stepLimit = null);
    }
}

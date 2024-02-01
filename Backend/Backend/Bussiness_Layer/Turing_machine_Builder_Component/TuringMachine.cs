using System;
using System.ComponentModel.DataAnnotations.Schema;
using System.Reflection.PortableExecutable;

namespace Backend.Bussiness_Layer.Turing_machine_Builder_Component
{
    public class TuringMachine
    {
        public IEnumerable<string> InputAlphabet { get; set; }
        public IEnumerable<string> TapeAlphabet { get; set; }
        public string Blank { get; set; }
        public IEnumerable<string> States { get; set; }
        public string InitialState { get; set; }
        public string AcceptState { get; set; }
        public string RejectState { get; set; }
        public Dictionary<(string, string), (string, string, string)> Delta { get; set; }




        // Tape and Head objects
        public List<char> Tape { get; set; }
        public int Head { get; set; }

        //     tape and head values

        public string currentState;
        public bool isHalted;

        /// <summary>
        /// return: 
        /// 3 in case accept
        /// 2 in case of reject
        /// 1 in case of successfull step
        /// 0 if machine already halted
        /// -1 invalid head position
        /// </summary>
        /// <returns></returns>
        public int Step()
        {
            if(Head < 0 || Head >= Tape.Count)
            {
                Head = -1;
                currentState = RejectState;
                //return -1;
                throw new Exception("invalid head position");
            }
            if(currentState == AcceptState || currentState == RejectState)
            {
                return 0;// turing machine already halted
            }

            // Retrieve the transition rule based on the current state and symbol
            var key = (currentState, Tape[Head].ToString());
            if (Delta.TryGetValue(key, out var transition))
            {
                // Apply the transition rule
                Tape[Head] = transition.Item1[0];
                //Tape.WriteSymbol(Head.Position, transition.Item1);
                if (transition.Item3[0] == 'R')
                    Head++;
                else if (transition.Item3[0] == 'L')
                    Head--;
                // else 'S' then Head stays the same
                //Head.Move(transition.Item3);
                currentState = transition.Item2;
                if(currentState == AcceptState)
                {
                    return 3;
                }
                else if(currentState == RejectState)
                {
                    return 2;
                }
                return 1;
                //Tape.UpdateHaltState(AcceptState, RejectState, transition.Item2);
            }
            else
            {
                // No transition rule found, transition to reject state
                Head = -1;
                currentState = RejectState;
                //Tape.UpdateHaltState(RejectState);
                //return -1;
                throw new Exception("No transition rule found, transition to reject state");
            }
        }
        

        public bool Run(string input)
        {
            Tape = ("B"+input+"B").ToCharArray().ToList();
            currentState = InitialState;
            Head = 1;

            int len = Tape.Count;
            try
            {
                for (int i = 0; i < len; i++)
                {
                    if (currentState == AcceptState)
                    {
                        return true;
                    }
                    else if (currentState == RejectState)
                    {
                        return false;
                    }
                    int result = Step();
                    if(result == 3)
                    {
                        return true;
                    }
                    else if(result == 2)
                    {
                        return false;
                    }
                }
                return false;
            }
            catch(Exception e) 
            {
                return false;
            }
            
        }

    }
}

using Newtonsoft.Json;
using System.Text.RegularExpressions;

namespace Frontend
{
    public static class TuringMachineBuilder
    {

        public static TuringMachine Parse(string code)
        {
            code = code.Replace("\r", "");
            var lines = code.Split("\n");
            string result = "";
            foreach (var l in lines)
            {
                var line = l.Trim();
                if (line == "")
                    continue;
                if (line[0] == '#' || line == "def build():")
                    continue;
                var res = "";
                if (line.IndexOf("#") != -1)
                    res = line.Split("#")[0].Trim();
                else
                    res = line;
                if (line.Contains("input_alphabet") ||
                    line.Contains("tape_alphabet") ||
                    line.Contains("blank") ||
                    line.Contains("states") ||
                    line.Contains("initial_state") ||
                    (line.Contains("acc") && line.Contains("=")) ||
                    (line.Contains("rej") && line.Contains("=")) ||
                    line.Contains("delta")
                    )
                {
                    result += "#";
                }
                result += res;
            }

            var pythonCodeLines = result.Split("#");

            ////////////////////////
            ///
            var turingMachine = new TuringMachine();
            var deltaDict = new Dictionary<(string, char), (char, string, char)>();
            lines = pythonCodeLines;
            foreach (var line in lines)
            {
                // Remove comments at the end of the line
                var cleanLine = Regex.Replace(line, "#.*$", "").Trim();

                if (string.IsNullOrWhiteSpace(cleanLine) || cleanLine.Trim().StartsWith("def"))
                    continue;


                // Remove all white spaces
                cleanLine = cleanLine.Replace(" ", "");

                var parts = cleanLine.Split('=').Select(part => part.Trim()).ToArray();

                if (parts.Length == 2)
                {
                    var variableName = parts[0];

                    if (variableName == "delta")
                    {
                        
                        // Handle special case for delta
                        var deltaCode = parts[1].Trim().TrimStart('{').TrimEnd('}');

                        var transitions = deltaCode.Split("),(");


                        
                        var delta = new Dictionary<(string, string), (string, string, string)>();

                        //var transitions = deltaCode.Replace("[", "").Replace("]", "").Split(',');
                        foreach (var transition in transitions)
                        {
                            var tr = transition.Replace("(", "").Replace(")", "");
                            var parts1 = tr.Split(':');
                            var state = parts1[0].Split(',');
                            var inputSymbol = state[1];
                            var writeSymbol = parts1[1].Split(',')[0];
                            var nextState = parts1[1].Split(',')[1];
                            var move = parts1[1].Split(',')[2];
                            delta.Add((state[0], inputSymbol), (writeSymbol, nextState, move));
                        }

                        // Set the Delta property after parsing
                        turingMachine.Delta = delta;
                    }
                    else
                    {
                        // Handle other parameters
                        var value = parts[1].Replace("'", "").Replace("[", "").Replace("]", "");
                        var elements = value.Split(',');

                        switch (variableName)
                        {
                            case "input_alphabet":
                                turingMachine.InputAlphabet = elements;
                                break;
                            case "tape_alphabet":
                                turingMachine.TapeAlphabet = elements;
                                break;
                            case "blank":
                                turingMachine.Blank = elements[0];
                                break;
                            case "states":
                                turingMachine.States = elements;
                                break;
                            case "initial_state":
                                turingMachine.InitialState = elements[0];
                                break;
                            case "acc":
                                turingMachine.AcceptState = elements[0];
                                break;
                            case "rej":
                                turingMachine.RejectState = elements[0];
                                break;
                        }
                    }
                }
            }

            return turingMachine;
        }
    }
}

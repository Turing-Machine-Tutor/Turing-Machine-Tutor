
using BussinessLayer.CodeEvaluation.Interfaces;
using BussinessLayer.TuringMachines.Impl;
using BussinessLayer.TuringMachines.Interfaces;
using IronPython.Runtime;
using static IronPython.Modules._ast;

namespace BussinessLayer.CodeEvaluation.Impl
{
    public class CodeEvaulator : ICodeEvaluator
    {
        public ITuringMachine Run(string code)
        {
            var engine = IronPython.Hosting.Python.CreateEngine();
            var scope = engine.CreateScope();
            engine.Execute(code, scope);
            
            if(!scope.ContainsVariable("build"))
            {
                throw new Exception("should have build function");
            }

            dynamic build = scope.GetVariable("build");
            CheckType<PythonFunction>(
                build,
                "build should be a function"
            );

            PythonDictionary dict = CheckType<PythonDictionary>(
                   build(), "build() needs to return a dictionary"
            );

            return new TuringMachine(
                inputAlphabet: ExtractInputAlphabet(dict),
                tapeAlphabet: ExtractTapeAlphabet(dict),
                blankCharacter: ExtractBlankCharacter(dict),
                acceptingState: ExtractAcceptingState(dict),
                rejectingState: ExtractRejectingState(dict),
                initialState: ExtractInitialState(dict),
                delta: ExtractDelta(dict),
                states: ExtractStates(dict)
            );
        }

        private IReadOnlyList<string> ExtractStates(PythonDictionary dict)
        {
            System.Collections.IEnumerable inputAlphabet = CheckType<System.Collections.IEnumerable>(
                dict.get("states"),
                "states must be enumerable (tuple, string, set etc)"
            );

            return inputAlphabet
                        .Cast<object>()
                        .Select(x => CheckType<string>(x, "states must be all strings"))
                        .ToList();
        }

        private IReadOnlyDictionary<TransitionInput, TransitionOutput> ExtractDelta(PythonDictionary dict)
        {
            PythonDictionary delta = CheckType<PythonDictionary>(dict.get("delta"), "delta must be dictionary");

            Dictionary<TransitionInput, TransitionOutput> ret = new Dictionary<TransitionInput, TransitionOutput>();

            foreach(var pair in delta)
            {
                PythonTuple key = CheckType<PythonTuple>(pair.Key, "key must be tuple");
                var keyAsList = CheckStringList(key, "delta dict key");
                if(keyAsList.Count != 2)
                {
                    throw new Exception("delta key must be tuple of length 2");
                }

                PythonTuple value = CheckType<PythonTuple>(pair.Value, "value must be tuple");
                var valueAsList = CheckStringList(pair.Value, "delta dict value");
                if(valueAsList.Count != 3)
                {
                    throw new Exception("delta value must be tuple of length 3");
                }

                string directionAsString = valueAsList[2];
                TransitionDirection dir;
                if("L".Equals(directionAsString))
                {
                    dir = TransitionDirection.Left;
                } else if ("R".Equals(directionAsString))
                {
                    dir = TransitionDirection.Right;
                } else if("S".Equals(directionAsString))
                {
                    dir = TransitionDirection.Stay;
                } else
                {
                    throw new Exception("third tuple element must be 'L', 'S' or 'R'");
                }

                ret.Add(
                    new TransitionInput(keyAsList[0], keyAsList[1]),
                    new TransitionOutput(valueAsList[0], valueAsList[1], dir)
                );
            }

            return ret;
        }

        private string ExtractInitialState(PythonDictionary dict)
        {
            return CheckType<string>(dict.get("initial_state"), "initial_state must be string");
        }

        private string ExtractRejectingState(PythonDictionary dict)
        {
            return CheckType<string>(dict.get("rej"), "rej must be string");
        }

        private string ExtractAcceptingState(PythonDictionary dict)
        {
            return CheckType<string>(dict.get("acc"), "acc must be string");
        }

        private string ExtractBlankCharacter(PythonDictionary dict)
        {
            return CheckType<string>(dict.get("blank"), "blank must be string");
        }

        private IReadOnlyList<string> ExtractTapeAlphabet(PythonDictionary dict)
        {
            System.Collections.IEnumerable tapeAlphabet = CheckType<System.Collections.IEnumerable>(
                    dict.get("tape_alphabet"),
                    "tape_alphabet must be iterable"
                );

            return tapeAlphabet
                        .Cast<object>()
                        .Select(x => CheckType<string>(x, "tape_alphabet must be all strings"))
                        .ToList();
        }

        private IReadOnlyList<string> ExtractInputAlphabet(PythonDictionary dict)
        {
            System.Collections.IEnumerable inputAlphabet = CheckType<System.Collections.IEnumerable>(
                dict.get("input_alphabet"),
                "input_alphabet must be enumerable (tuple, string, set etc)"
            );

            return inputAlphabet
                        .Cast<object>()
                        .Select(x => CheckType<string>(x, "input_alphabet must be all strings"))
                        .ToList();
        }

        private List<string> CheckStringList(dynamic thing, string varName)
        {
            System.Collections.IEnumerable ie = CheckType<System.Collections.IEnumerable>(
                thing,
                $"{varName} must be enumerable (tuple, list, set etc)"
            );
            return ie.Cast<object>()
                        .Select(x => CheckType<string>(x, $"{varName} must be all strings"))
                        .ToList();
        }

        private static T CheckType<T>(dynamic thing, string msg)
        {
            if(thing is T t)
            {
                return t;
            }
            throw new Exception(msg);
        }
    }
}

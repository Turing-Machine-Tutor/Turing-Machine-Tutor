namespace Frontend
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
    }
}

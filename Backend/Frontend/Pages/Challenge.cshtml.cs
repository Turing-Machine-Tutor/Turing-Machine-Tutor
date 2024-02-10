using Backend.Service_Layer;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using System.Numerics;

namespace Frontend.Pages
{
    public class ChallengeModel : PageModel
    {
        private Guid challengeId;

        public TuringMachine TuringMachineInstance { get; set; }

        [BindProperty]
        public string Description { get; set; }
        [BindProperty]
        public string Code {  get; set; }

        [BindProperty]
        public string TestInput { get; set; }
        [BindProperty]
        public char[] MyArray { get; set; }



        public void OnGet()
        {
            if (MyArray == null)
            {
                MyArray = new char[20];
                for (int i = 0; i < MyArray.Length; i++)
                {
                    MyArray[i] = 'B';
                }
            }
            challengeId = API.selectedChallengeId;
            Description = API.selectedChallengeDesc;
            // challege id that the user has selected

            // initial code
            Code = @"def build():
    # Example Turing Machine parameters
    input_alphabet = ['0', '1']
    tape_alphabet = ['0', '1', 'B']  # B represents blank symbol
    blank = 'B'
    states = ['q0', 'q1', 'acc', 'rej']
    initial_state = 'q0'
    acc = 'acc'
    rej = 'rej'
    delta = {
        ('q0', '0'): ('0', 'q1', 'R'),
        ('q0', '1'): ('1', 'q1', 'R'),
        ('q1', '0'): ('0', 'q0', 'L'),
        ('q1', '1'): ('1', 'q0', 'L'),
        ('q0', 'B'): ('B', 'acc', 'S'),
        ('q1', 'B'): ('B', 'rej', 'S')
    }
";

        }


        public void OnPost()
        {
            string test = Request.Form["test"];
            string validate = Request.Form["validate"];
            string step = Request.Form["step_button"];
            if (test != null)
            {
                Console.WriteLine("Test" + Code);

                TuringMachineInstance = TuringMachineBuilder.Parse(Code);

                bool result = TuringMachineInstance.Run(TestInput);
                if(result)
                {
                    TempData["TestResult"] = "Turing Machine accepts input: " + TestInput;
                }
                else
                {
                    TempData["TestResult"] = "Turing Machine rejects input: " + TestInput;
                }

            }
            else if (validate != null)
            {
                Console.WriteLine("Validate" + Code);
        
                
                Response<string> response= Backend_Connector.get_service_controller().Validate_turing_machine(Code, API.selectedChallengeId.ToString());
                if(response.ErrorOccured)
                {
                    TempData["TestResult"] = response.ErrorMessage;
                }
                else
                {
                    TempData["TestResult"] = response.Value;
                }

                // where we can use tempdata at the very beginning to initialize the service controller?
                // TempData["service_controller"].Validate_turing_machine(code,id)

            }
            else if (step !=null)
            {
                
                Console.WriteLine("first char in array is   " + MyArray[0]);
                Console.WriteLine("TestInput is   " + TestInput);
                

            }

            Description = API.selectedChallengeDesc;
            challengeId = API.selectedChallengeId;

        }

    }
}

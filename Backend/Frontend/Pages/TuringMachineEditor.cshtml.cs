using Backend.Bussiness_Layer.Turing_machine_Builder_Component;
using Backend.Service_Layer;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using System.Collections.Generic;

namespace Frontend.Pages
{
    public class TuringMachineEditorModel : PageModel
    {
        public class TuringMachineChallenge
        {
            public string Id { get; set; }
            public string Name { get; set; }
            public string Description { get; set; }
            public string InitialInput { get; set; }
        }


        [BindProperty]
        public Guid ChallengeId { get; set; }

        //public TuringMachineChallenge SelectedChallenge { get; set; }
        public List<TuringMachineChallenge> Challenges { get; set; }
        public void OnGet()
        {
            // Fetch challenges from your data source (e.g. backend, database)
            // This is a simplified example, replace it with your actual data retrieval logic
            Challenges = new List<TuringMachineChallenge>();
           Response<List<Turing_machine>> Response= Backend_Connector.get_service_controller().extract_all_turing_machines();
            foreach (Turing_machine challenge in Response.Value)
            {
                Challenges.Add(new TuringMachineChallenge { Id = challenge.get_id(), Name = challenge.get_name(), Description = challenge.Description, InitialInput = "0101" });

            }
            /*
            Challenges = new List<TuringMachineChallenge>
            {
            new TuringMachineChallenge { Id = 1, Name = "Challenge 1", Description = "0*", InitialInput = "0101" },
            new TuringMachineChallenge { Id = 2, Name = "Challenge 2", Description = "0*1*", InitialInput = "0011" }
            // Add more challenges as needed
            };
            */
        }

        public RedirectToPageResult OnPost() 
        {
            // Redirect to the SelectChallenge page with the selected challenge ID
            API.selectedChallengeId = ChallengeId;
            TempData["Challenge"] = ChallengeId;
            return RedirectToPage("/Challenge");
        }
    }
}

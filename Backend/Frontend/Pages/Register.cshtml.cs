using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using System.ComponentModel.DataAnnotations;

namespace Frontend.Pages
{
    public class RegisterModel : PageModel
    {
        [BindProperty]
        public string FirstName { get; set; }
        [BindProperty]
        public string LastName { get; set; }
        [BindProperty]
        public string Email { get; set; }
        [BindProperty]
        public string Password { get; set; }
        [BindProperty]
        public string ConfirmPassword { get; set; }

        public void OnGet()
        {
            FirstName = "";

        }
        public void OnPost()
        {

            // TODO

            // user succesfuly registers to system show relevant message
            TempData["RegistrationMessage"] = "User Successfully Registered";


            FirstName = "";
            LastName = "";
            Email = "";
        }
    }
}

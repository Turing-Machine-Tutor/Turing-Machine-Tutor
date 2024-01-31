using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace Frontend.Pages
{
    public class LoginModel : PageModel
    {
        
        public string Email { get; set; }
        public string EmailError { get; set; }
        public string Password { get; set; }
        
        public void OnGet()
        {

        }

        public void OnPost()
        {

            // TODO

            // user successfully logged in
            API.userLoggedin = true;
            TempData["LoginMessage"] = "User Successfully Logged in";

        }
    }
}

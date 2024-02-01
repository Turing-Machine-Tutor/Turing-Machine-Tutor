using Backend.Service_Layer;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace Frontend.Pages
{
    public class LoginModel : PageModel
    {


        [BindProperty]
        public string Email { get; set; }
        [BindProperty]
        public string EmailError { get; set; }
        [BindProperty]
        public string Password { get; set; }
        
        public void OnGet()
        {

        }

        public void OnPost()
        {

            // TODO

            // user successfully logged in
            Response<string> response = Backend_Connector.get_service_controller().Login(Password, Email);
            if (response.ErrorOccured)
            {
                TempData["LoginMessage"] = response.ErrorMessage;
            }
            else
            {
                TempData["LoginMessage"] = response.Value;
                TempData["email"] = Email;
                API.userLoggedin = true;
            }


            
            

        }
    }
}

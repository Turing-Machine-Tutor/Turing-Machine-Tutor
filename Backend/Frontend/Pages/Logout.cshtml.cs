using Backend.Service_Layer;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace Frontend.Pages
{
    public class LogoutModel : PageModel
    {
        public RedirectToPageResult OnGet()
        {
            // TODO
            string email = (string)TempData["email"];
 
                Backend_Connector.get_service_controller().Logout(email);
                

                API.userLoggedin = false;
                TempData["LogoutMessage"] = "You have been successfully logged out.";
                return RedirectToPage("Index");
            
        }
    }
}

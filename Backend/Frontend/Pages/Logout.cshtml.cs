using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace Frontend.Pages
{
    public class LogoutModel : PageModel
    {
        public RedirectToPageResult OnGet()
        {
            API.userLoggedin = false;
            TempData["LogoutMessage"] = "You have been successfully logged out.";
            return RedirectToPage("Index");
        }
    }
}

using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;
using Backend.Bussiness_Layer.Turing_machine_Builder_Component;
using Backend.Bussiness_Layer.User_Component;

namespace Backend.Service_Layer
{
    internal class Service_Controller
    {
        private User_Controller user_Controller;
        private Turing_machine_controller turing_Machine_Controller;


        public Service_Controller()
        {
            user_Controller= User_Controller.GetInstance();
            turing_Machine_Controller  = Turing_machine_controller.GetInstance();
        }

        public Response<String> Register(string first_name,string last_name,string password,string email)
        {
            try
            {
                Response<string> ok = Response<string>.FromValue(this.user_Controller.register(first_name, last_name, password,email));
               

                return ok;

            }
            catch (Exception e)
            {
              
                return Response<String>.FromError(e.Message);
            }
        }

        public Response<String> Login(string password, string email)
        {
            try
            {
                Response<string> ok = Response<string>.FromValue(this.user_Controller.Login(password, email));


                return ok;

            }
            catch (Exception e)
            {

                return Response<String>.FromError(e.Message);
            }
        }

        public void Logout(string email) {
        
         this.user_Controller.Logout(email);
            
        }

        public Response<String> Validate_turing_machine(string code,string selected_turing_machine_id)
        {
            try
            {
                Response<string> ok = Response<string>.FromValue(this.turing_Machine_Controller.Validate_turing_machine(code, selected_turing_machine_id));


                return ok;

            }
            catch (Exception e)
            {

                return Response<String>.FromError(e.Message);
            }
        }






    }
}

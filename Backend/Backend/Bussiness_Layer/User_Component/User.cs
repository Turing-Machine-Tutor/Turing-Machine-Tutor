using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Backend.Bussiness_Layer.User_Component
{
    internal class User
    {
        private string first_name;
        private string last_name;
        private string hashed_password;
        private string email;

        public User(string first_name, string last_name, string password, string email)
        {
            this.first_name = first_name;
            this.last_name = last_name;
            this.hashed_password = password;
            this.email = email;
        }
    }
}

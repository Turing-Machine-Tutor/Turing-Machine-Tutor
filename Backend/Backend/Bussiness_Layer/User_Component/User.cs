using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Backend.Bussiness_Layer.User_Component
{
    internal class User
    {
        public enum Role
        {
            student,
            lecturer,
            admin
        }



        private string first_name;
        private string last_name;
        private string hashed_password;
        private string email;
        private Role role;
        private bool is_logged_in;

        public User(string first_name, string last_name, string password, string email)
        {
            this.first_name = first_name;
            this.last_name = last_name;
            this.hashed_password = password;
            this.email = email;
            this.role = Role.student;
            this.is_logged_in = true;
        }

        public bool IsLoggedIn()
        {
            return is_logged_in;
        }

        public bool Log_in(string password) {
            
            if(Password_Hasher.VerifyPassword(password, hashed_password))
            {
                this.is_logged_in = true;
                return true;
                
            }
            return false;
            

             
        }

        public string get_first_name()
        {
            return this.first_name;
        }

        public string get_last_name()
        {
            return this.last_name;
        }

        public Role Get_role()
        {
            return this.role;
        }

        public string get_email() { 
        return this.email;
        }

        internal void Logout()
        {
            this.is_logged_in = false;
        }
    }
}

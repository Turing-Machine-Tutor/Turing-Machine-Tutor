using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Backend.Bussiness_Layer.User_Component
{
    internal class User_Controller
    {


        private Dictionary<string,User> users; // key is email , value is user
        

        private User_Controller()
        {

            users = new Dictionary<string, User>();
            
        }

        private static User_Controller Instance = null;

        //To use the lock, we need to create one variable
        private static readonly object Instancelock = new object();
        public static User_Controller GetInstance()
        {
            //This is thread-Safe - Performing a double-lock check.    
            //As long as one thread locks the resource, no other thread can access the resource
            //As long as one thread enters into the Critical Section, 
            //no other threads are allowed to enter the critical section
            lock (Instancelock)
            { //Critical Section Start
                if (Instance == null)
                {
                    Instance = new User_Controller();

                }
            } //Critical Section End
              //Once the thread releases the lock, the other thread allows entering into the critical section
              //But only one thread is allowed to enter the critical section
              //Return the Singleton Instance
            return Instance;
        }

        internal string register(string first_name, string last_name, string password, string email)
        {
            if (!users.ContainsKey(email)) {
                string hashed_password= Password_Hasher.HashPassword(password);
                users.Add(email,new User(first_name, last_name, hashed_password, email));
                return "successfully registered!";
            }

            throw new Exception("this email is already registered!");
        }

        internal string Login(string password, string email)
        {
            if (users.ContainsKey(email))
            {
                if (users[email].IsLoggedIn())
                {
                    throw new Exception("user is already logged in!");
                }

                if (users[email].Log_in(password))
                {
                    return "successfully logged in!";
                }
            }

            throw new Exception("email or password is invalid!");

        }

        internal void Logout(string email)
        {

            users[email].Logout();

        }
    }
}

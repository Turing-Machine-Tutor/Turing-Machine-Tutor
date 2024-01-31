using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;

namespace Backend.Bussiness_Layer.Turing_machine_Builder_Component
{
    internal class ID_generator
    {
        private string current_id;

        private ID_generator()
        {
            this.current_id = "1";
            
        }

        private static ID_generator Instance = null;

        //To use the lock, we need to create one variable
        private static readonly object Instancelock = new object();
        public static ID_generator GetInstance()
        {
            //This is thread-Safe - Performing a double-lock check.    
            //As long as one thread locks the resource, no other thread can access the resource
            //As long as one thread enters into the Critical Section, 
            //no other threads are allowed to enter the critical section
            lock (Instancelock)
            { //Critical Section Start
                if (Instance == null)
                {
                    Instance = new ID_generator();


                }
            } //Critical Section End
              //Once the thread releases the lock, the other thread allows entering into the critical section
              //But only one thread is allowed to enter the critical section
              //Return the Singleton Instance
            return Instance;
        }

        
        public  string Get_ID()
        {
            lock (Instancelock)
            {
                string return_me = Instance.current_id;
                Instance.current_id=(Int32.Parse(Instance.current_id)+1).ToString();
                return return_me;
                
            }

        }


    }
}

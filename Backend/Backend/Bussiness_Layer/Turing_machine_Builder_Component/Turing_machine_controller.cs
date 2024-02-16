using Backend.Bussiness_Layer.User_Component;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Backend.Bussiness_Layer.Turing_machine_Builder_Component
{
    internal class Turing_machine_controller
    {
        private Dictionary<string, Turing_machine> turing_machines; //key is ID value is turing machine

        private Turing_machine_controller()
        {
            this.turing_machines = new Dictionary<string, Turing_machine>();
            //build in turing machines 
            Turing_machine tm=new Turing_machine("turing machine that accepts only empty string","empty string language", new List<string> { "" }, new List<string> { "sfs", "0" });
            string id = tm.get_id();
            Turing_machine tm_2 = new Turing_machine("turing machine that accepts only the word 0 and 1", "tutorial_1", new List<string> { "0","1" }, new List<string> { "00", "a" });
            string id_2=tm_2.get_id();
            Turing_machine tm_3 = new Turing_machine("turing machine that accepts 0^n 1^n : s.t n>=1 ", "0^n 1^n", new List<string> { "000111", "00001111" }, new List<string> { "001", "011","0" });
            string id_3=tm_3.get_id();
            turing_machines.Add(id, tm);
            turing_machines.Add(id_2, tm_2);
            turing_machines.Add(id_3, tm_3);   



        }

        private static Turing_machine_controller Instance = null;

        //To use the lock, we need to create one variable
        private static readonly object Instancelock = new object();
        public static Turing_machine_controller GetInstance()
        {
            //This is thread-Safe - Performing a double-lock check.    
            //As long as one thread locks the resource, no other thread can access the resource
            //As long as one thread enters into the Critical Section, 
            //no other threads are allowed to enter the critical section
            lock (Instancelock)
            { //Critical Section Start
                if (Instance == null)
                {
                    Instance = new Turing_machine_controller();


                }
            } //Critical Section End
              //Once the thread releases the lock, the other thread allows entering into the critical section
              //But only one thread is allowed to enter the critical section
              //Return the Singleton Instance
            return Instance;
        }

        internal string Validate_turing_machine(string code,string selected_turing_machine_id)
        {

            TuringMachine tm= TuringMachineParser.Parse(code);
            Turing_machine selected_turing_machine = turing_machines[selected_turing_machine_id];
            string return_me = "running " + selected_turing_machine.get_total_tests_number().ToString() + " tests:  ";
            return_me = return_me + "passed: ";
            int number_of_passed_tests = 0;
            foreach (string illegal_word in selected_turing_machine.WordsNotInLanguage)
            {
                // check words not in lanuage, if turing mahcine accepts then the turing machine is incorrect
                if(tm.Run(illegal_word))
                {
                    return_me = return_me + number_of_passed_tests.ToString() + "/" + selected_turing_machine.get_total_tests_number().ToString()+"   ";
                    throw new Exception(return_me+"accepted a word that is not in language");
                }
                number_of_passed_tests++;
            }

            foreach (string legal_word in selected_turing_machine.WordsInLanguage)
            {
                // check words in lanuage, if turing mahcine does not accepts then the turing machine is incorrect
                if (!tm.Run(legal_word))
                {
                    return_me = return_me + number_of_passed_tests.ToString() + "/" + selected_turing_machine.get_total_tests_number().ToString() + "    ";
                    throw new Exception(return_me+"declined a word that is in language");
                }
                number_of_passed_tests++;
            }

            return return_me+"all tests passed";

        }

        internal List<Turing_machine> extract_all_turing_machines()
        {
            List<Turing_machine> all_machines=new List<Turing_machine>(); 
            foreach(KeyValuePair<string,Turing_machine> pair in this.turing_machines)
            {
                all_machines.Add(pair.Value);
            }
            return all_machines;
        }
    }
}

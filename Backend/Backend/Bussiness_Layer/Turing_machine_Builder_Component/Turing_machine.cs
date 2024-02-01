using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Backend.Bussiness_Layer.Turing_machine_Builder_Component
{
    public class Turing_machine
    {
        private string description;
        private string name;
        private List<string> words_in_language;
        private List<string> words_not_in_language;
        private int total_tests;
        private Guid ID;

        public Turing_machine(string description,string name, List<string> words_in_languages, List<string> words_not_ins_language)
        {
            this.description = description; 
            this.name = name;
            this.words_in_language = words_in_languages;
            this.words_not_in_language=words_not_ins_language;
            total_tests=words_in_language.Count+words_not_ins_language.Count;
            this.ID = Guid.NewGuid();
        }

        public string Description { get { return description; } }
        public List<string> WordsInLanguage { get {  return words_in_language; } }
        public  List<string> WordsNotInLanguage { get { return words_not_in_language; } }

        public string get_id()
        {
            return this.ID.ToString();
        }

        public int get_total_tests_number()
        {
            return total_tests;
        }
        public string get_name()
        {
            return name;
        }


    }
}

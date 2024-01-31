using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Backend.Bussiness_Layer.Turing_machine_Builder_Component
{
    internal class Turing_machine
    {
        private string description;
        private List<string> words_in_language;
        private List<string> words_not_in_language;
        private string ID;

        public Turing_machine(string description, List<string> words_in_languages, List<string> words_not_ins_language,string ID)
        {
            this.description = description; 
            this.words_in_language = words_in_languages;
            this.words_not_in_language=words_not_ins_language;
            this.ID = ID;   
        }

        public string Description { get { return description; } }
        public List<string> WordsInLanguage { get {  return words_in_language; } }
        public  List<string> WordsNotInLanguage { get { return words_not_in_language; } }


    }
}

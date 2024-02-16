// See https://aka.ms/new-console-template for more information
using System.IO;
using System.Reflection.PortableExecutable;
using System.Runtime.CompilerServices;
using Backend.Bussiness_Layer.Turing_machine_Builder_Component;

namespace Backend;
class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("greetings stranger!");
        List<Turing_machine> list_of_tm = Turing_machine_controller.GetInstance().extract_all_turing_machines();
        Console.WriteLine("at any stage press 'q' to quit\n\n");
        display_first_menu(list_of_tm);
        string action_input = Console.ReadLine();
        Console.WriteLine("\n");
        while (action_input != "q")
        {
            
            switch (action_input)
            {
               
                case "0":                  
                    selected_machine_menu_handler(list_of_tm[0].get_id());                
                    break;
                case "1":
                    selected_machine_menu_handler(list_of_tm[0].get_id());
                    break;
                case "2":
                    selected_machine_menu_handler(list_of_tm[0].get_id());
                    break;
                case "q":
                  System.Environment.Exit(0);
                    break;


            }

            display_first_menu(list_of_tm);
            action_input = Console.ReadLine();
            Console.WriteLine("\n");
        }

        
    }

    private static void display_first_menu(List<Turing_machine> list_of_tm)
    {
        Console.WriteLine("please choose desired turing machine to work on: (choose the number) ");
       
        Console.WriteLine("choose your desired action number:");

        for (int i = 0; i < list_of_tm.Count; i++)
        {
            Console.WriteLine("[" + i + "]:  " + list_of_tm[i].Description);
        }
        Console.WriteLine("[q]  Quit");
        Console.WriteLine("\n");
    }

    private static void selected_machine_menu_handler(string tm_ID)
    {
        Console.WriteLine("choose your desired action number:\n");
        Console.WriteLine("[0]  load code for one turing machine from txt file");
        Console.WriteLine("[1]  define more than one turing machines");
        Console.WriteLine("[b]  Back");
        Console.WriteLine("[q]  Quit");
        Console.WriteLine("\n");

        string action_input=Console.ReadLine();
        Console.WriteLine("\n");
        string code;
        switch (action_input)
        {
            case "0":
                code = code_from_path();
                check_user_tm(code, tm_ID);
                break;
            case "1":
                Console.WriteLine("to be continued..");
                break;
            case "q":
                System.Environment.Exit(0);
                break;
            case "b":
                return;
        }
    }

    private static void check_user_tm(string code, string selected_turing_machine_id)
    {
        try
        {
            Console.WriteLine(Turing_machine_controller.GetInstance().Validate_turing_machine(code, selected_turing_machine_id)+"\n");
            
        }
        catch(Exception e) { 
            Console.WriteLine(e.Message+"\n"); 
        }
    }

    public static string code_from_path()
    {
        Console.WriteLine("enter path for text file that includes the turing machine code please:\n");
        Console.WriteLine("the path should be in this format:\n");
        Console.WriteLine("C:\\\\Users\\\\user\\\\Desktop\\\\my_code.txt\n");
        // Console.WriteLine("the file should be in this format:\n");
        // Console.WriteLine("def build():\r\n    # Example Turing Machine parameters\r\n    input_alphabet = ['0', '1']\r\n    tape_alphabet = ['0', '1', 'B']  # B represents blank symbol\r\n    blank = 'B'\r\n    states = ['q0', 'q1', 'acc', 'rej']\r\n    initial_state = 'q0'\r\n    acc = 'acc'\r\n    rej = 'rej'\r\n    delta = {\r\n        ('q0', '0'): ('0', 'q1', 'R'),\r\n        ('q0', '1'): ('1', 'q1', 'R'),\r\n        ('q1', '0'): ('0', 'q0', 'L'),\r\n        ('q1', '1'): ('1', 'q0', 'L'),\r\n        ('q0', 'B'): ('B', 'acc', 'S'),\r\n        ('q1', 'B'): ('B', 'rej', 'S')\r\n    }\n\n\n");
        string path = Console.ReadLine();
        Console.WriteLine();
        //C:\\Users\\bayan\\Desktop\\shit.txt
        StreamReader sr = new StreamReader(path);
        //Read the first line of text
        string code = sr.ReadToEnd();
        sr.Close();
        return code;
        

        
    }
}

    

using System;

namespace AOC2019_5
{

    public class Program
    {
        private static readonly string InputPath = "./InputData.txt";
        private static readonly int InputInstruction = 5;

        private static readonly FileReader fileReader = new FileReader();
        private static readonly InputParser inputParser = new InputParser();
        private static readonly IntCodeComputer intCodeComputer = null;

        static Program()
        {
            var text = fileReader.Get(InputPath);

            var input = inputParser.Parse(text);

            intCodeComputer = new IntCodeComputer(input);
        }

        static void Main(string[] args)
        {
            intCodeComputer.Run(InputInstruction);
        }
    }
}

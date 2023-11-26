using System;
using System.IO;

namespace AOC2019_1
{
    public class FileReader
    {
        public string Get(string path)
        {
            var input = File.ReadAllText(path);

            return input;
        }
    }

    public class InputParser
    {
        private readonly string Splitter = "\r\n";

        public int[] Parse(string input)
        {
            var splitInput = input.Split(this.Splitter);

            var intArray = new int[splitInput.Length];

            for(int i = 0; i < intArray.Length; i++)
            {
                try
                {
                    intArray[i] = int.Parse(splitInput[i]);
                }
                catch(FormatException)
                {
                    Console.WriteLine("Input not of correct format to parse as an integer");
                }
            }

            return intArray;
        }
    }

    public class Calculator
    {
        private readonly int MinInputValue = 9;

        public int Calculate(int input)
        {
            var calculation = input / 3;
            calculation -= 2;

            if (calculation >= this.MinInputValue)
                calculation += this.Calculate(calculation);

            return calculation;
        }
    }

    public class Program
    {
        private static readonly string Input = "./InputData.txt";

        private static readonly FileReader fileReader = new FileReader();
        private static readonly InputParser inputParser = new InputParser();
        private static readonly Calculator calculator = new Calculator();

        static void Main(string[] args)
        {
            var input = fileReader.Get(Input);
            var parsedInput = inputParser.Parse(input);

            int fuelRequirement = 0;

            foreach(var inputElement in parsedInput)
            {
                fuelRequirement += calculator.Calculate(inputElement);
            }

            Console.WriteLine($"Fuel Requirement: {fuelRequirement}");

            Console.ReadLine();
        }
    }
}

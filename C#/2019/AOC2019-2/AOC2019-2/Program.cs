using System;
using System.IO;

namespace AOC2019_2
{
    public class FileReader
    {
        public string Get(string path)
        {
            return File.ReadAllText(path);
        }        
    }

    public class InputParser
    {
        private readonly string Separator = ",";

        public int[] Parse(string input)
        {
            var splitInput = input.Split(this.Separator);

            var intArray = new int[splitInput.Length];

            for(int i = 0; i < splitInput.Length; i++)
            {
                try
                {
                    intArray[i] = int.Parse(splitInput[i]);
                }
                catch(FormatException)
                {
                    Console.WriteLine("The input is of the wrong format to parse as an integer value");
                }
            }

            return intArray;
        }
    }

    public class Manipulator
    {
        public int FindOpCode(int[] input)
        {
            for (int i = 0; i < input.Length - 3; i += 4)
            {
                var opCode = input[i];

                var value1 = input[input[i + 1]];
                var value2 = input[input[i + 2]];

                var outputLocation = input[i + 3];

                if(opCode == 1)
                {
                    input[outputLocation] = value1 + value2;
                }
                else if(opCode == 2)
                {
                    input[outputLocation] = value1 * value2;
                }
                else if(opCode == 99)
                {
                    break;
                }
                else
                {
                    Console.WriteLine("Invalid OpCode");

                    return -1;
                }
            }

            return input[0];
        }
    }

    public class Program
    {
        private static readonly string InputPath = "./InputData.txt";

        private static readonly FileReader fileReader = new FileReader();
        private static readonly InputParser inputParser = new InputParser();
        private static readonly Manipulator manipulator = new Manipulator();

        static void Main(string[] args)
        {
            var text = fileReader.Get(InputPath);

            var input = inputParser.Parse(text);

            var modifiedInput = (int[])input.Clone();

            int output = 0;
            int noun = 0;
            int verb = 0;

            for(int i = 0; i < 100; i++)
            {
                for(int j = 0; j < 100; j++)
                {
                    modifiedInput[1] = i;
                    modifiedInput[2] = j;

                    output = manipulator.FindOpCode(modifiedInput);

                    if (output == 19690720)
                    {
                        verb = j;
                        break;
                    }

                    modifiedInput = (int[])input.Clone();
                }

                if (output == 19690720)
                {
                    noun = i;
                    break;
                }
            }

            Console.WriteLine($"OpCode: {output} with noun: {noun}, and verb: {verb}");
            Console.WriteLine($"Therefore the output is 100 * {noun} + {verb} = {100 * noun + verb}");

            Console.ReadLine();
        }
    }
}

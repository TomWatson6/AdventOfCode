using System;

namespace AOC2019_5
{
    public class InputParser
    {
        private readonly string Separator = ",";

        public int[] Parse(string input)
        {
            var splitInput = input.Split(this.Separator);

            var intArray = new int[splitInput.Length];

            for (int i = 0; i < splitInput.Length; i++)
            {
                try
                {
                    intArray[i] = int.Parse(splitInput[i]);
                }
                catch (FormatException)
                {
                    Console.WriteLine("The input is of the wrong format to parse as an integer value");
                }
            }

            return intArray;
        }
    }
}

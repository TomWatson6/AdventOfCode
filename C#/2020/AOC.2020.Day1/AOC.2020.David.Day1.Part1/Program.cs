using System;
using System.IO;
using System.Linq;

namespace AOC._2020.David.Day1.Part1
{
    class Program
    {
        static void Main(string[] args)
        {
            var input = File.ReadAllText("input.txt");
            var numbers = input.Split("\r\n").Select(x => int.Parse(x)).ToArray();

            for(int i = 0; i < numbers.Length - 1; i++)
            {
                for(int j = i + 1; j < numbers.Length; j++)
                {
                    if(numbers[i] + numbers[j] == 2020)
                    {
                        Console.WriteLine("Answer: " + (numbers[i] * numbers[j]));
                    }
                }
            }
        }
    }
}

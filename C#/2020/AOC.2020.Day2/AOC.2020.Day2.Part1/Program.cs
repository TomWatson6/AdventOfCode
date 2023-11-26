using System;
using System.IO;
using System.Linq;

namespace AOC._2020.Day2.Part1
{
    class Program
    {
        static void Main(string[] args)
        {
            var input = File.ReadAllText("input.txt");
            var lines = input.Split("\r\n");

            var count = 0;

            //14-15 v: vdvvvvvsvvvvvfpv

            foreach (var line in lines)
            {
                var components = line.Split(": ");
                var specs = components[0].Split(" ");
                var bounds = specs[0].Split("-");

                var lowerBound = int.Parse(bounds[0]);
                var upperBound = int.Parse(bounds[1]);

                var constraintLetter = specs[1];

                var password = components[1];

                var letters = password.Where(x => x.ToString() == constraintLetter);
                var letterCount = letters.Count();

                if (letterCount >= lowerBound && letterCount <= upperBound)
                    count++;
            }

            Console.WriteLine("Number of correct passwords: " + count);
        }
    }
}

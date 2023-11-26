using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Security.Cryptography.X509Certificates;

namespace AOC._2020.Day2.Part2
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
                var positions = specs[0].Split("-");

                var pos1 = int.Parse(positions[0]) - 1;
                var pos2 = int.Parse(positions[1]) - 1;

                var constraintLetter = specs[1];

                var password = components[1];
                var charPositions = new List<int>();

                for(int i = 0; i < password.Length; i++)
                {
                    if (password[i].ToString() == constraintLetter)
                        charPositions.Add(i);
                }

                if (charPositions.Where(x => x == pos1 || x == pos2).Count() == 1)
                    count++;
            }

            Console.WriteLine("Number of correct passwords: " + count);
        }
    }
}

using System;
using System.IO;
using System.Linq;

namespace AOC._2020.Day6
{
    class Program
    {
        static void Main(string[] args)
        {
            var reader = new FileReader();

            var input = reader.Read("input.txt");

            var part1 = new Part1();
            var part2 = new Part2();

            Console.WriteLine(part1.Solve(input));
            Console.WriteLine();
            Console.WriteLine(part2.Solve(input));

        }
    }
}

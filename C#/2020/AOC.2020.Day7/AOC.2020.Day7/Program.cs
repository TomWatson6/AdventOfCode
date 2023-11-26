using System;
using System.Diagnostics;

namespace AOC._2020.Day7
{
    class Program
    {
        static void Main(string[] args)
        {
            var reader = new FileReader();
            var part1 = new Part1();
            var part2 = new Part2();

            var input = reader.Read("input.txt");

            var stopwatch = new Stopwatch();
            stopwatch.Start();

            Console.WriteLine("Part 1: " + part1.Solve(input));

            stopwatch.Stop();

            Console.WriteLine("Time Taken (ms): " + stopwatch.ElapsedMilliseconds);
            Console.WriteLine();

            stopwatch.Reset();
            stopwatch.Start();

            Console.WriteLine("Part 2: " + part2.Solve(input));

            stopwatch.Stop();

            Console.WriteLine("Time Taken (ms): " + stopwatch.ElapsedMilliseconds);
        }
    }
}

using System;
using System.Diagnostics;

namespace AOC._2020.Day15
{
    class Program
    {
        static void Main(string[] args)
        {
            var part1 = new Part1();
            var part2 = new Part1();

            var stopwatch = new Stopwatch();
            stopwatch.Start();

            Console.WriteLine("Part 1: " + part1.Solve(2020));

            stopwatch.Stop();

            Console.WriteLine("Time Taken (ms): " + stopwatch.ElapsedMilliseconds);
            Console.WriteLine();

            stopwatch.Reset();
            stopwatch.Start();

            Console.WriteLine("Part 2: " + part2.Solve(30000000));

            stopwatch.Stop();

            Console.WriteLine("Time Taken (ms): " + stopwatch.ElapsedMilliseconds);
        }
    }
}

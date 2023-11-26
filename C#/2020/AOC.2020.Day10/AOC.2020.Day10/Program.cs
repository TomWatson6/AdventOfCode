using System;
using System.Diagnostics;
using System.IO;
using System.Linq;

namespace AOC._2020.Day10
{
    class Program
    {
        static void Main(string[] args)
        {
            var input = File.ReadAllText("input.txt");
            var joltages = input.Split(Environment.NewLine).Select(x => int.Parse(x)).ToHashSet();

            var part1 = new Part1();

            var stopwatch = new Stopwatch();
            stopwatch.Start();

            Console.WriteLine("Part 1: " + part1.Solve(joltages));

            stopwatch.Stop();

            Console.WriteLine("Time Taken (ms): " + stopwatch.ElapsedMilliseconds);

            Console.WriteLine();

            var part2 = new Part2();

            stopwatch.Reset();
            stopwatch.Start();

            Console.WriteLine("Part 2: " + part2.Solve(joltages));

            stopwatch.Stop();

            Console.WriteLine("Time Taken (ms): " + stopwatch.ElapsedMilliseconds);
        }
    }
}

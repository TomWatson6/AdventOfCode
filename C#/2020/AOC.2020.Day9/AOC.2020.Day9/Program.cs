using System;
using System.Diagnostics;
using System.IO;
using System.Linq;

namespace AOC._2020.Day9
{
    class Program
    {
        static void Main(string[] args)
        {
            var input = File.ReadAllText("input.txt").Split(Environment.NewLine).Select(x => long.Parse(x)).ToArray();

            var part1 = new Part1();

            var stopwatch = new Stopwatch();
            stopwatch.Start();

            var part1Answer = part1.Solve(input);

            Console.WriteLine("Part 1: " + part1Answer);

            stopwatch.Stop();

            Console.WriteLine("Time Taken (ms): " + stopwatch.ElapsedMilliseconds);

            var part2 = new Part2();

            stopwatch.Reset();
            stopwatch.Start();

            Console.WriteLine();
            Console.WriteLine("Part 2: " + part2.Solve(input, long.Parse(part1Answer)));

            stopwatch.Stop();

            Console.WriteLine("Time Taken (ms): " + stopwatch.ElapsedMilliseconds);
        }
    }
}

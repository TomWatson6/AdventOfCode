using System;
using System.Diagnostics;

namespace AOC._2020.Day17
{
    class Program
    {
        static void Main(string[] args)
        {
            var reader = new FileReader();

            var input = reader.Read("input.txt");

            var stopwatch = new Stopwatch();
            stopwatch.Start();

            var part1 = new Part1(input);

            Console.WriteLine("Part 1: " + part1.Solve(6));

            stopwatch.Stop();

            Console.WriteLine("Time Taken (ms): " + stopwatch.ElapsedMilliseconds);
            Console.WriteLine();

            var input2 = reader.Read2("input.txt");

            stopwatch.Reset();
            stopwatch.Start();

            var part2 = new Part2(input2);

            Console.WriteLine("Part 2: " + part2.Solve(6));

            stopwatch.Stop();

            Console.WriteLine("Time Taken (ms): " + stopwatch.ElapsedMilliseconds);
        }
    }
}

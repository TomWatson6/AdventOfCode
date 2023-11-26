using System;
using System.Diagnostics;
using System.Runtime.InteropServices;

namespace AOC._2020.Day11
{
    class Program
    {
        static void Main(string[] args)
        {
            var reader = new FileReader();
            var grid = reader.Read("input.txt");

            var stopwatch = new Stopwatch();
            stopwatch.Start();

            var part1 = new Part1(grid);

            Console.WriteLine("Part 1: " + part1.Solve());

            stopwatch.Stop();

            Console.WriteLine("Time Taken (ms): " + stopwatch.ElapsedMilliseconds);
            Console.WriteLine();

            stopwatch.Reset();
            stopwatch.Start();

            var part2 = new Part2(grid);

            Console.WriteLine("Part 2: " + part2.Solve());

            stopwatch.Stop();

            Console.WriteLine("Time Taken (ms): " + stopwatch.ElapsedMilliseconds);
        }
    }
}

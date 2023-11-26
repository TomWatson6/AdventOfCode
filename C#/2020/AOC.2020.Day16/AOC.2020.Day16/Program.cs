using System;
using System.Diagnostics;

namespace AOC._2020.Day16
{
    class Program
    {
        static void Main(string[] args)
        {
            var reader = new FileReader();

            var ticketInfo = reader.Read("input.txt");

            var part1 = new Part1();

            var stopwatch = new Stopwatch();
            stopwatch.Start();

            Console.WriteLine("Part 1: " + part1.Solve(ticketInfo));

            stopwatch.Stop();

            Console.WriteLine("Time Taken (ms): " + stopwatch.ElapsedMilliseconds);

            Console.WriteLine();

            var part2 = new Part2();

            stopwatch.Reset();
            stopwatch.Start();

            Console.WriteLine("Part 2: " + part2.Solve(ticketInfo));

            stopwatch.Stop();

            Console.WriteLine("Time Taken (ms): " + stopwatch.ElapsedMilliseconds);
        }
    }
}

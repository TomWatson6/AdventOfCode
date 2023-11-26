using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Security.Cryptography.X509Certificates;

namespace AOC._2020.Day12
{
    class Program
    {
        static void Main(string[] args)
        {
            var input = File.ReadAllText("input.txt");
            var splitInput = input.Split(Environment.NewLine);

            var instructions = splitInput.Select(x => (x.Substring(0, 1), int.Parse(x.Substring(1, x.Length - 1)))).ToArray();

            var stopwatch = new Stopwatch();
            stopwatch.Start();

            var part1 = new Part1();

            Console.WriteLine("Part 1: " + part1.Solve(instructions));

            stopwatch.Stop();

            Console.WriteLine("Time Taken (ms): " + stopwatch.ElapsedMilliseconds);
            Console.WriteLine();

            stopwatch.Reset();
            stopwatch.Start();

            var part2 = new Part2();

            Console.WriteLine("Part 2: " + part2.Solve(instructions));

            stopwatch.Stop();

            Console.WriteLine("Time Taken (ms): " + stopwatch.ElapsedMilliseconds);
        }
    }
}

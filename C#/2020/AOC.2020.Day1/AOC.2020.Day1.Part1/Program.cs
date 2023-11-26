using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Text;

namespace AOC._2020.Day1.Part1
{
    class Program
    {
        static readonly int Total = 2020;

        static void Main(string[] args)
        {
            var input = File.ReadAllText("input2.txt");
            var lines = input.Split("\r\n");

            var stopwatch = new Stopwatch();

            stopwatch.Start();

            var found = false;
            Console.WriteLine("METHOD 1:");

            for(int i = 0; i < lines.Length - 1; i++)
            {
                for(int j = i + 1; j < lines.Length; j++)
                {
                    if (int.Parse(lines[i]) + int.Parse(lines[j]) == Total)
                    {
                        found = true;
                        Console.WriteLine($"{lines[i]} * {lines[j]} = {int.Parse(lines[i]) * int.Parse(lines[j])}");
                        break;
                    }
                }

                if (found)
                    break;
            }

            stopwatch.Stop();
            Console.WriteLine($"Time Taken (ms): {stopwatch.ElapsedMilliseconds}");
            Console.WriteLine();
            Console.WriteLine();

            stopwatch.Reset();
            stopwatch.Start();

            Console.WriteLine("METHOD 2:");

            var lookup = new HashSet<int>();

            foreach(var line in lines)
            {
                var value = int.Parse(line);

                if (lookup.Contains(Total - value)) {
                    Console.WriteLine($"{value} * {Total - value} = {value * (Total - value)}");
                    break;
                }
                else
                {
                    lookup.Add(value);
                }
            }

            stopwatch.Stop();
            Console.WriteLine($"Time Taken (ms): {stopwatch.ElapsedMilliseconds}");
        }
    }
}

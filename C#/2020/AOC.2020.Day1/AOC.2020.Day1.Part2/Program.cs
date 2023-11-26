using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;

namespace AOC._2020.Day1.Part2
{
    class Program
    {
        static readonly int Total = 2020;

        static void Main(string[] args)
        {
            var input = File.ReadAllText("input.txt");
            var lines = input.Split("\r\n").Select(x => int.Parse(x)).ToArray();

            var stopwatch = new Stopwatch();

            stopwatch.Start();
            //var output = new Dictionary<int, string>();

            for(int i = 0; i < lines.Length - 2; i++)
            {
                for(int j = i + 1; j < lines.Length - 1; j++)
                {
                    for(int k = j + 1; k < lines.Length; k++)
                    {
                        //output.TryAdd(lines[i] + lines[j] + lines[k], $"{lines[i]} + {lines[j]} + {lines[k]} = {lines[i] + lines[j] + lines[k]}");

                        if (lines[i] + lines[j] + lines[k] == Total)
                        {
                            Console.WriteLine($"{lines[i]} * {lines[j]} * {lines[k]} = {lines[i] * lines[j] * lines[k]}");
                        }
                    }
                }
            }

            //foreach(var @out in output.OrderBy(x => x.Key).Select(x => x.Value))
            //{
            //    Console.WriteLine(@out);
            //}

            stopwatch.Stop();
            Console.WriteLine("Time Taken: " + stopwatch.ElapsedMilliseconds);
        }
    }
}

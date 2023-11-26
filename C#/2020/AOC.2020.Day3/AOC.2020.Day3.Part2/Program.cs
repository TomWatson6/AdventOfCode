using System;
using System.Collections.Generic;
using System.IO;

namespace AOC._2020.Day3.Part2
{
    class Program
    {
        static readonly char Tree = '#';
        static readonly double[] horizIncs = { 0.5, 1, 3, 5, 7 };

        static void Main(string[] args)
        {
            var input = File.ReadAllText("input.txt");
            var rows = input.Split("\r\n");

            var treeCounts = new List<int>();


            foreach (var inc in horizIncs)
            {
                var horizCounter = 0.0;
                var treeCount = 0;

                foreach (var row in rows)
                {
                    if (horizCounter % 1 == 0)
                    {
                        if (row[(int)(horizCounter % row.Length)] == Tree)
                            treeCount++;
                    }

                    horizCounter += inc;
                }

                treeCounts.Add(treeCount);
            }

            BigInteger answer = -1;

            treeCounts.ForEach(x =>
            {
                if (answer == -1)
                    answer = x;
                else
                    answer *= x;
            });

            Console.WriteLine("Answer: " + answer);
        }
    }
}

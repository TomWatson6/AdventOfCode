using System;
using System.IO;

namespace AOC._2020.David.Day3.Part2
{
    class Program
    {
        static readonly char Tree = '#';
        static readonly double[] horizIncs = { 0.5, 1, 3, 5, 7 };

        static void Main(string[] args)
        {
            var input = File.ReadAllText("input.txt");
            var rows = input.Split(Environment.NewLine);

            var treeCount = 0;
            var horizCounter = 0.0;

            long product = 1;

            foreach (var inc in horizIncs)
            {
                foreach (var row in rows)
                {
                    if (horizCounter % 1 == 0)
                    {
                        var index = Convert.ToInt32(horizCounter % row.Length);

                        if (row[index] == Tree)
                            treeCount++;
                    }

                    horizCounter += inc;
                }

                product *= treeCount;

                treeCount = 0;
                horizCounter = 0;
            }

            Console.WriteLine("Product: " + product);
        }
    }
}

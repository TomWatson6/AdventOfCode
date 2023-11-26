using System;
using System.IO;
using System.Linq;

namespace AOC._2020.Day18
{
    class Program
    {
        static void Main(string[] args)
        {
            var input = File.ReadAllText("input.txt").Split(Environment.NewLine);

            var part1 = input.Select(x => Expression.Resolve(x, out var p)).Sum();

            Console.WriteLine("Part 1: " + part1);
            Console.WriteLine();

            var alteredExpressions = input.Select(x => Expression.Alter(x)).ToArray();

            var part2 = alteredExpressions.Select(x => Expression.Resolve(x, out var p)).Sum();

            Console.WriteLine("Part 2: " + part2);

            /* 
             * IDEAS:
             * 
             * Do the best possible alteration, but take out the "cleaned expression" step
             * Once crunched down with Alter function, pass to a ResolveBrackets method, which uses Resolve with substrings (inner most bracket(s)) of the expression
             * Then run through alter once more to auto put the brackets around the additions
             * Then run whole thing through Resolve function and should work
             *
             */
        }
    }
}

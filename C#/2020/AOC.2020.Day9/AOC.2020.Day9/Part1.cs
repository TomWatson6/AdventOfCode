using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace AOC._2020.Day9
{
    public class Part1
    {
        private readonly int preambleLength = 25;

        public string Solve(long[] input)
        {
            for(int i = preambleLength; i < input.Length; i++)
            {
                var number = input[i];

                var preamble = input[(i - preambleLength)..i];

                if (preamble.Any(x => preamble.Any(y => y != x && y + x == number)))
                    continue;

                return number.ToString();
            }

            return "NO NUMBER FOUND";
        }
    }
}

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace AOC._2020.Day9
{
    public class Part2
    {
        public string Solve(long[] input, long invalidNumber)
        {
            for(int i = 0; i < input.Length - 1; i++)
            {
                long cumTotal = 0;
                var upper = i + 1;

                while (cumTotal <= invalidNumber)
                {
                    if (upper >= input.Length)
                        return "ERROR";

                    var section = input[i..upper];

                    cumTotal = section.Sum();

                    if (cumTotal == invalidNumber)
                        return $"{section.Min() + section.Max()}";

                    upper++;
                }
            }

            return "Sum not found";
        }
    }
}

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace AOC._2020.Day10
{
    public class Part1
    {
        public string Solve(HashSet<int> joltages)
        {
            var max = joltages.Max();

            var diff1 = 0;
            var diff3 = 1;
            var count = 0;

            for(int i = 0; i <= max; i++)
            {
                if(joltages.Contains(i))
                {
                    if (count == 1)
                    {
                        diff1++;
                        count = 0;
                    }
                    else if (count == 3)
                    {
                        diff3++;
                        count = 0;
                    }
                    else if (count > 3)
                        return "ERROR";
                }

                count++;
            }

            return (diff1 * diff3).ToString();
        }
    }
}

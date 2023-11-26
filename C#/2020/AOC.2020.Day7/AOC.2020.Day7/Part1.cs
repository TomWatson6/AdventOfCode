using System;
using System.Collections.Generic;
using System.Text;

namespace AOC._2020.Day7
{
    public class Part1
    {
        public string Solve(HashSet<Bag> input)
        {
            var count = 0;
            var record = new HashSet<string>();

            foreach(var bag in input)
            {
                if (bag.ContainsBag("shiny gold", input, record))
                    count++;
            }

            return count.ToString();
        }
    }
}

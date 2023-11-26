using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace AOC._2020.Day7
{
    public class Part2
    {
        public string Solve(HashSet<Bag> input)
        {
            return input.First(x => x.Name == "shiny gold").NumberOfBagsContained(input).ToString();
        }
    }
}

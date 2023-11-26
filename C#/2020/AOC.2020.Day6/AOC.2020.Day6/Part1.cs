using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace AOC._2020.Day6
{
    public class Part1
    {
        public string Solve(string[] input)
        {
            var answerLists = input.Select(x => x.Split("\r\n"));

            var output = answerLists.Select(x => x.SelectMany(y => y).ToHashSet()).Select(x => x.Count()).Sum();

            return "Sum of answers: " + output;
        }
    }
}

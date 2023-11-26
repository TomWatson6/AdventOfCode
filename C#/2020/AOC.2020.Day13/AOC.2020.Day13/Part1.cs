using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;

namespace AOC._2020.Day13
{
    public class Part1
    {
        public string Solve((int, int[]) input)
        {
            var busRuns = input.Item2.ToDictionary(x => x, x => input.Item1 / (double)x);

            var runs = busRuns.Select(x => (x.Key, (int)x.Value < x.Value ? ((int)x.Value + 1) * x.Key : (int)x.Value * x.Key));

            var waitTimes = runs.Select(x => (x.Key, x.Item2 - input.Item1));

            var time = waitTimes.OrderBy(x => x.Item2).First();

            return (time.Key * time.Item2).ToString();
        }
    }
}

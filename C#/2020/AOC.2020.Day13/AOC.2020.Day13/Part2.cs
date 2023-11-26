using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Runtime;
using System.Runtime.InteropServices.ComTypes;
using System.Text;

namespace AOC._2020.Day13
{
    public class Part2
    {
        public string Solve(string[] input)
        {
            var rules = new Dictionary<int, int>();

            for(int i = 0; i < input.Length; i++)
            {
                if(input[i] != "x")
                    rules.Add(int.Parse(input[i]), i);
            }

            long inc = rules.First().Key;
            var orderedRules = rules.Where(x => x.Key != rules.First().Key).ToDictionary(x => x.Key, x => x.Value).OrderBy(x => x.Key);

            for (long i = inc; true; i += inc)
            {
                var incChanged = false;

                var rule = orderedRules.First();

                var mult = (i + rule.Value) / (double)rule.Key;

                if (mult > (long)mult)
                    continue;

                var intMult = (long)mult;

                var value = rule.Key * intMult;

                if (value - i == rule.Value)
                {
                    inc = this.LCM(rule.Key, inc);
                    incChanged = true;
                } 

                if (incChanged)
                    orderedRules = orderedRules.Where(x => x.Key != orderedRules.First().Key).ToDictionary(x => x.Key, x => x.Value).OrderBy(x => x.Key);

                if (orderedRules.Count() == 0)
                    return i.ToString();
            }
        }

        private static long GCD(long a, long b)
        {
            if (a % b == 0) return b;
            return GCD(b, a % b);
        }

        private long LCM(long a, long b)
        {
            return a * b / GCD(a, b);
        }
    }
}

using AOC2019_4.Rules;
using System;
using System.Collections.Generic;

namespace AOC2019_4
{
    public class Program
    {
        private static readonly NumberGenerator numberGenerator = null;
        private static readonly List<IRule> rules;

        static Program()
        {
            numberGenerator = new NumberGenerator();
            rules = new List<IRule>()
            {
                new RangeRule(),
                new AscendingRule(),
                new AdjacentEqualityRule()
            };
        }

        static void Main(string[] args)
        {
            var count = numberGenerator.CountCorrectNumbers(rules);

            Console.WriteLine($"Count: {count}");

            Console.ReadLine();
        }
    }
}

using AOC2019_4.Rules;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace AOC2019_4
{
    public class NumberGenerator
    {
        private readonly int Range = 1000000;

        public int CountCorrectNumbers(List<IRule> rules)
        {
            var count = 0;

            for(int i = 0; i < this.Range; i++)
            {
                if (rules.All(x => x.Check(i)))
                    count++;
            }

            return count;
        }
    }
}

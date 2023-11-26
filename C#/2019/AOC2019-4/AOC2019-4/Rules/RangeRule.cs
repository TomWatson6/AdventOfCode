using System;
using System.Collections.Generic;
using System.Text;

namespace AOC2019_4.Rules
{
    public class RangeRule : IRule
    {
        private readonly int LowerBound = 236491;
        private readonly int UpperBound = 713787;

        public bool Check(int number)
        {
            if (number >= this.LowerBound)
                if (number <= this.UpperBound)
                    return true;

            return false;
        }
    }
}

using System;
using System.Collections.Generic;
using System.Text;

namespace AOC2019_4.Rules
{
    public interface IRule
    {
        bool Check(int number);
    }
}

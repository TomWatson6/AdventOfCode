using System;
using System.Collections.Generic;
using System.Text;

namespace AOC2019_7
{
    public enum Mode
    {
        Position = 0,
        Immediate = 1
    }

    public class Parameter
    {
        public Parameter(Mode mode, int value)
        {
            this.Mode = mode;
            this.Value = value;
        }

        public Mode Mode { get; set; }
        public int Value { get; set; }
    }
}

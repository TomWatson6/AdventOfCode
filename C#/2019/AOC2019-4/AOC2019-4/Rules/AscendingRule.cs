using System;
using System.Collections.Generic;
using System.Text;

namespace AOC2019_4.Rules
{
    public class AscendingRule : IRule
    {
        public bool Check(int number)
        {
            bool isAscending = true;

            var numberStr = number.ToString();
            
            for(int i = 0; i < numberStr.Length - 1; i++)
            {
                if (int.Parse(numberStr[i].ToString()) > int.Parse(numberStr[i + 1].ToString()))
                    isAscending = false;
            }

            return isAscending;
        }
    }
}

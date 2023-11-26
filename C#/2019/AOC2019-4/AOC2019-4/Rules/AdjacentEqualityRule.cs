using System;
using System.Collections.Generic;
using System.Text;

namespace AOC2019_4.Rules
{
    public class AdjacentEqualityRule : IRule
    {
        public bool Check(int number)
        {
            bool hasDouble = false;
            bool previousWasDouble = false;

            var numberStr = number.ToString();

            for (int i = 0; i < numberStr.Length - 1; i++)
            {
                if (int.Parse(numberStr[i].ToString()) == int.Parse(numberStr[i + 1].ToString()))
                {
                    hasDouble = true;

                    if (previousWasDouble)
                        hasDouble = false;

                    previousWasDouble = true;
                }
                else
                {
                    previousWasDouble = false;

                    if (hasDouble)
                        return hasDouble;
                }
            }

            return hasDouble;
        }
    }
}

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace AOC._2020.Day14
{
    public class Part1
    {
        public string Solve(Dictionary<string, (long, long)[]> input)
        {
            var memory = new Dictionary<long, long>();

            foreach(var spec in input)
            {
                var mask = spec.Key;

                var memoryNumbers = spec.Value;

                foreach(var number in memoryNumbers)
                {
                    var binary = Convert.ToString(number.Item2, 2);

                    var maskedBinary = new StringBuilder();

                    for(int i = 0; i < mask.Length; i++)
                    {
                        if(binary.Length >= mask.Length - i)
                        {
                            var index = i - mask.Length + binary.Length;

                            if (mask[i] == 'X')
                                maskedBinary.Append(binary[index]);
                            else
                                maskedBinary.Append(mask[i]);
                        }
                        else
                        {
                            if (mask[i] == 'X')
                                maskedBinary.Append("0");
                            else
                                maskedBinary.Append(mask[i]);
                        }
                    }

                    if (memory.TryGetValue(number.Item1, out var output))
                        memory[number.Item1] = Convert.ToInt64(maskedBinary.ToString(), 2);
                    else
                        memory.Add(number.Item1, Convert.ToInt64(maskedBinary.ToString(), 2));
                }
            }

            return memory.Select(x => x.Value).Sum().ToString();
        }
    }
}

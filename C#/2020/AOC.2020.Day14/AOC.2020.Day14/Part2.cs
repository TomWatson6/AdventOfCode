using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace AOC._2020.Day14
{
    public class Part2
    {
        public string Solve(Dictionary<string, (long, long)[]> input)
        {
            var memory = new Dictionary<long, long>();

            foreach (var spec in input)
            {
                var mask = spec.Key;

                var memoryNumbers = spec.Value;

                foreach (var number in memoryNumbers)
                {
                    var binary = Convert.ToString(number.Item1, 2);
                    
                    var maskedBinaries = new List<long>();

                    var maskedBinary = new StringBuilder();
                    var xLocations = new List<int>();

                    for (int i = 0; i < mask.Length; i++)
                    {
                        if (binary.Length >= mask.Length - i)
                        {
                            var index = i - mask.Length + binary.Length;

                            if (mask[i] == '0')
                                maskedBinary.Append(binary[index]);
                            else
                                maskedBinary.Append(mask[i]);
                        }
                        else
                        { 
                            maskedBinary.Append(mask[i]);
                        }

                        if (mask[i] == 'X')
                            xLocations.Add(i);
                    }

                    var combinations = this.GetReplacementCombinations(maskedBinary.ToString());
                    xLocations = xLocations.Where(x => x >= 0).ToList();

                    if (combinations.Count() == 0)
                        maskedBinaries.Add(Convert.ToInt64(maskedBinary.ToString(), 2));

                    foreach(var combination in combinations)
                    {
                        var sb = new StringBuilder();
                        var combIndex = 0;

                        for(int i = 0; i < maskedBinary.Length; i++)
                        {
                            if (xLocations.Contains(i))
                            {
                                sb.Append(combination[combIndex]);
                                combIndex++;
                            }
                            else
                                sb.Append(maskedBinary[i]);
                        }

                        maskedBinaries.Add(Convert.ToInt64(sb.ToString(), 2));
                    }

                    foreach(var bin in maskedBinaries)
                    {
                        if (memory.TryGetValue(bin, out var output))
                            memory[bin] = number.Item2;
                        else
                            memory.Add(bin, number.Item2);
                    }

                    //if (memory.TryGetValue(number.Item1, out var output))
                    //    memory[number.Item1] = Convert.ToInt64(maskedBinary.ToString(), 2);
                    //else
                    //    memory.Add(number.Item1, Convert.ToInt64(maskedBinary.ToString(), 2));
                }
            }

            return memory.Select(x => x.Value).Sum().ToString();
        }

        private string[] GetReplacementCombinations(string maskedBinary)
        {
            var combinations = new List<string>();

            var countX = maskedBinary.Where(x => x == 'X').Count();

            if (countX == 0)
                return combinations.ToArray();

            var sb = new StringBuilder();

            for(int i = 0; i < countX; i++)
            {
                sb.Append('1');
            }

            var maxBinary = sb.ToString();
            var max = Convert.ToInt64(maxBinary, 2);

            for(int i = 0; i <= max; i++)
            {
                combinations.Add(Convert.ToString(i, 2));
            }

            var maxLength = combinations.Max(x => x.Length);
            var paddedCombinations = new List<string>();

            foreach(var combination in combinations)
            {
                paddedCombinations.Add(combination.PadLeft(maxLength, '0'));
            }

            return paddedCombinations.ToArray();
        }
    }
}

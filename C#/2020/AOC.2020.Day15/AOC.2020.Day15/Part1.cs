using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace AOC._2020.Day15
{
    public class Part1
    {
        private readonly long[] startingNumbers = { 6, 4, 12, 1, 20, 0, 16 };
        private Dictionary<long, List<long>> visitedNumbers = new Dictionary<long, List<long>>();

        public string Solve(long iterations)
        {
            var numbers = new List<long>();

            foreach(var number in this.startingNumbers) {
                numbers.Add(number);
                visitedNumbers.Add(number, new List<long>() { numbers.IndexOf(number) });
            }

            for (int i = numbers.Count - 1; i < iterations - 1; i++)
            {
                if (visitedNumbers[numbers[i]].Count == 1)
                {
                    numbers.Add(0);

                    if (visitedNumbers.ContainsKey(0))
                        visitedNumbers[0].Add(i + 1);
                    else
                        visitedNumbers.Add(0, new List<long> { i + 1 });
                }
                else
                {
                    var numberToAdd = i - visitedNumbers[numbers[i]][visitedNumbers[numbers[i]].Count - 2];

                    numbers.Add(numberToAdd);

                    if (visitedNumbers.ContainsKey(numberToAdd))
                        visitedNumbers[numberToAdd].Add(i + 1);
                    else
                        visitedNumbers.Add(numberToAdd, new List<long> { i + 1 });
                }
            }

            return numbers.Last().ToString();
        }
    }
}

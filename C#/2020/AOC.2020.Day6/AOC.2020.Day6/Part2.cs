using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace AOC._2020.Day6
{
    public class Part2
    {
        public string Solve(string[] input)
        {
            var answerLists = input.Select(x => x.Split("\r\n"));

            var answersDist = answerLists.Select(x => x.Select(y => y.Select(z => z)));

            var counts = new List<int>();

            foreach(var answers in answersDist)
            {
                var count = 0;

                for(char i = 'a'; i <= 'z'; i++)
                {
                    if (answers.All(x => x.Contains(i)))
                        count++;
                }

                counts.Add(count);
            }

            return "Sum of questions that have been answered by all people in each group: " + counts.Sum();
        }
    }
}

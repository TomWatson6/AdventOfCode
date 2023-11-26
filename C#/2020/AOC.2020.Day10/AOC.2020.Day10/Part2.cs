using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;

namespace AOC._2020.Day10
{
    public class Part2
    {
        public string Solve(HashSet<int> joltages)
        {
            var max = joltages.Max();

            //var numRoutes = this.FindPath(joltages, max, 71);

            var savedRoutes = new Dictionary<int, BigInteger>();

            BigInteger numRoutes = 0;

            //foreach(var joltage in joltages.OrderByDescending(x => x))
            //{
            //    numRoutes = this.FindPath(joltages, max, joltage, savedRoutes);
            //    savedRoutes.Add(joltage, numRoutes);
            //}

            numRoutes = this.FindPath(joltages, max, 0, savedRoutes);

            return numRoutes.ToString();
        }

        public BigInteger FindPath(HashSet<int> joltages, int max, int start, Dictionary<int, BigInteger> savedRoutes)
        {
            BigInteger count = 0;

            if (start == max)
                return 1;

            if (start > max)
                return 0;

            BigInteger inc = 0;

            if (savedRoutes.ContainsKey(start + 1))
                count += savedRoutes[start + 1];
            else if (joltages.Contains(start + 1))
            {
                inc = this.FindPath(joltages, max, start + 1, savedRoutes);
                count += inc;
                savedRoutes.Add(start + 1, inc);
            }

            if (savedRoutes.ContainsKey(start + 2))
                count += savedRoutes[start + 2];
            else if (joltages.Contains(start + 2))
            {
                inc = this.FindPath(joltages, max, start + 2, savedRoutes);
                count += inc;
                savedRoutes.Add(start + 2, inc);
            }

            if (savedRoutes.ContainsKey(start + 3))
                count += savedRoutes[start + 3];
            else if (joltages.Contains(start + 3))
            {
                inc = this.FindPath(joltages, max, start + 3, savedRoutes);
                count += inc;
                savedRoutes.Add(start + 3, inc);
            }

            //if (joltages.Contains(start + 2))
            //    count += this.FindPath(joltages, max, start + 2, savedRoutes);

            //if (joltages.Contains(start + 3))
            //    count += this.FindPath(joltages, max, start + 3, savedRoutes);

            return count;
        }

        public BigInteger FindPathEff(HashSet<int> joltages, int max)
        {
            BigInteger total = 1;

            var blackList = new List<int>();

            foreach(var joltage in joltages.OrderBy(x => x))
            {
                var count = 0;

                if (blackList.Contains(joltage))
                    continue;

                var hasRoute1 = this.HasRoute(joltages, max, joltage + 1);
                var hasRoute2 = this.HasRoute(joltages, max, joltage + 2);
                var hasRoute3 = this.HasRoute(joltages, max, joltage + 3);

                if (!hasRoute1)
                    blackList.Add(joltage + 1);
                if (!hasRoute2)
                    blackList.Add(joltage + 2);
                if (!hasRoute3)
                    blackList.Add(joltage + 3);

                if (joltages.Contains(joltage + 1) && hasRoute1)
                    count++;

                if (joltages.Contains(joltage + 2) && hasRoute2)
                    count++;

                if (joltages.Contains(joltage + 3) && hasRoute3)
                    count++;

                if(count != 0)
                    total *= count;
            }

            foreach(var item in blackList)
            {
                Console.WriteLine(item);
            }

            return total;
        }

        public bool HasRoute(HashSet<int> joltages, int max, int start)
        {
            var subset = joltages.Where(x => x <= start);

            var count = 0;

            for (int i = subset.Min(); i <= max; i++)
            {
                if (joltages.Contains(i))
                {
                    if (count == 1)
                        count = 0;
                    if (count == 2)
                        count = 0;
                    else if (count == 3)
                        count = 0;
                    else if (count > 3)
                        return false;
                }

                count++;
            }

            return true;
        }

        public BigInteger FindPathEff2(HashSet<int> joltages, int max)
        {
            BigInteger total = 1;
            var count = 0;

            for(int i = max; i > 0; i--)
            {
                if(joltages.Contains(i))
                {
                    if (joltages.Contains(i - 1))
                        count++;
                    if (joltages.Contains(i - 2))
                        count++;
                    if (joltages.Contains(i - 3))
                        count++;

                    if (count == 0)
                        continue;

                    total *= count;
                }

                count = 0;
            }

            return total;
        }
    }
}

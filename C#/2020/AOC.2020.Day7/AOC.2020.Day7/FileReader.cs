using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace AOC._2020.Day7
{
    public class FileReader
    {
        public HashSet<Bag> Read(string path)
        {
            var input = File.ReadAllText("input.txt");

            var lines = input.Split(".\r\n");

            var specifications = lines.Select(x => x.Split(" contain "));

            var bags = new List<Bag>();

            foreach(var specification in specifications)
            {
                var name = specification[0];

                name = name.Replace(" bags", "").Replace(" bag", "");

                if(specification[1] == "no other bags")
                {
                    bags.Add(new Bag(name));
                    continue;
                }

                var containedBags = specification[1].Split(", ").Select(x => x.Replace(" bags", "").Replace(" bag", ""));

                var amountOfBags = containedBags.ToDictionary(x => string.Join(" ", x.Split(" ")[1..x.Split(" ").Length]), x => int.Parse(x.Split(" ")[0]));

                bags.Add(new Bag(name, amountOfBags));
            }

            return bags.ToHashSet();
        }
    }
}

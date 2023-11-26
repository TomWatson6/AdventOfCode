using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;

namespace AOC._2020.Day7
{
    public class Bag
    {
        public Bag(string name, Dictionary<string, int> bagsContained = null)
        {
            this.Name = name;

            if(bagsContained != null)
                this.BagsContained = bagsContained;
        }

        public string Name { get; set; }
        public Dictionary<string, int> BagsContained { get; set; } = new Dictionary<string, int>();

        public bool ContainsBag(string name, HashSet<Bag> bagRules, HashSet<string> record)
        {
            var contained = false;

            foreach (var bagContained in this.BagsContained)
            {
                if (record.Contains(bagContained.Key) || bagContained.Key == name)
                {
                    record.Add(this.Name);
                    return true;
                }
                else
                    contained = bagRules.First(x => x.Name == bagContained.Key).ContainsBag(name, bagRules, record);

                if (contained)
                    return true;
            }

            return contained;
        }

        public int NumberOfBagsContained(HashSet<Bag> bagRules)
        {
            var value = 0;

            value += this.BagsContained.Select(x => x.Value).Sum();

            foreach(var bag in this.BagsContained)
            {
                value += bagRules.First(x => x.Name == bag.Key).NumberOfBagsContained(bagRules) * bag.Value;
            }

            return value;
        }
    }
}

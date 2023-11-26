using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection.Metadata.Ecma335;

namespace AOC._2015.Day5
{
    class Program
    {
        static void Main(string[] args)
        {
            var input = File.ReadAllText("input.txt");
            var lines = input.Split(Environment.NewLine);

            var rules = new List<Rule> { new VowelRule(), new TwoLetterRule(), new ExclusionRule() };

            var niceOnes = 0;

            foreach(var line in lines)
            {
                if (!rules.Any(x => !x.Validate(line)))
                    niceOnes++;
            }

            Console.WriteLine("Nice Strings: " + niceOnes);
        }
    }

    public interface Rule
    {
        public bool Validate(string text);
    }

    public class VowelRule : Rule
    {
        public char[] Vowels = { 'a', 'e', 'i', 'o', 'u' };

        public bool Validate(string text)
        {
            var vowels = text.Where(x => this.Vowels.Contains(x));

            if (vowels.Count() < 3)
                return false;

            return true;
        }
    }

    public class TwoLetterRule : Rule
    {
        public bool Validate(string text)
        {
            char? lastLetter = null;

            foreach(var letter in text)
            {
                if (lastLetter == letter)
                    return true;
                else
                    lastLetter = letter;
            }

            return false;
        }
    }

    public class ExclusionRule : Rule
    {
        public string[] PatternsToExclude = { "ab", "cd", "pq", "xy" };

        public bool Validate(string text)
        {
            foreach(var pattern in this.PatternsToExclude)
            {
                if (text.Contains(pattern))
                    return false;
            }

            return true;
        }
    }
}

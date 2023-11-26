using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace AOC._2020.Day4.Part1
{
    class Program
    {
        static readonly string[] Requirements = { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" };

        static void Main(string[] args)
        {
            var input = File.ReadAllText("input.txt");

            var splitInput = input.Split("\r\n\r\n");

            var passportCollection = splitInput.Select(x => x.Split("\r\n").SelectMany(y => y.Split(" ")));

            var passports = passportCollection.Select(x => x.ToDictionary(y => y.Split(":")[0], y => y.Split(":")[1])).ToArray();

            var validPassports = passports.Where(x => Requirements.All(y => x.ContainsKey(y)));

            Console.WriteLine("Number of valid passports: " + validPassports.Count());
        }
    }
}

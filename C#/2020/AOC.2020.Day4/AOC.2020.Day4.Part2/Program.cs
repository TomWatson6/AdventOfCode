using System;
using System.Collections.Generic;
using System.Data;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Runtime.CompilerServices;

namespace AOC._2020.Day4.Part2
{
    class Program
    {
        static readonly string[] Requirements = { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" };
        static readonly string[] EyeColours = { "amb", "blu", "brn", "gry", "grn", "hzl", "oth" };

        static void Main(string[] args)
        {
            var stopwatch = new Stopwatch();
            stopwatch.Start();

            var requirements = new Dictionary<string, Func<string, bool>>();

            requirements.Add("byr", x => validateYear(x, 4, 1920, 2002));
            requirements.Add("iyr", x => validateYear(x, 4, 2010, 2020));
            requirements.Add("eyr", x => validateYear(x, 4, 2020, 2030));

            requirements.Add("hgt", x =>
            {
                if (!x.EndsWith("cm") && !x.EndsWith("in"))
                    return false;

                var isNumber = int.TryParse(x.Substring(0, x.Length - 2), out var output);

                if (!isNumber)
                    return false;

                if (x.EndsWith("cm"))
                    if (!validateYear(output.ToString(), 3, 150, 193))
                        return false;
                
                if (x.EndsWith("in"))
                    if (!validateYear(output.ToString(), 2, 59, 76))
                        return false;

                return true;
            });

            requirements.Add("hcl", x =>
            {
                if (!x.StartsWith("#"))
                    return false;

                var code = x.Substring(1, x.Length - 1);

                if (code.Length != 6)
                    return false;

                if (!code.All(x => ((int)x >= 48 && (int)x <= 57) || ((int)x >= 97 && (int)x <= 102)))
                    return false;

                return true;
            });

            requirements.Add("ecl", x => EyeColours.Contains(x));

            requirements.Add("pid", x =>
            {
                if (x.Length != 9)
                    return false;

                if (int.TryParse(x, out var output) == false)
                    return false;

                return true;
            });

            var input = File.ReadAllText("input.txt");

            var splitInput = input.Split("\r\n\r\n");

            var passportCollection = splitInput.Select(x => x.Split("\r\n").SelectMany(y => y.Split(" ")));

            var passports = passportCollection.Select(x => x.ToDictionary(y => y.Split(":")[0], y => y.Split(":")[1])).ToArray();

            var validPassports = passports.Where(x => Requirements.All(y => x.ContainsKey(y)));
            validPassports = validPassports.Where(x => x.All(y => 
            {
                if (y.Key == "cid")
                    return true;
                else
                    return requirements[y.Key].Invoke(y.Value);
            }));

            Console.WriteLine("Number of valid passports: " + validPassports.Count());

            stopwatch.Stop();

            Console.WriteLine("Time Taken (ms): " + stopwatch.ElapsedMilliseconds);
        }

        static bool validateYear(string input, int digits, int lowerBound, int upperBound)
        {
            if (input.Length != digits)
                return false;

            var intInput = int.Parse(input);

            if (intInput < lowerBound || intInput > upperBound)
                return false;

            return true;
        }
    }
}

using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;

namespace AOC._2020.Day13
{
    public class FileReader
    {
        public (int, int[]) Read(string path)
        {
            var input = File.ReadAllText(path);
            var splitInput = input.Split(Environment.NewLine);

            (int, int[]) output;

            output.Item1 = int.Parse(splitInput[0]);

            output.Item2 = splitInput[1].Split(",").Where(x => x != "x").Select(x => int.Parse(x)).ToArray();

            return output;
        }

        public string[] ReadAll(string path)
        {
            var input = File.ReadAllText(path);
            var splitInput = input.Split(Environment.NewLine);

            var output = splitInput[1].Split(",").Select(x => x).ToArray();

            return output;
        }
    }
}

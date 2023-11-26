using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace AOC2019_3
{
    public class FileReader
    {
        public List<string[]> Get(string path)
        {
            var input = File.ReadAllText(path);

            var wires = input.Split("\r\n").ToList();

            var splitWires = wires.Select(x => x.Split(","));

            return splitWires.ToList();
        }
    }
}

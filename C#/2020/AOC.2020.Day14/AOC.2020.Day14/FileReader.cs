using System;
using System.Collections.Generic;
using System.Diagnostics.Tracing;
using System.IO;
using System.Linq;
using System.Text;

namespace AOC._2020.Day14
{
    public class FileReader
    {
        public Dictionary<string, (long, long)[]> Read(string path)
        {
            var input = File.ReadAllText(path);
            var splitInput = input.Split(Environment.NewLine);

            var output = new Dictionary<string, (long, long)[]>();

            var mask = "";
            var mems = new List<(long, long)>();

            foreach (var line in splitInput)
            {
                if (line.StartsWith("mask"))
                {
                    if (!string.IsNullOrEmpty(mask))
                    {
                        output.Add(mask, mems.ToArray());
                        mems = new List<(long, long)>();
                    }

                    mask = line.Split(" = ")[1];
                }

                if(line.StartsWith("mem"))
                {
                    var components = line.Split(" = ");
                    var left = long.Parse(components[0].Split("mem[")[1].Trim(']'));
                    var right = long.Parse(components[1]);

                    mems.Add((left, right));
                }
            }

            output.Add(mask, mems.ToArray());

            return output;
        }
    }
}

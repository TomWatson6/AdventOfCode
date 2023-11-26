using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;

namespace AOC._2020.Day17
{
    public class FileReader
    {
        public Dictionary<(long, long, long), char> Read(string path)
        {
            var input = File.ReadAllLines(path);

            var output = new Dictionary<(long, long, long), char>();

            for(int y = 0; y < input.Length; y++)
            {
                for(int x = 0; x < input[0].Length; x++)
                {
                    output.Add((x, y, 0), input[y][x]);
                }
            }

            return output;
        }

        public Dictionary<(long, long, long, long), char> Read2(string path)
        {
            var input = File.ReadAllLines(path);

            var output = new Dictionary<(long, long, long, long), char>();

            for (int y = 0; y < input.Length; y++)
            {
                for (int x = 0; x < input[0].Length; x++)
                {
                    output.Add((x, y, 0, 0), input[y][x]);
                }
            }

            return output;
        }
    }
}

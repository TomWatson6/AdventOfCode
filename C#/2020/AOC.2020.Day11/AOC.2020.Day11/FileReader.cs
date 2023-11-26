using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace AOC._2020.Day11
{
    public class FileReader
    {
        public char[][] Read(string path)
        {
            var input = File.ReadAllText("input.txt");
            var splitInput = input.Split(Environment.NewLine);

            var grid = splitInput.Select(x => x.ToCharArray()).ToArray();

            return grid;
        }
    }
}

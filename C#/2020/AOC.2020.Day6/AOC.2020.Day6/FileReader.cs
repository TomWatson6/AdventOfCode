using System;
using System.Collections.Generic;
using System.IO;
using System.Text;

namespace AOC._2020.Day6
{
    public class FileReader
    {
        public string[] Read(string path)
        {
            var input = File.ReadAllText(path);

            var splitInput = input.Split("\r\n\r\n");

            return splitInput;
        }
    }
}

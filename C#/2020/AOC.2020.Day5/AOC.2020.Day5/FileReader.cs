using System;
using System.Collections.Generic;
using System.IO;
using System.Text;

namespace AOC._2020.Day5
{
    public class FileReader
    {
        public string[] Read(string path)
        {
            return File.ReadAllText(path).Split(Environment.NewLine);
        }
    }
}

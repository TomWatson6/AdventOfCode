using System;
using System.Collections.Generic;
using System.IO;
using System.Text;

namespace AOC2019_6
{
    public class FileReader
    {
        public string[] Get(string path)
        {
            var fileContents = File.ReadAllText(path);

            var inputData = this.Parse(fileContents);

            return inputData;
        }

        private string[] Parse(string input)
        {
            return input.Split("\r\n");
        }
    }
}

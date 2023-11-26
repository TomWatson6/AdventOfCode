using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection.Metadata.Ecma335;
using System.Text;

namespace AOC._2020.Day8
{
    public class FileReader
    {
        public string[] Read(string path)
        {
            var input = File.ReadAllText(path);

            var splitInput = input.Split("\r\n");

            return splitInput;

            //var output = splitInput.ToDictionary(x => x.Split(" ")[0], x =>
            //{
            //    var number = x.Split(" ")[1];

            //    if (number.StartsWith("+"))
            //        return int.Parse(number.Substring(1, number.Length - 1));
            //    else
            //        return int.Parse(number);
            //});

            //return output;
        }  
    }
}

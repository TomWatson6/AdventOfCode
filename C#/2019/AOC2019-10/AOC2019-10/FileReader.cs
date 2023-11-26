using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace AOC2019_10
{
    public class FileReader
    {
        public char[,] Get(string path, out int xDim, out int yDim)
        {
            var input = File.ReadAllText(path);

            var splitInput = input.Split("\r\n");

            yDim = splitInput.Length;

            xDim = splitInput.Max(x => x.Length);

            char[,] results = new char[xDim, splitInput.Length];

            for(int i = 0; i < splitInput.Length; i++)
            {
                for(int j = 0; j < xDim; j++)
                {
                    results[j, i] = splitInput[i][j];
                }
            }

            return results;
        }
    }
}

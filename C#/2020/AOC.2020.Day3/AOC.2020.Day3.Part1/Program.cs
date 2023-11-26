using System;
using System.Collections.Generic;
using System.IO;
using System.Numerics;

namespace AOC._2020.Day3.Part1
{
    class Program
    {
        static readonly char Tree = '#';
        static readonly int horizInc = 3;

        static void Main(string[] args)
        {
            var input = File.ReadAllText("input.txt");
            var rows = input.Split("\r\n");

            var treeCount = 0;
            var horizCounter = 0;        

            foreach (var row in rows)
            {
                if (row[horizCounter % row.Length] == Tree)
                    treeCount++;

                horizCounter += horizInc;
            }

            Console.WriteLine("Number of Trees: " + treeCount);
        }
    }
}

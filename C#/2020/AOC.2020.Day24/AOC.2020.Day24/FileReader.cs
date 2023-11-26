using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Text;

namespace AOC._2020.Day24
{

    public class FileReader
    {
        private readonly (string name, (double x, double y) direction)[] Instructions = 
        {
            ("ne", (0.5, 1)),
            ("nw", (-0.5, 1)),
            ("se", (0.5, -1)),
            ("sw", (-0.5, -1)),
            ("e", (1, 0)),
            ("w", (-1, 0))
        };

        public Dictionary<(double, double), long> Read(string path)
        {
            var lines = File.ReadAllLines(path);

            var tileDirections = new Dictionary<(double x, double y), long>();

            foreach (var line in lines)
            {
                (double x, double y) tile = (0, 0);

                var instructionString = line;

                //Console.WriteLine("Instructions: " + instructionString);

                while (instructionString.Length > 0)
                {
                    foreach (var instruction in this.Instructions)
                    {
                        if (instructionString.StartsWith(instruction.name))
                        {
                            if (instructionString.Length > instruction.name.Length)
                                instructionString = instructionString.Substring(instruction.name.Length);
                            else
                                instructionString = "";

                            tile = (tile.x + instruction.direction.x, tile.y + instruction.direction.y);
                            //Console.WriteLine($"Instruction: {instruction} -> [{tile.ne}, {tile.e}, {tile.se}]");

                            break;
                        }
                    }
                }

                if (tileDirections.TryGetValue(tile, out var value))
                    tileDirections[tile] += 1;
                else
                    tileDirections.Add(tile, 1);
            }

            return tileDirections;
        }
    }
}

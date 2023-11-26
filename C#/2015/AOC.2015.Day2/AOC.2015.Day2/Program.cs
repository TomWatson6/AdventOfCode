using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Security.Cryptography.X509Certificates;

namespace AOC._2015.Day2
{
    class Program
    {
        static void Main(string[] args)
        {
            var input = File.ReadAllText("input.txt");

            var lines = input.Split(Environment.NewLine);

            var dimensionsList = lines.Select(x => x.Split("x").Select(y => int.Parse(y)).ToArray());

            var totalSquareFeet = 0;
            var totalRibbonLength = 0;

            foreach(var dimensions in dimensionsList)
            {
                var squareFeet = 0;
                var ribbonLength = 0;

                var width = dimensions[0];
                var height = dimensions[1];
                var depth = dimensions[2];

                var smallestSide = 0;

                var side1 = width * height;
                var side2 = height * depth;
                var side3 = depth * width;

                if(side1 > side2)
                {
                    if (side2 > side3)
                        smallestSide = side3;
                    else
                        smallestSide = side2;
                }
                else
                {
                    if (side1 > side3)
                        smallestSide = side3;
                    else
                        smallestSide = side1;
                }

                squareFeet = (side1 + side2 + side3) * 2 + smallestSide;

                totalSquareFeet += squareFeet;

                var smallestDims = dimensions.OrderBy(x => x).ToArray()[0..(dimensions.Length - 1)];
                ribbonLength += (smallestDims[0] + smallestDims[1]) * 2;

                ribbonLength += dimensions[0] * dimensions[1] * dimensions[2];

                totalRibbonLength += ribbonLength;
            }

            Console.WriteLine("Total Square Feet: " + totalSquareFeet);
            Console.WriteLine("Total Ribbon Length: " + totalRibbonLength);
        }
    }
}

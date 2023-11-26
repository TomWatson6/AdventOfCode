using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;

namespace AOC._2015.Day3
{
    class Program
    {
        static void Main(string[] args)
        {
            var input = File.ReadAllText("input.txt");

            var housesDeliveredTo = new HashSet<Point>();

            Point[] currentLocation = { new Point(0, 0), new Point(0, 0) };

            housesDeliveredTo.Add(new Point(currentLocation[0].X, currentLocation[0].Y));

            var currentSanta = 0;

            foreach(var direction in input)
            {
                switch(direction)
                {
                    case '<':
                        currentLocation[currentSanta].X -= 1;
                        break;
                    case '>':
                        currentLocation[currentSanta].X += 1;
                        break;
                    case '^':
                        currentLocation[currentSanta].Y += 1;
                        break;
                    case 'v':
                        currentLocation[currentSanta].Y -= 1;
                        break;
                }

                housesDeliveredTo.Add(new Point(currentLocation[currentSanta].X, currentLocation[currentSanta].Y));

                currentSanta = currentSanta == 0 ? 1 : 0;
            }

            Console.WriteLine("Houses that got at least 1 present: " + housesDeliveredTo.Count);
        }
    }
}

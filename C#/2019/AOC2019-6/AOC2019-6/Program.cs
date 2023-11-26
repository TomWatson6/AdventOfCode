using System;
using System.Collections.Generic;
using System.Linq;

namespace AOC2019_6
{
    public class Program
    {
        private readonly static string InputData = "./InputData.txt";

        private readonly static FileReader fileReader;

        static Program()
        {
            fileReader = new FileReader();
        }

        static void Main(string[] args)
        {
            var input = fileReader.Get(InputData);

            var spaceObjectLibrary = new Dictionary<string, SpaceObject>();

            foreach(var element in input)
            {
                var splitElement = element.Split(")");

                foreach(var part in splitElement)
                {
                    if (!spaceObjectLibrary.TryGetValue(part, out var spaceObject))
                        spaceObjectLibrary.Add(part, new SpaceObject(part));
                }
            }

            foreach(var element in input)
            {
                var splitElement = element.Split(")");

                if(spaceObjectLibrary.TryGetValue(splitElement[1], out var spaceObject))
                {
                    spaceObject.ObjectOrbitted = spaceObjectLibrary[splitElement[0]];
                }
            }

            int checkNum = 0;

            foreach(var kv in spaceObjectLibrary)
            {
                checkNum += kv.Value.GetOrbits();
            }

            Console.WriteLine("Total Orbits: " + checkNum);

            var you = spaceObjectLibrary["YOU"];

            var distance = you.GetDistance(spaceObjectLibrary, "SAN");

            Console.WriteLine("Total Distance: " + distance);
            Console.ReadLine();
        }
    }
}

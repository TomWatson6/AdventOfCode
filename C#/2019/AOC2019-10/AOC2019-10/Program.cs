using System;
using System.Drawing;

namespace AOC2019_10
{
    public class Program
    {
        private static readonly string InputPath = "./InputData.txt";

        private static readonly FileReader fileReader = new FileReader();

        static void Main(string[] args)
        {
            var input = fileReader.Get(InputPath, out var xDim, out var yDim);

            var asteroidField = new AsteroidField(input, xDim, yDim);

            int mostAsteroids = 0;

            for(int i = 0; i < xDim; i++)
            {
                for(int j = 0; j < yDim; j++)
                {
                    if (asteroidField.SpaceObjects[i, j].SpaceObjectType == SpaceObjectType.Nothing) {
                        var num = asteroidField.GetVisibleAsteroids(new Point(i, j));

                        if (num > mostAsteroids)
                            mostAsteroids = num;
                    }
                }
            }

            Console.WriteLine($"Most Asteroids: {mostAsteroids}");
            Console.ReadLine();
        }
    }
}

using System;

namespace AOC2019_3
{
    public class Program
    {
        private readonly static string InputData = "./InputData.txt";

        private readonly static FileReader fileReader = new FileReader();
        private readonly static WireCalculator calculator = new WireCalculator();

        static void Main(string[] args)
        {
            var input = fileReader.Get(InputData);

            var closestPoint = calculator.CalculateClosestIntersectionDistance(input);

            Console.WriteLine($"Closest Intersection Distance: {closestPoint}");

            var smallestDistance = calculator.CalculateSmallestNumberOfStepsToIntersection(input);

            Console.WriteLine($"Smallest Distance to intersection: {smallestDistance}");
        }
    }
}

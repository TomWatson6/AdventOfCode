using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;

namespace AOC2019_3
{
    

    public class WireCalculator
    {
        private readonly Point origin = new Point(0, 0);

        public int CalculateClosestIntersectionDistance(List<string[]> wires)
        {
            var intersectionPoints = this.GetIntersectionPoints(wires);

            var closestIntersectionDistance = GetClosestIntersectionDistance(intersectionPoints);

            return closestIntersectionDistance;
        }

        public int CalculateSmallestNumberOfStepsToIntersection(List<string[]> wires)
        {
            var intersectionPoints = this.GetIntersectionPoints(wires);

            var totalDistances = this.GetStepsToEachIntersection(wires, intersectionPoints);

            var smallest = totalDistances.Min(x => x);

            return smallest;
        }

        private List<int> GetStepsToEachIntersection(List<string[]> wires, List<Point> intersectionPoints)
        {
            var totalDistances = new Dictionary<Point, int>();

            int distance;
            var currentPosition = new Point(origin.X, origin.Y);

            foreach(var wire in wires)
            {
                distance = 0;
                currentPosition = new Point(origin.X, origin.Y);

                foreach(var movement in wire)
                {
                    var direction = movement.Substring(0, 1);
                    var magnitude = int.Parse(movement.Substring(1, movement.Length - 1));

                    for (int i = 0; i < magnitude; i++)
                    {
                        switch (direction)
                        {
                            case "L":
                                currentPosition.X--;
                                break;
                            case "R":
                                currentPosition.X++;
                                break;
                            case "U":
                                currentPosition.Y++;
                                break;
                            case "D":
                                currentPosition.Y--;
                                break;

                        }

                        distance++;

                        if(currentPosition.X == 303 && currentPosition.Y == 0)
                            Console.WriteLine("WTF");

                        if (intersectionPoints.Any(x => x == currentPosition))
                        {
                            if (totalDistances.TryGetValue(currentPosition, out var dist))
                                totalDistances[currentPosition] += distance;
                            else
                                totalDistances.Add(currentPosition, distance);
                        }


                    }
                }
            }

            return totalDistances.Select(x => x.Value).ToList();
        }

        private List<Point> GetIntersectionPoints(List<string[]> wires)
        {
            var wireActivity = new Dictionary<Point, HashSet<int>>();

            for(int i = 0; i < wires.Count; i++)
            {
                var currentPosition = new Point(origin.X, origin.Y);

                for(int j = 0; j < wires[i].Length; j++)
                {
                    var direction = wires[i][j].Substring(0, 1);
                    var magnitude = int.Parse(wires[i][j].Substring(1, wires[i][j].Length - 1));

                    for (int k = 0; k < magnitude; k++)
                    {
                        switch (direction)
                        {
                            case "L":
                                currentPosition.X--;
                                break;
                            case "R":
                                currentPosition.X++;
                                break;
                            case "U":
                                currentPosition.Y++;
                                break;
                            case "D":
                                currentPosition.Y--;
                                break;

                        }

                        if (wireActivity.TryGetValue(currentPosition, out var point))
                            wireActivity[currentPosition].Add(i);
                        else
                            wireActivity.Add(currentPosition, new HashSet<int>() { i });
                    }
                }
            }

            var intersectionPoints = wireActivity.Where(x => x.Value.Count > 1).Select(x => x.Key);

            return intersectionPoints.ToList();
        }

        private int GetClosestIntersectionDistance(List<Point> intersectionPoints)
        {
            var closest = intersectionPoints.Min(x => Math.Abs(x.X) + Math.Abs(x.Y));

            return closest;
        }
    }
}

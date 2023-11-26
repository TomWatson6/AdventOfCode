﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace AOC._2020.Day17
{
    public class Part2
    {
        private Dictionary<(long, long, long, long), char> Cubes;

        private long XLower;
        private long XUpper;
        private long YLower;
        private long YUpper;
        private long ZLower;
        private long ZUpper;
        private long WLower;
        private long WUpper;

        public Part2(Dictionary<(long, long, long, long), char> cubes)
        {
            this.Cubes = cubes;

            this.XLower = this.Cubes.Min(x => x.Key.Item1);
            this.XUpper = this.Cubes.Max(x => x.Key.Item1);
            this.YLower = this.Cubes.Min(x => x.Key.Item2);
            this.YUpper = this.Cubes.Max(x => x.Key.Item2);
            this.ZLower = this.Cubes.Min(x => x.Key.Item3);
            this.ZUpper = this.Cubes.Max(x => x.Key.Item3);
            this.WLower = this.Cubes.Min(x => x.Key.Item4);
            this.WUpper = this.Cubes.Max(x => x.Key.Item4);
        }

        public string Solve(long iterations)
        {
            for (int i = 0; i < iterations; i++)
            {
                var newCube = new Dictionary<(long, long, long, long), char>();

                this.ModifyCheckCubes();

                for (long x = XLower; x <= XUpper; x++)
                {
                    for (long y = YLower; y <= YUpper; y++)
                    {
                        for (long z = ZLower; z <= ZUpper; z++)
                        {
                            for (long w = WLower; w <= WUpper; w++)
                            {
                                var adjacents = this.GetAdjacents(x, y, z, w);
                                var activeNeighbours = adjacents.Where(x => x == '#');

                                if (this.Cubes[(x, y, z, w)] == '#')
                                {
                                    if (activeNeighbours.Count() != 2 && activeNeighbours.Count() != 3)
                                        newCube.Add((x, y, z, w), '.');
                                    else
                                        newCube.Add((x, y, z, w), '#');
                                }
                                else
                                {
                                    if (activeNeighbours.Count() == 3)
                                        newCube.Add((x, y, z, w), '#');
                                    else
                                        newCube.Add((x, y, z, w), '.');
                                }
                            }
                        }
                    }
                }

                this.Cubes = newCube;
            }

            Console.WriteLine("Number of cubes: " + this.Cubes.Count().ToString());

            return this.Cubes.Select(x => x.Value).Where(x => x == '#').Count().ToString();
        }

        private char[] GetAdjacents(long xCurrent, long yCurrent, long zCurrent, long wCurrent)
        {
            var adjacents = new List<char>();

            for (int x = -1; x <= 1; x++)
            {
                for (int y = -1; y <= 1; y++)
                {
                    for (int z = -1; z <= 1; z++)
                    {
                        for (int w = -1; w <= 1; w++)
                        {
                            if (!(x == 0 && y == 0 && z == 0 && w == 0))
                            {
                                if (this.Cubes.TryGetValue((xCurrent + x, yCurrent + y, zCurrent + z, wCurrent + w), out var value))
                                {
                                    adjacents.Add(value);
                                    //Console.WriteLine($"Could Get: [{x}, {y}, {z}] with value: {value}");
                                }
                                //else
                                //{
                                //    Console.WriteLine($"Couldn't Get: [{x}, {y}, {z}]");
                                //}
                            }
                        }
                    }
                }
            }

            return adjacents.ToArray();
        }

        private void ModifyCheckCubes()
        {
            for (long y = this.YLower - 1; y <= this.YUpper + 1; y++)
            {
                for (long z = this.ZLower - 1; z <= this.ZUpper + 1; z++)
                {
                    for (long w = this.WLower - 1; w <= this.WUpper + 1; w++)
                    {
                        this.Cubes.TryAdd((this.XLower - 1, y, z, w), '.');
                        this.Cubes.TryAdd((this.XUpper + 1, y, z, w), '.');
                    }
                }
            }

            for (long x = this.XLower - 1; x <= this.XUpper + 1; x++)
            {
                for (long z = this.ZLower - 1; z <= this.ZUpper + 1; z++)
                {
                    for (long w = this.WLower - 1; w <= this.WUpper + 1; w++)
                    {
                        this.Cubes.TryAdd((x, this.YLower - 1, z, w), '.');
                        this.Cubes.TryAdd((x, this.YUpper + 1, z, w), '.');
                    }
                }
            }

            for (long x = this.XLower - 1; x <= this.XUpper + 1; x++)
            {
                for (long y = this.YLower - 1; y <= this.YUpper + 1; y++)
                {
                    for (long w = this.WLower - 1; w <= this.WUpper + 1; w++)
                    {
                        this.Cubes.TryAdd((x, y, this.ZLower - 1, w), '.');
                        this.Cubes.TryAdd((x, y, this.ZUpper + 1, w), '.');
                    }
                }
            }

            for (long x = this.XLower - 1; x <= this.XUpper + 1; x++)
            {
                for (long y = this.YLower - 1; y <= this.YUpper + 1; y++)
                {
                    for (long z = this.ZLower - 1; z <= this.ZUpper + 1; z++)
                    {
                        this.Cubes.TryAdd((x, y, z, this.WLower - 1), '.');
                        this.Cubes.TryAdd((x, y, z, this.WUpper + 1), '.');
                    }
                }
            }

            this.XLower--;
            this.XUpper++;
            this.YLower--;
            this.YUpper++;
            this.ZLower--;
            this.ZUpper++;
            this.WLower--;
            this.WUpper++;
        }
    }
}

using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Net.Http.Headers;
using System.Runtime.CompilerServices;
using System.Threading.Tasks;

namespace AOC._2020.Day24
{
    class Program
    {
        static readonly (double x, double y)[] Adjacents =
        {
            (1.0, 0.0),
            (-1.0, 0.0),
            (0.5, 1),
            (-0.5, 1),
            (0.5, -1),
            (-0.5, -1)
        };

        static void Main(string[] args)
        {
            var reader = new FileReader();

            var tiles = reader.Read("input.txt");

            var part1 = tiles.Where(x => x.Value % 2 == 1).Count();

            Console.WriteLine("Part 1: " + part1);
            Console.WriteLine();

            var cDictionary = new ConcurrentDictionary<(double x, double y), long>();

            foreach (var kvp in tiles)
                cDictionary.TryAdd(kvp.Key, kvp.Value);

            var part2 = Part2(cDictionary);

            Console.WriteLine("Part 2: " + part2);
        }

        static long Part2(ConcurrentDictionary<(double x, double y), long> tiles)
        {
            var stopwatch = new Stopwatch();

            for(int i = 1; i <= 100; i++)
            {
                ExpandTiles(tiles);

                var newTiles = new ConcurrentDictionary<(double x, double y), long>();

                Parallel.ForEach(tiles, tile =>
                {
                    var adjacents = GetAdjacents(tiles, tile.Key.x, tile.Key.y);

                    var surroundingBlacks = tiles.Where(x => adjacents.Any(y => y == x.Key && x.Value % 2 == 1)).Count();

                    if (tile.Value % 2 == 1)
                    {
                        if (surroundingBlacks == 0 || surroundingBlacks > 2)
                            newTiles.TryAdd(tile.Key, tile.Value + 1);
                        else
                            newTiles.TryAdd(tile.Key, tile.Value);
                    }

                    if (tile.Value % 2 == 0)
                    {
                        if (surroundingBlacks == 2)
                            newTiles.TryAdd(tile.Key, tile.Value + 1);
                        else
                            newTiles.TryAdd(tile.Key, tile.Value);
                    }
                });

                tiles = newTiles;

                RemoveExcess(tiles);

                Console.WriteLine($"Day {i}:" + tiles.Where(x => x.Value % 2 == 1).Count() + " With Number of Tiles: " + tiles.Count());

                //Console.WriteLine($"Iteration {i} Completed -- Time: {expansionTime} (Expansion) - {adjacentTime} (Adjacents) - {surroundingBlackTime} (Surrounding Black) - {remainingTime} - (Remaining)");
            }

            return tiles.Where(x => x.Value % 2 == 1).Count();
        }

        static void RemoveExcess(ConcurrentDictionary<(double x, double y), long> tiles)
        {
            var toRemove = new ConcurrentDictionary<(double x, double y), byte>();

            Parallel.ForEach(tiles, tile =>
            {
                var adjacents = GetAdjacents(tiles, tile.Key.x, tile.Key.y);
                var surroundingBlacks = tiles.Where(x => adjacents.Any(y => y == x.Key && x.Value % 2 == 1)).Count();
                if (surroundingBlacks == 0 && tile.Value == 0)
                {
                    toRemove.TryAdd(tile.Key, 1);
                }
            });

            Parallel.ForEach(toRemove, removable =>
            {
                tiles.Remove(removable.Key, out long value);
            });
        }

        static void ExpandTiles(ConcurrentDictionary<(double x, double y), long> tiles)
        {
            var toAdd = new ConcurrentDictionary<(double x, double y), byte>();

            Parallel.ForEach(tiles, tile =>
            {
                var adjacents = GetAdjacents(tiles, tile.Key.x, tile.Key.y);

                foreach (var adj in adjacents)
                {
                    if (!tiles.ContainsKey(adj))
                        toAdd.TryAdd(adj, 1);
                }
            });

            Parallel.ForEach(toAdd, addition =>
            {
                tiles.TryAdd(addition.Key, 0);
            });
        }

        static (double x, double y)[] GetAdjacents(ConcurrentDictionary<(double x, double y), long> tiles, double x, double y)
        {
            var adjacents = new ConcurrentDictionary<(double x, double y), byte>();

            Parallel.ForEach(Adjacents, adj =>
            {
                adjacents.TryAdd((x + adj.x, y + adj.y), 1);
            });

            //var adjacents = Adjacents.Select(z => (z.x + x, z.y + y)).ToArray();

            return adjacents.Select(x => x.Key).ToArray();
        }
    }
}

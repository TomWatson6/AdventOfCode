using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;

namespace AOC._2020.Day11
{
    public class Part1
    {
        private readonly int dimX = 0;
        private readonly int dimY = 0;
        private char[][] grid;

        public Part1(char[][] grid)
        {
            this.dimX = grid.Length;
            this.dimY = grid.First().Length;
            this.grid = grid;
        }

        public string Solve()
        {
            var changed = false;

            var iterations = 0;

            do
            {
                var newGrid = new List<List<char>>();

                changed = false;

                for (int x = 0; x < this.dimX; x++)
                {
                    newGrid.Add(new List<char>());

                    for (int y = 0; y < this.dimY; y++)
                    {
                        newGrid[x].Add(this.grid[x][y]);

                        if (this.grid[x][y] == 'L')
                        {
                            var adjSeats = this.GetAdjacentSeats(x, y);

                            if (adjSeats.All(x => x == 'L' || x == '.'))
                            {
                                newGrid[x][y] = '#';
                                changed = true;
                            }
                        }
                        else if (this.grid[x][y] == '#')
                        {
                            var adjSeats = this.GetAdjacentSeats(x, y);

                            if (adjSeats.Where(x => x == '#').Count() >= 4)
                            {
                                newGrid[x][y] = 'L';
                                changed = true;
                            }
                        }
                    }
                }

                this.grid = newGrid.Select(x => x.ToArray()).ToArray();

                iterations++;

                //File.WriteAllText("output" + iterations + ".txt", string.Join("\r\n", this.grid.Select(x => string.Join("", x.Select(y => y)))));                
            } while (changed);

            var occupiedSeats = this.grid.Select(x => x.Where(y => y == '#').Count()).Sum();

            Console.WriteLine("Iterations: " + iterations);

            return occupiedSeats.ToString();
        }

        private char[] GetAdjacentSeats(int x, int y)
        {
            var seats = new List<char>();

            if(x != 0)
            {
                if (y != 0)
                    seats.Add(this.grid[x - 1][y - 1]);

                seats.Add(this.grid[x - 1][y]);

                if (y != this.dimY - 1)
                    seats.Add(this.grid[x - 1][y + 1]);
            }

            if (y != 0)
                seats.Add(this.grid[x][y - 1]);

            if (y != this.dimY - 1)
                seats.Add(this.grid[x][y + 1]);

            if(x != this.dimX - 1)
            {
                if (y != 0)
                    seats.Add(this.grid[x + 1][y - 1]);

                seats.Add(this.grid[x + 1][y]);

                if (y != this.dimY - 1)
                    seats.Add(this.grid[x + 1][y + 1]);
            }

            return seats.ToArray();
        }
    }
}

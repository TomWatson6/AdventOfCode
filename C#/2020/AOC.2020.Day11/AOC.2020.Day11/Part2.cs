using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;

namespace AOC._2020.Day11
{
    public class Part2
    {
        private readonly int dimX = 0;
        private readonly int dimY = 0;
        private char[][] grid;

        public Part2(char[][] grid)
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
                            var adjSeats = this.GetSeenAdjacentSeats(x, y);

                            if (adjSeats.All(x => x == 'L' || x == '.'))
                            {
                                newGrid[x][y] = '#';
                                changed = true;
                            }
                        }
                        else if (this.grid[x][y] == '#')
                        {
                            var adjSeats = this.GetSeenAdjacentSeats(x, y);

                            if (adjSeats.Where(x => x == '#').Count() >= 5)
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

        private bool isOutsideOfSeats(int x, int y)
        {
            if (x < 0 || y < 0 || x > this.dimX - 1 || y > this.dimY - 1)
                return true;

            return false;
        }

        private char GetSeenSeat(int x, int y, Func<Point, Point> direction)
        {
            var output = '-';

            var currentPos = direction.Invoke(new Point(x, y));

            while(!isOutsideOfSeats(currentPos.X, currentPos.Y))
            { 
                if (this.grid[currentPos.X][currentPos.Y] == 'L' || this.grid[currentPos.X][currentPos.Y] == '#')
                {
                    output = this.grid[currentPos.X][currentPos.Y];
                    break;
                }

                currentPos = direction.Invoke(currentPos);
            }

            return output;
        }

        private char[] GetSeenAdjacentSeats(int x, int y)
        {
            var seats = new List<char>();

            seats.Add(this.GetSeenSeat(x, y, p => new Point(p.X - 1, p.Y - 1)));
            seats.Add(this.GetSeenSeat(x, y, p => new Point(p.X, p.Y - 1)));
            seats.Add(this.GetSeenSeat(x, y, p => new Point(p.X + 1, p.Y - 1)));
            seats.Add(this.GetSeenSeat(x, y, p => new Point(p.X + 1, p.Y)));
            seats.Add(this.GetSeenSeat(x, y, p => new Point(p.X + 1, p.Y + 1)));
            seats.Add(this.GetSeenSeat(x, y, p => new Point(p.X, p.Y + 1)));
            seats.Add(this.GetSeenSeat(x, y, p => new Point(p.X - 1, p.Y + 1)));
            seats.Add(this.GetSeenSeat(x, y, p => new Point(p.X - 1, p.Y)));

            return seats.Where(x => x != '-').ToArray();
        }
    }
}

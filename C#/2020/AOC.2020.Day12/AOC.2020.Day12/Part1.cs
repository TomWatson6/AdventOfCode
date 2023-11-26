using System;
using System.Collections.Generic;
using System.Drawing;
using System.Runtime.CompilerServices;
using System.Text;

namespace AOC._2020.Day12
{
    public class Part1
    {
        private readonly Dictionary<int, string> directions = new Dictionary<int, string>();

        private (int, Point) currentState = (1, new Point(0, 0));

        public Part1()
        {
            this.directions.Add(0, "N");
            this.directions.Add(1, "E");
            this.directions.Add(2, "S");
            this.directions.Add(3, "W");
        }

        public string Solve((string, int)[] instructions)
        {
            foreach(var instruction in instructions)
            {
                switch(instruction.Item1)
                {
                    case "N":
                        this.currentState.Item2.Y += instruction.Item2;
                        break;
                    case "E":
                        this.currentState.Item2.X += instruction.Item2;
                        break;
                    case "S":
                        this.currentState.Item2.Y -= instruction.Item2;
                        break;
                    case "W":
                        this.currentState.Item2.X -= instruction.Item2;
                        break;
                    case "L":
                        this.currentState.Item1 -= instruction.Item2 / 90;
                        break;
                    case "R":
                        this.currentState.Item1 += instruction.Item2 / 90;
                        break;
                    case "F":
                        switch(this.directions[this.currentState.Item1 % 4 < 0 ? this.currentState.Item1 % 4 + 4 : this.currentState.Item1 % 4])
                        {
                            case "N":
                                this.currentState.Item2.Y += instruction.Item2;
                                break;
                            case "E":
                                this.currentState.Item2.X += instruction.Item2;
                                break;
                            case "S":
                                this.currentState.Item2.Y -= instruction.Item2;
                                break;
                            case "W":
                                this.currentState.Item2.X -= instruction.Item2;
                                break;
                        }
                        break;
                }

                //Console.WriteLine("Instruction: " + instruction.Item1 + instruction.Item2 + " \t=> Facing " + (this.directions[this.currentState.Item1 % 4 < 0 ? this.currentState.Item1 % 4 + 4 : this.currentState.Item1 % 4]) +
                //    " \tCurrent Position: [" + this.currentState.Item2.X + ", " + this.currentState.Item2.Y + "]");
            }

            return (Math.Abs(this.currentState.Item2.X) + Math.Abs(this.currentState.Item2.Y)).ToString();
        }
    }
}

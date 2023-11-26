using System;
using System.Collections.Generic;
using System.Drawing;
using System.Text;

namespace AOC._2020.Day12
{
    class Part2
    {
        private Point shipLocation = new Point(0, 0);
        private Point waypointLocation = new Point(10, 1);

        public string Solve((string, int)[] instructions)
        {
            foreach (var instruction in instructions)
            {
                switch (instruction.Item1)
                {
                    case "N":
                        waypointLocation.Y += instruction.Item2;
                        break;
                    case "E":
                        waypointLocation.X += instruction.Item2;
                        break;
                    case "S":
                        waypointLocation.Y -= instruction.Item2;
                        break;
                    case "W":
                        waypointLocation.X -= instruction.Item2;
                        break;
                    case "L":
                        this.Rotate(instruction.Item1, instruction.Item2);
                        break;
                    case "R":
                        this.Rotate(instruction.Item1, instruction.Item2);
                        break;
                    case "F":
                        var x = this.waypointLocation.X - this.shipLocation.X;
                        var y = this.waypointLocation.Y - this.shipLocation.Y;

                        for (int i = 0; i < instruction.Item2; i++)
                        {
                            this.shipLocation.X += x;
                            this.shipLocation.Y += y;
                            this.waypointLocation.X += x;
                            this.waypointLocation.Y += y;
                        }

                        break;
                }

                //Console.WriteLine("Instruction: " + instruction.Item1 + instruction.Item2 + " \t=> Ship Location: [" + this.shipLocation.X + ", " + this.shipLocation.Y + "] Waypoint Location: [" +
                //    this.waypointLocation.X + ", " + this.waypointLocation.Y + "]");
            }

            return (Math.Abs(this.shipLocation.X) + Math.Abs(this.shipLocation.Y)).ToString();
        }

        private void Rotate(string direction, int degrees)
        {
            if (direction == "L")
                degrees = ((degrees % 360) * -1) + 360;

            var countClockwise = 0;

            switch(degrees)
            {
                case 90:
                    countClockwise = 1;
                    break;
                case 180:
                    countClockwise = 2;
                    break;
                case 270:
                    countClockwise = 3;
                    break;
            }

            for(int i = 0; i < countClockwise; i++)
            {
                var relativePoint = new Point(this.waypointLocation.X - this.shipLocation.X, this.waypointLocation.Y - this.shipLocation.Y);

                var translation = new Point(relativePoint.Y, -relativePoint.X);

                this.waypointLocation = new Point(this.shipLocation.X + translation.X, this.shipLocation.Y + translation.Y);
            }
        }
    }
}

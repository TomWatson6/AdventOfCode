using System;
using System.Collections.Generic;
using System.Drawing;
using System.Text;

namespace AOC2019_10
{
    public class AsteroidField
    {
        public AsteroidField(char[,] spaceObjects, int xDim, int yDim)
        {
            this.SpaceObjects = new SpaceObject[xDim, yDim];

            this.XDim = xDim;
            this.YDim = yDim;

            for(int x = 0; x < xDim; x++)
            {
                for(int y = 0; y < yDim; y++)
                {
                    this.SpaceObjects[x, y] = new SpaceObject(spaceObjects[x, y]);
                }
            }
        }

        public SpaceObject[,] SpaceObjects { get; set; }
        public int XDim { get; set; }
        public int YDim { get; set; }

        public int GetVisibleAsteroids(Point p)
        {
            var blockedAsteroids = this.GetLongLatBlockedAsteroids(p);
            blockedAsteroids += this.GetDiagonalBlockedAsteroids(p);

            return blockedAsteroids;
        }

        public int GetLongLatBlockedAsteroids(Point p)
        {
            int countAA = 0;
            int countAB = 0;

            for(int x = 0; x < this.XDim; x++)
            {
                if (this.SpaceObjects[x, p.Y].SpaceObjectType == SpaceObjectType.Asteroid)
                {
                    if (x < p.X)
                        countAA++;
                    else
                        countAB++;
                }
            }

            countAA -= 1;
            if (countAA < 0)
                countAA = 0;

            countAB -= 1;
            if (countAB < 0)
                countAB = 0;

            int countA = countAA + countAB;

            int countBA = 0;
            int countBB = 0;

            for (int y = 0; y < this.YDim; y++)
            {
                if (this.SpaceObjects[p.X, y].SpaceObjectType == SpaceObjectType.Asteroid)
                {
                    if (y < p.Y)
                        countBA++;
                    else
                        countBB++;
                }
            }

            countBA -= 1;
            if (countBA < 0)
                countBA = 0;

            countBB -= 1;
            if (countBB < 0)
                countBB = 0;

            int countB = countBA + countBB;

            var count = countA + countB;

            return count;
        }

        public int GetDiagonalBlockedAsteroids(Point p)
        {
            int smallestDistance = p.X < p.Y ? p.X : p.Y;

            var startingPoint = new Point(p.X - smallestDistance, p.Y - smallestDistance);

            int countAA = 0;
            int countAB = 0;

            for (var point = startingPoint; point.X < this.XDim && point.Y < this.YDim; point.X++, point.Y++)
            {
                if (this.SpaceObjects[point.X, point.Y].SpaceObjectType == SpaceObjectType.Asteroid)
                {
                    if (point.X > p.X && point.Y > p.Y)
                        countAA++;
                    else
                        countAB++;
                }
            }

            countAA -= 1;
            if (countAA < 0)
                countAA = 0;

            countAB -= 1;
            if (countAB < 0)
                countAB = 0;

            int countA = countAA + countAB;

            smallestDistance = p.X < this.YDim - p.Y ? p.X : this.YDim - p.Y;

            startingPoint = new Point(p.X - smallestDistance, p.Y + smallestDistance - 1);

            int countBA = 0;
            int countBB = 0;

            for (var point = startingPoint; point.X < this.XDim && point.Y >= 0; point.X++, point.Y--)
            {
                if (this.SpaceObjects[point.X, point.Y].SpaceObjectType == SpaceObjectType.Asteroid)
                {
                    if (point.X > p.X && point.Y < p.Y)
                        countBA++;
                    else
                        countBB++;
                }
            }

            countBA -= 1;
            if (countBA < 0)
                countBA = 0;

            countBB -= 1;
            if (countBB < 0)
                countBB = 0;

            int countB = countBA + countBB;

            var count = countA + countB;

            return count;
        }
    }
}

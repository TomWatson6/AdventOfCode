using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace AOC2019_6
{
    public class SpaceObject
    {
        public SpaceObject(string name, SpaceObject objectOrbitted = null)
        {
            this.Name = name;
            this.ObjectOrbitted = ObjectOrbitted;
        }

        public SpaceObject(SpaceObject spaceObject)
        {
            this.Name = spaceObject.Name;
            this.ObjectOrbitted = spaceObject.ObjectOrbitted;
        }

        public string Name { get; set; }
        public SpaceObject ObjectOrbitted { get; set; }

        public int GetOrbits()
        {
            if (this.ObjectOrbitted != null)
                return this.ObjectOrbitted.GetOrbits() + 1;
            else
                return 0;
        }

        public List<SpaceObject> GetOrbittedObjects()
        {
            var currentObject = this.ObjectOrbitted;
            var spaceObjects = new List<SpaceObject> { new SpaceObject(currentObject) };

            while(currentObject != null)
            {
                currentObject = currentObject.ObjectOrbitted;

                if (currentObject != null)
                    spaceObjects.Add(new SpaceObject(currentObject));
            }

            return spaceObjects;
        }

        public int GetDistance(Dictionary<string, SpaceObject> spaceObjectLibrary, string destinationName)
        {
            var originObjects = this.GetOrbittedObjects().Select(x => x.Name);
            
            if(spaceObjectLibrary.TryGetValue(destinationName, out var destination))
            {
                var destinationObjects = destination.GetOrbittedObjects().Select(x => x.Name);

                var commonObject = originObjects.First(x => destinationObjects.Any(y => x == y));

                var distFromOrigin = originObjects.ToList().IndexOf(commonObject);
                var distFromDestination = destinationObjects.ToList().IndexOf(commonObject);

                var totalDist = distFromOrigin + distFromDestination;

                return totalDist;
            }
            else
            {
                return -1;
            }
        }
    }
}

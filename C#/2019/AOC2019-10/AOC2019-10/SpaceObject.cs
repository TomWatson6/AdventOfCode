namespace AOC2019_10
{
    public enum SpaceObjectType
    {
        Asteroid,
        Nothing
    }

    public class SpaceObject
    {
        public SpaceObject(char @object)
        {
            switch(@object)
            {
                case '#':
                    this.SpaceObjectType = SpaceObjectType.Asteroid;
                    break;
                default:
                    this.SpaceObjectType = SpaceObjectType.Nothing;
                    break;
            }
        }

        public SpaceObjectType SpaceObjectType { get; set; }
    }
}
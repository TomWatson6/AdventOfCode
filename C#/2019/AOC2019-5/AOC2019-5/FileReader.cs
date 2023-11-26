using System.IO;

namespace AOC2019_5
{
    public class FileReader
    {
        public string Get(string path)
        {
            return File.ReadAllText(path);
        }
    }
}

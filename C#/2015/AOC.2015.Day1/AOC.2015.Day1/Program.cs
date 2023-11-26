using System;
using System.IO;

namespace AOC._2015.Day1
{
    class Program
    {
        static void Main(string[] args)
        {
            var input = File.ReadAllText("input.txt");

            var floor = 0;

            for(int i = 0; i < input.Length; i++)
            {
                floor += input[i] == '(' ? 1 : -1;

                if(floor == -1)
                {
                    Console.WriteLine("character pos that makes go into basement: " + (i + 1));
                    break;
                }
            }
        }
    }
}

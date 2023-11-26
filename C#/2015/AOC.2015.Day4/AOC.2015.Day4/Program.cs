using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;

namespace AOC._2015.Day4
{
    class Program
    {
        static readonly string input = "iwrupvqb";
        static readonly string inputTest = "abcdef609043";

        static void Main(string[] args)
        {
            var counter = 1;
            

            while (counter <= 10000000)
            {
                var md5 = MD5.Create();
                var toHash = input + counter;

                var output = BitConverter.ToString(md5.ComputeHash(Encoding.ASCII.GetBytes(toHash))).Replace("-", "");

                if (output.StartsWith("000000"))
                    break;

                counter++;
            }

            Console.WriteLine("Lowest Number: " + counter);
        }
    }
}

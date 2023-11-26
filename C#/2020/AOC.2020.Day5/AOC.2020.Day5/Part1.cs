using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;

namespace AOC._2020.Day5
{
    public class Part1
    {
        public string Solve(string[] input)
        {
            var seats = new List<Seat>();

            foreach(var specification in input)
            {
                seats.Add(new Seat(specification));
            }

            seats = seats.OrderBy(x => x.Column).ToList();
            seats = seats.OrderBy(x => x.Row).ToList();

            var lowest = seats.Min(x => x.Row);
            var highest = seats.Max(x => x.Row);

            var output = new List<string>();

            for(int i = lowest; i <= highest; i++)
            {
                for(int j = 0; j < 8; j++)
                {
                    if (seats.Any(x => x.Row == i && x.Column == j))
                    {
                        Console.Write("O");
                    }
                    else
                    {
                        Console.Write("X");
                        output.Add("Row: " + i + " Column: " + j);
                    }
                }

                Console.WriteLine();
            }

            foreach(var o in output)
            {
                Console.WriteLine(o);
            }

            var ids = seats.Select(x => x.Id);

            var largestId = ids.Max(x => x);

            return "The Largest ID is: " + largestId;
        }
    }
}
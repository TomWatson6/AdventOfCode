using System;
using System.Collections.Generic;
using System.Security.Cryptography.X509Certificates;
using System.Text;

namespace AOC._2020.Day8
{
    public class Part1
    {
        public string Solve(string[] input)
        {
            var indexesVisited = new HashSet<int>();
            var current = 0;
            var accumulator = 0;
            var iterations = 0;

            while(true)
            {
                if (indexesVisited.Contains(current))
                    break;

                indexesVisited.Add(current);

                var opCode = input[current].Split(" ")[0];

                var number = input[current].Split(" ")[1];

                var operand = 0;

                if (number.StartsWith("+"))
                    operand = int.Parse(number.Substring(1, number.Length - 1));
                else
                    operand = int.Parse(number);

                switch(opCode)
                {
                    case "acc":
                        accumulator += operand;
                        current++;
                        break;
                    case "jmp":
                        current += operand;
                        break;
                    default:
                        current++;
                        break;
                }

                iterations++;
            }

            Console.WriteLine("Iterations: " + iterations);

            return accumulator.ToString();
        }
    }
}

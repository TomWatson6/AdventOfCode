using System;
using System.Collections.Generic;
using System.Text;

namespace AOC._2020.Day8
{
    public class Part2
    {
        public string Solve(string[] input)
        {
            var indexesVisited = new HashSet<int>();
            var current = 0;
            var accumulator = 0;
            //var iterations = 0;
            var repeating = false;

            for (int i = 0; i < input.Length; i++)
            {
                current = 0;
                repeating = false;

                string[] inputCopy = new string[input.Length];
                input.CopyTo(inputCopy, 0);

                var split = input[i].Split(" ");

                if (split[0] == "nop")
                    split[0] = "jmp";
                else if (split[0] == "jmp")
                    split[0] = "nop";
                else
                    continue;

                inputCopy[i] = string.Join(" ", split);

                while (true)
                {
                    if (indexesVisited.Contains(current))
                    {
                        repeating = true;
                        break;
                    }

                    indexesVisited.Add(current);

                    var opCode = inputCopy[current].Split(" ")[0];

                    var number = inputCopy[current].Split(" ")[1];

                    var operand = 0;

                    if (number.StartsWith("+"))
                        operand = int.Parse(number.Substring(1, number.Length - 1));
                    else
                        operand = int.Parse(number);

                    switch (opCode)
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

                    //iterations++;

                    if (current >= inputCopy.Length)
                        break;
                }

                //Console.WriteLine("Iterations: " + iterations);
                //iterations = 0;

                if (repeating)
                {
                    accumulator = 0;
                    indexesVisited = new HashSet<int>();
                }
                else
                {
                    Console.WriteLine("Index Changed: " + i + ", String is: " + input[i] + " -> " + inputCopy[i]);
                    break;
                }
            }

            return accumulator.ToString();
        }
    }
}

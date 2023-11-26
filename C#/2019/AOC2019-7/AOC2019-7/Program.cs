using System;
using System.Diagnostics;
using System.Linq;

namespace AOC2019_7
{
    public class Program
    {
        private static readonly string InputPath = "./TestData.txt";
        private static readonly int[] Input;
        private static readonly int AmplifierCount = 5;

        private static readonly FileReader fileReader = new FileReader();
        private static readonly InputParser inputParser = new InputParser();

        static Program()
        {
            var text = fileReader.Get(InputPath);

            Input = inputParser.Parse(text);
        }

        static void Main(string[] args)
        {
            var amps = new IntCodeComputer[AmplifierCount];

            for (int i = 0; i < amps.Length; i++)
            {
                amps[i] = new IntCodeComputer(Input);
            }

            int output = 0;

            int ax = 0;
            int bx = 0;
            int cx = 0;
            int dx = 0;
            int ex = 0;

            for (int a = 5; a < AmplifierCount + 5; a++)
            {
                for (int b = 5; b < AmplifierCount + 5; b++)
                {
                    for (int c = 5; c < AmplifierCount + 5; c++)
                    {
                        for (int d = 5; d < AmplifierCount + 5; d++)
                        {
                            for (int e = 5; e < AmplifierCount + 5; e++)
                            {
                                var array = new int[] { a, b, c, d, e };

                                if (array.Distinct().Count() < AmplifierCount)
                                    continue;

                                for (int i = 0; i < amps.Length; i++)
                                {
                                    amps[i].Input = Input;
                                }

                                var sw = new Stopwatch();
                                sw.Start();
                                ax = amps[0].Run(a, ex);
                                bx = amps[1].Run(b, ax);
                                cx = amps[2].Run(c, bx);
                                dx = amps[3].Run(d, cx);
                                ex = amps[4].Run(e, dx);
                                sw.Stop();
                                Console.WriteLine("Time Taken: " + sw.ElapsedMilliseconds);

                                output = ex > output ? ex : output;
                            }
                        }
                    }
                }
            }

            //for (int i = 0; i < amps.Length; i++)
            //{
            //    amps[i] = new IntCodeComputer((int[])Input.Clone());
            //}

            //for(int i = 1; i < AmplifierCount; i++)
            //{
            //    for(int j = 2; j < 25; j++)
            //    {
            //        Console.WriteLine("Output: " + amps[0].Run(i, j));
            //    }
            //}

            Console.WriteLine($"Output: {output}");
            Console.ReadLine();
        }
    }
}

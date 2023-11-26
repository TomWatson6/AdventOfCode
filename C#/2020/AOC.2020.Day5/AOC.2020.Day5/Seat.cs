using System;
using System.Collections.Generic;
using System.Text;

namespace AOC._2020.Day5
{
    public class Seat
    {
        public Seat(string specification)
        {
            specification = specification.Replace("F", "-");
            specification = specification.Replace("B", "+");
            specification = specification.Replace("R", "+");
            specification = specification.Replace("L", "-");

            var rowSpec = specification.Substring(0, 7);
            var columnSpec = specification.Substring(7, 3);

            this.Row = this.Decipher(rowSpec, 127);
            this.Column = this.Decipher(columnSpec, 7);
        }

        public int Row { get; set; }
        public int Column { get; set; }
        public int Id => Row * 8 + Column;

        private int Decipher(string spec, int size)
        {
            var shift = (size + 1) / 2;

            var lowerBound = 0;
            var upperBound = size;

            while(lowerBound != upperBound)
            {
                var item = spec.Substring(0, 1);
                spec = spec.Substring(1, spec.Length - 1);

                if(item == "+")
                {
                    lowerBound += shift;
                }
                else
                {
                    upperBound -= shift;
                }

                shift /= 2;
            }

            return lowerBound;
        }

        //private int Decipher(string spec, int size)
        //{
        //    size /= 2;

        //    var currentPos = size;

        //    foreach(var character in spec)
        //    {
        //        size /= 2;

        //        if(character == '+')
        //        {
        //            currentPos += size;
        //        }
        //        else
        //        {
        //            currentPos -= size;
        //        }
        //    }

        //    return currentPos;
        //}
    }
}
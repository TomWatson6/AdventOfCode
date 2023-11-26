using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;

namespace AOC._2020.Day16
{
    public class Part1
    {
        public string Solve(TicketInfo ticketInfo)
        {
            var errors = new List<long>();

            foreach(var nearbyTicket in ticketInfo.NearbyTickets)
            {
                foreach(var number in nearbyTicket)
                {
                    if(!ticketInfo.Rules.Any(x => x.Value.Any(y => this.IsWithinRange(y.Item1, y.Item2, number))))
                    {
                        errors.Add(number);
                        break;
                    }
                }
            }

            return errors.Sum().ToString();
        }

        private bool IsWithinRange(long lower, long upper, long value)
        {
            return value >= lower && value <= upper;
        }
    }
}

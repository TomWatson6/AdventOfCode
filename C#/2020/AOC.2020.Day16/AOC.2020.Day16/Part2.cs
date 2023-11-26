using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace AOC._2020.Day16
{
    public class Part2
    {
        public string Solve(TicketInfo ticketInfo)
        {
            var validTickets = new List<long[]>();

            foreach (var nearbyTicket in ticketInfo.NearbyTickets)
            {
                var invalid = false;

                foreach (var number in nearbyTicket)
                {
                    if (!ticketInfo.Rules.Any(x => x.Value.Any(y => this.IsWithinRange(y.Item1, y.Item2, number))))
                    {
                        invalid = true;
                        break;
                    }
                }

                if (invalid)
                    continue;

                validTickets.Add(nearbyTicket);
            }

            validTickets.Add(ticketInfo.MyTicket);

            var ticketPossibilities = new List<(long, HashSet<string>)[]>();

            foreach(var ticket in validTickets)
            {
                var ticketPos = new List<(long, HashSet<string>)>();

                foreach(var value in ticket)
                {
                    var possibleFields = new HashSet<string>();

                    foreach (var rule in ticketInfo.Rules)
                    {
                        if (rule.Value.Any(x => this.IsWithinRange(x.Item1, x.Item2, value)))
                            possibleFields.Add(rule.Key);
                    }

                    ticketPos.Add((value, possibleFields));
                }

                ticketPossibilities.Add(ticketPos.ToArray());
            }

            var distinguishingTickets = ticketPossibilities.Where(x => x.Any(y => y.Item2.Count() < 20)).ToArray();

            var intersections = new Dictionary<long, string[]>();

            for(int i = 0; i < ticketInfo.MyTicket.Length; i++)
            {
                var possibilities = new List<string>();

                var possibleFields = distinguishingTickets.Select(x => x[i].Item2);

                foreach(var rule in ticketInfo.Rules.Select(x => x.Key).ToArray())
                {
                    if (possibleFields.All(x => x.Contains(rule)))
                        possibilities.Add(rule);
                }

                intersections.Add(i, possibilities.ToArray());
            }

            var establishedFields = new Dictionary<string, long>();

            var orderedIntersections = intersections.OrderBy(x => x.Value.Count()).ToArray();

            var resetI = false;

            for(int i = 0; i < orderedIntersections.Count() || resetI; i++)
            {
                if (resetI)
                    i = 0;

                resetI = false;

                if (orderedIntersections.Count() > 0)
                {
                    if (orderedIntersections[i].Value.Count() == 1)
                    {
                        establishedFields.Add(orderedIntersections[i].Value[0], orderedIntersections[i].Key);

                        for (int j = 0; j < orderedIntersections.Count(); j++)
                        {
                            orderedIntersections[j] = KeyValuePair.Create(orderedIntersections[j].Key,
                                orderedIntersections[j].Value.Where(x => x != establishedFields.Last().Key).ToArray());
                        }

                        orderedIntersections = orderedIntersections.Where(x => x.Value.Length > 0).OrderBy(x => x.Value.Count()).ToArray();

                        resetI = true;
                    }
                }
            }

            var output = establishedFields.Where(x => x.Key.StartsWith("departure")).Select(x => x.Value);

            long product = 1;

            foreach(var @out in output)
            {
                product *= ticketInfo.MyTicket[@out];
                Console.WriteLine(@out);
            }

            return product.ToString();
        }

        private bool IsWithinRange(long lower, long upper, long value)
        {
            return value >= lower && value <= upper;
        }

        private bool IsWithinRangeExclusive(long lower, long upper, long value)
        {
            return value > lower && value < upper;
        }
    }
}

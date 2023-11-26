using System;
using System.Collections.Generic;
using System.Text;

namespace AOC._2020.Day16
{
    public class TicketInfo
    {
        public TicketInfo(Dictionary<string, (long, long)[]> rules, long[] myTicket, long[][] nearbyTickets)
        {
            this.Rules = rules;
            this.MyTicket = myTicket;
            this.NearbyTickets = nearbyTickets;
        }

        public Dictionary<string, (long, long)[]> Rules { get; set; }
        public long[] MyTicket { get; set; }
        public long[][] NearbyTickets { get; set; }
    }
}

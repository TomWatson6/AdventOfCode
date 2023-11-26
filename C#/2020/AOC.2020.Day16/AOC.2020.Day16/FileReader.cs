using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;

namespace AOC._2020.Day16
{
    public class FileReader
    {
        public TicketInfo Read(string path)
        {
            var input = File.ReadAllText(path);

            var splitInput = input.Split("\r\n\r\n");

            var depInfo = splitInput[0].Split(Environment.NewLine);
            var myTicket = splitInput[1].Split(Environment.NewLine)[1].Split(",").Select(x => long.Parse(x)).ToArray();
            var nearbyTickets = splitInput[2].Split(Environment.NewLine)[1..].Select(x => x.Split(",").Select(y => long.Parse(y)).ToArray()).ToArray();

            var departureInfo = depInfo.ToDictionary(x => x.Split(": ")[0],
                x => x.Split(": ")[1].Split(" or ").Select(y => (long.Parse(y.Split("-")[0]), long.Parse(y.Split("-")[1]))).ToArray());

            var ticketInfo = new TicketInfo(departureInfo, myTicket, nearbyTickets);

            return ticketInfo;
        }
    }
}

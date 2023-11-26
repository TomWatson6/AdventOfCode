using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Numerics;
using System.Runtime.CompilerServices;
using System.Text;

namespace AOC._2020.Day19
{
    public class FileReader
    {
        public Dictionary<long, HashSet<string>> ReadTree(string path)
        {
            var input = File.ReadAllText(path);

            var lines = input.Split("\r\n\r\n")[0].Split(Environment.NewLine);

            var splitInput = lines.Select(x => x.Split(": "));

            var treePointers = splitInput.Where(x => !x[1].StartsWith("\""));
            var treeLiterals = splitInput.Where(x => x[1].StartsWith("\""));

            var treePointerDictionary = new Dictionary<long, long[][]>();

            foreach (var pointer in treePointers)
            {
                var indexes = pointer[1].Split(" | ").Select(x => x.Split(" ").Select(x => long.Parse(x)).ToArray()).ToArray();

                treePointerDictionary.Add(long.Parse(pointer[0]), indexes);
            }

            var treeLiteralDictionary = treeLiterals.ToDictionary(x => long.Parse(x[0]), x => new HashSet<string> { x[1].Trim('"') });

            while (treePointerDictionary.Where(x => !treeLiteralDictionary.ContainsKey(x.Key)).Count() != 0)
            {
                var compatibleBranches = treePointerDictionary.Where(x => x.Value.Any(y => y.All(z => treeLiteralDictionary.ContainsKey(z))));
                var toAdd = new Dictionary<long, HashSet<string>>();

                foreach (var branch in compatibleBranches)
                {
                    foreach (var possibility in branch.Value)
                    {
                        if (possibility.All(x => treeLiteralDictionary.ContainsKey(x)))
                        {
                            var sb = new StringBuilder();

                            foreach (var index in possibility)
                            {
                                foreach(var item in treeLiteralDictionary[index])
                                    sb.Append(item);
                            }

                            if (toAdd.ContainsKey(branch.Key))
                                toAdd[branch.Key].Add(sb.ToString());
                            else
                                toAdd.Add(branch.Key, new HashSet<string> { sb.ToString() });
                        }
                    }
                }

                foreach(var kvp in toAdd)
                {
                    if(treeLiteralDictionary.ContainsKey(kvp.Key))
                    {
                        foreach (var item in kvp.Value)
                            treeLiteralDictionary[kvp.Key].Add(item);
                    }
                    else
                    {
                        treeLiteralDictionary.Add(kvp.Key, kvp.Value);
                    }
                }
            }

            return treeLiteralDictionary;
        }

        private HashSet<string> GetPossibilities(Dictionary<long, HashSet<string>> treeLiteralDictionary, KeyValuePair<long, long[][]> branch)
        {
            var toAdd = new Dictionary<long, HashSet<string>>();

            foreach (var possibility in branch.Value)
            {
                if (possibility.All(x => treeLiteralDictionary.ContainsKey(x)))
                {
                    var sb = new StringBuilder();

                    foreach (var index in possibility)
                    {
                        foreach (var item in treeLiteralDictionary[index])
                            sb.Append(item);
                    }

                    if (toAdd.ContainsKey(branch.Key))
                        toAdd[branch.Key].Add(sb.ToString());
                    else
                        toAdd.Add(branch.Key, new HashSet<string> { sb.ToString() });
                }
            }
        }
    }
}

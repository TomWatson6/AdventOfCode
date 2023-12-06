#![allow(unused)]

use std::io::{self, Read};
use std::vec;
use std::io::{Write, BufReader, BufRead, ErrorKind};
use std::fs::File;
use std::cmp::Ordering;
use std::collections::{HashMap, HashSet};
use std::time::Instant;

fn read_file(file_name: &str) -> String {
    let mut file = File::open(file_name).unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    contents
}

#[derive(Debug)]
struct Entry {
    dest: usize,
    source: usize,
    range: usize,
}

fn map_seeds(mut seeds: &mut Vec<(usize, usize)>, map: &Vec<Entry>) -> Vec<(usize, usize)> {
    let mut mapped: Vec<(usize, usize)> = Vec::new();

    while let Some((lower, upper)) = seeds.pop() {
        let mut in_range = false;

        for entry in map {
            let overlap_lower = lower.max(entry.source);
            let overlap_upper = upper.min(entry.source + entry.range);

            if overlap_lower < overlap_upper {
                in_range = true;

                mapped.push((overlap_lower - entry.source + entry.dest, overlap_upper - entry.source + entry.dest));
                
                if overlap_lower > lower {
                    seeds.push((lower, overlap_lower));
                }

                if upper > overlap_upper {
                    seeds.push((overlap_upper, upper));
                }

                break;
            }
        }

        if !in_range {
            mapped.push((lower, upper));
        }
    }

    mapped
}

fn lowest_location(mut pairs: Vec<(usize, usize)>, maps: &Vec<Vec<Entry>>) -> usize {
    for map in maps {
        pairs = map_seeds(&mut pairs, map);
    }

    pairs.iter().map(|x| x.0).min().unwrap_or(0)
}

fn main() {
    let start = Instant::now();

    let input = read_file("input.txt");

    let chunks: Vec<&str> = input.split("\n\n").collect();
    let mut seeds: Vec<usize> = chunks.first().unwrap().split(' ').filter_map(|x| x.parse().ok()).collect();
    let mut maps: Vec<Vec<Entry>> = Vec::new();

    for chunk in chunks.iter().skip(1) {
        let mut map: Vec<Entry> = Vec::new();

        for line in chunk.lines().skip(1) {
            let parts: Vec<usize> = line.split(' ').filter_map(|x| x.parse().ok()).collect();

            map.push(Entry{dest: parts[0], source: parts[1], range: parts[2]});
        }

        maps.push(map);
    }

    let mut pairs: Vec<(usize, usize)> = seeds.iter().map(|x| (*x, *x + 1)).collect();
    let lowest = lowest_location(pairs, &maps);
    
    println!("Part 1: {}", lowest);

    let mut pairs: Vec<(usize, usize)> = seeds.chunks(2).map(|x| (x[0], x[0] + x[1])).collect();
    let lowest = lowest_location(pairs, &maps);

    println!("Part 2: {}", lowest);

    let duration = start.elapsed();
    println!("Execution Time: {:?}", duration);
}


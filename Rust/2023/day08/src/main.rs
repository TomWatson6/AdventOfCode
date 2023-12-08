#![allow(unused)]

use std::io::{self, Read};
use std::vec;
use std::io::{Write, BufReader, BufRead, ErrorKind};
use std::fs::File;
use std::cmp::Ordering;
use std::collections::{HashMap, HashSet};

fn read_file(file_name: &str) -> String {
    let mut file = File::open(file_name).unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    contents
}

fn gcd(mut a: usize, mut b: usize) -> usize {
    while b != 0 {
        (a, b) = (b, a % b);
    }

    a
}

fn lcm(mut a: usize, mut b: usize) -> usize {
    (a * b) / gcd(a, b)
}

fn main() {
    let input = read_file("input.txt");
    let mut lines = input.lines();

    let instructions: Vec<char> = lines.next().unwrap().chars().collect();
    let mut map: HashMap<&str, (&str, &str)> = HashMap::new();

    for line in lines.skip(1) {
        let (start, finish) = line.split_once(" = ").unwrap();
        let dirs: Vec<&str> = finish.split(", ").map(|x| x.trim_matches(|c| c == '(' || c == ')').trim()).collect();
        let (left, right) = (dirs[0], dirs[1]);

        map.insert(start, (left, right));
    }

    let mut pos = "AAA";
    let mut count = 0;

    loop {
        let i = instructions[count % instructions.len()];

        match i {
            'L' => pos = map[pos].0,
            'R' => pos = map[pos].1,
            _ => panic!("Invalid char for direction: {}", i),
        }

        count += 1;

        if pos == "ZZZ" {
            break
        }
    }

    println!("Part 1: {}", count);

    let starts: Vec<&str> = map.keys().filter(|x| x.ends_with('A')).map(|x| *x).collect();
    let mut positions: Vec<&str> = starts.clone();
    let mut occurrences: HashMap<&str, (usize, usize)> = HashMap::new();

    for x in 0..positions.len() {
        let mut count = 0;
        let mut seen: HashMap<&str, usize> = HashMap::new();

        loop {
            let i = instructions[count % instructions.len()];

            match i {
                'L' => positions[x] = map[positions[x]].0,
                'R' => positions[x] = map[positions[x]].1,
                _ => panic!("Invalid char for direction: {}", i),
            }

            count += 1;

            if positions[x].ends_with('Z') && seen.contains_key(positions[x]) {
                *occurrences.entry(starts[x]).or_insert((0, 0)) = (count, count - seen[positions[x]]);
                break;
            }

            *seen.entry(positions[x]).or_insert(0) = count;
        }
    }

    let mut mult = 1;

    for o in occurrences.values() {
        mult = lcm(mult, o.1);
    }

    println!("Part 2: {}", mult);
}


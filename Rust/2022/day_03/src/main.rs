#![allow(unused)]

use std::io::{self, Read};
use std::vec;
use std::io::{Write, BufReader, BufRead, ErrorKind};
use std::fs::File;
use std::cmp::Ordering;
use std::collections::HashMap;

fn read_file(file_name: &str) -> String {
    let mut file = File::open(file_name).unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    contents
}

fn calculate(mut total: u32, c: u32) -> u32 {
    if c >= 97 {
        total += c - 96
    } else if c >= 65 {
        total += c - 38
    } else {
        assert!(false);
    }

    total
}

fn part1(input: String) {
    let mut total = 0;

    for line in input.lines() {
        if line == "" {
            continue;
        }

        let mut mutual_chars = vec![];
        let left = line[..line.len() / 2].chars();
        let right = line[line.len() / 2..].chars();

        for l in left {
            for r in right.clone() {
                if l == r {
                    mutual_chars.push(l);
                }
            }
        }

        mutual_chars.dedup();

        assert!(mutual_chars.len() == 1);

        let c = mutual_chars[0] as u32;

        total = calculate(total, c)
    }

    println!("Part 1: {}", total)
}

fn part2(input: String) {
    let lines: Vec<&str> = input.lines().collect();

    let mut count = 0;
    let mut total = 0;

    while count < lines.len() {
        let mut seen: HashMap<char, u32> = HashMap::new();

        for line in lines[count..count+3].iter() {
            let mut seen_in_line: HashMap<char, u32> = HashMap::new();

            for c in line.chars() {
                seen_in_line.insert(c, 1);
            }

            for (k, v) in seen_in_line.iter() {
                if let Some(x) = seen.get(k) {
                    seen.insert(*k, x + 1);
                } else {
                    seen.insert(*k, 1);
                }
            }
        }

        for (k, v) in seen.iter() {
            if *v == 3 {
                total = calculate(total, *k as u32);
            }
        }

        count += 3;
    }

    println!("Part 2: {}", total)
}

fn main() {
    let input = read_file("input.txt");

    part1(input.clone());
    part2(input);
}


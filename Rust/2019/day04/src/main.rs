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

fn main() {
    let input = read_file("input.txt");
    let (lower, upper) = input.split_once('-').unwrap();
    let lower = lower.parse::<usize>().unwrap();
    let upper = upper.trim().parse::<usize>().unwrap();

    let mut total = 0;
    let mut total2 = 0;

    for pass in lower..upper {
        if valid(&pass) {
            total += 1;

            if two_adjacent_only(&pass) {
                total2 += 1;
            }
        }
    }

    println!("Part 1: {}", total);
    println!("Part 2: {}", total2);
}

fn valid(pass: &usize) -> bool {
    is_six_digits(pass) && two_adjacent(pass) && increasing(pass)
}

fn is_six_digits(pass: &usize) -> bool {
    pass.to_string().len() == 6
}

fn two_adjacent(pass: &usize) -> bool {
    pass.to_string()
        .chars()
        .collect::<Vec<char>>()
        .windows(2)
        .into_iter()
        .any(|x| x[0] == x[1])
}

fn two_adjacent_only(pass: &usize) -> bool {
    let mut counts: Vec<usize> = Vec::new();

    let mut last = ' ';
    let mut count = 0;

    for c in pass.to_string().chars() {
        if c != last {
            counts.push(count);
            count = 0;
            last = c;
        }

        count += 1;
    }

    counts.push(count);

    counts.into_iter().any(|x| x == 2)
}

fn increasing(pass: &usize) -> bool {
    pass.to_string()
        .chars()
        .collect::<Vec<char>>()
        .windows(2)
        .into_iter()
        .all(|x| x[0].to_string().parse::<usize>().unwrap() <= x[1].to_string().parse::<usize>().unwrap())
}



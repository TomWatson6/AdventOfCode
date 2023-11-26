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
    let mut totals: Vec<i32> = Vec::new();
    let mut total = 0;

    for line in input.lines() {
        if line == "" {
            totals.push(total);
            total = 0;
            continue
        }

        total += line.parse::<i32>().unwrap();
    }

    totals.sort();

    println!("Part 1: {}", totals[totals.len()-1]);

    total = 0;

    for x in totals[totals.len()-3..].iter() {
        total += x;
    }

    println!("Part 2: {}", total)
}


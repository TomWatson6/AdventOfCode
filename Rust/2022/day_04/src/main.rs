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
    let mut contained = 0;
    let mut overlapping = 0;

    for line in input.lines() {
        let mut s1: HashSet<u32> = HashSet::new();
        let mut s2: HashSet<u32> = HashSet::new();

        let parts = line.split(",").collect::<Vec<&str>>();
        let left = parts[0].split("-").collect::<Vec<&str>>();
        let l1 = left[0].parse::<u32>().unwrap();
        let r1 = left[1].parse::<u32>().unwrap();

        let right = parts[1].split("-").collect::<Vec<&str>>();
        let l2 = right[0].parse::<u32>().unwrap();
        let r2 = right[1].parse::<u32>().unwrap();

        if (l1 >= l2 && r1 <= r2) || (l2 >= l1 && r2 <= r1) {
            contained += 1;
        }

        for i in l1..r1 + 1 {
            s1.insert(i);
        }

        for i in l2..r2 + 1 {
            s2.insert(i);
        }

        if s1.intersection(&s2).count() > 0 {
            overlapping += 1;
        }
    }

    println!("Part 1: {}", contained);
    println!("Part 2: {}", overlapping)
}


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

    let mut floor = 0;
    let mut p2 = false;
    let mut p2_ans = 0;

    for (i, c) in input.chars().enumerate() {
        match c {
            '(' => floor += 1,
            ')' => floor -= 1,
            _ => continue,
        }

        if floor < 0 && !p2 {
            p2_ans = i + 1;
            p2 = true;
        }
    }

    println!("Part 1: {}", floor);
    println!("Part 2: {}", p2_ans);
}


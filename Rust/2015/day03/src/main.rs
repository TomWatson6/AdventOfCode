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
    let mut visited: HashSet<(i32, i32)> = HashSet::new();
    let mut pos: (i32, i32) = (0, 0);
    visited.insert(pos);

    for c in input.chars() {
        match c {
            '<' => pos.0 -= 1,
            '>' => pos.0 += 1,
            '^' => pos.1 -= 1,
            'v' => pos.1 += 1,
            _ => continue,
        }

        visited.insert(pos);
    }

    println!("Part 1: {}", visited.len());

    visited = HashSet::new();
    visited.insert((0, 0));
    let mut santas: Vec<(i32, i32)> = vec![(0, 0), (0, 0)];
    let mut curr = 0;

    for c in input.chars() {
        match c {
            '<' => santas[curr].0 -= 1,
            '>' => santas[curr].0 += 1,
            '^' => santas[curr].1 -= 1,
            'v' => santas[curr].1 += 1,
            _ => continue,
        }

        visited.insert(santas[curr]);

        curr = (curr + 1) % 2;
    }

    println!("Part 2: {}", visited.len());
}


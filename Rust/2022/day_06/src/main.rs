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
    let chars = input.chars().collect::<Vec<char>>();

    let mut i = 0;
    let mut p1_done = false;

    while i < chars.len() - 3 {
        let mut s: HashSet<char> = HashSet::new();
        let mut s2: HashSet<char> = HashSet::new();

        for c in chars[i..i+4].iter() {
            s.insert(*c);
        }

        for c in chars[i..i+14].iter() {
            s2.insert(*c);
        }

        if s.len() > 3 && !p1_done {
            println!("Part 1: {}", i + 4);
            p1_done = true;
        }

        if s2.len() > 13 {
            println!("Part 2: {}", i + 14);
            break;
        }

        i += 1;
    }
}


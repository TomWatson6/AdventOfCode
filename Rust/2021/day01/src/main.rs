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

    let nums: Vec<usize> = input.lines().into_iter().filter_map(|x| x.parse().ok()).collect();

    let mut larger = 0;

    for i in 0..nums.len() - 1 {
        if nums[i + 1] > nums[i] {
            larger += 1;
        }
    }

    println!("Part 1: {}", larger);
    larger = 0;

    for i in 0..nums.len() - 3 {
        if nums[i] < nums[i + 3] {
            larger += 1;
        }
    }

    println!("Part 2: {}", larger);
}


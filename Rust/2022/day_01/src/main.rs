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
    
    let most = input.split("\n\n")
        .map(|x| x.lines()
            .map(|x| x.parse().unwrap())
            .collect::<Vec<usize>>()
            .iter()
            .sum::<usize>())
        .max()
        .unwrap();

    println!("Part 1: {}", most);

    let mut nums: Vec<usize> = input.split("\n\n")
        .map(|x| x.lines()
            .map(|n| n.parse().unwrap())
            .collect::<Vec<usize>>()
            .iter()
            .sum::<usize>())
        .collect();

    nums.sort();
    let top_three: usize = nums[nums.len()-3..].iter().sum();
    

    println!("Part 2: {}", top_three);
}


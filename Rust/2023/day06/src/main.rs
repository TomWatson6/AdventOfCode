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

    let mut lines = input.lines();
    let times: Vec<usize> = lines.next().unwrap().split(' ').skip(1).filter_map(|x| x.parse().ok()).collect();
    let distances: Vec<usize> = lines.next().unwrap().split(' ').skip(1).filter_map(|x| x.parse().ok()).collect();

    let mut product = 1;

    for (t, d) in times.iter().zip(&distances) {
        let mut wins = 0;

        for x in 0..*t {
            if (t - x) * x > *d {
                wins += 1;
            }
        }

        product *= wins;
    }

    println!("Part 1: {}", product);

    let time: usize = times.iter().map(|&x| x.to_string()).collect::<String>().parse().unwrap();
    let distance: usize = distances.iter().map(|&x| x.to_string()).collect::<String>().parse().unwrap();

    let mut wins = 0;

    for x in 0..time {
        if (time - x) * x > distance {
            wins += 1;
        }
    }

    println!("Part 2: {}", wins);
}


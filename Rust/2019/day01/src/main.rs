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

fn fuel_cost(fuel: i32) -> i32 {
    fuel / 3 - 2
}

fn fuel_cost2(fuel: i32) -> i32 {
    let f = fuel / 3 - 2;

    if f <= 0 {
        0
    } else {
        f + fuel_cost2(f)
    }
}

fn main() {
    let input = read_file("input.txt");
    let mut cost = 0;
    let mut cost2 = 0;

    for line in input.lines() {
        let f = line.parse::<i32>().unwrap();
        cost += fuel_cost(f);
        cost2 += fuel_cost2(f);
    }

    println!("Part 1: {}", cost);
    println!("Part 2: {}", cost2);
}


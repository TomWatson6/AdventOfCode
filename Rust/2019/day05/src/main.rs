#![allow(unused)]

use std::io::{self, Read};
use std::vec;
use std::io::{Write, BufReader, BufRead, ErrorKind};
use std::fs::File;
use std::cmp::Ordering;
use std::collections::{HashMap, HashSet};

mod intcode;
use intcode::*;

fn read_file(file_name: &str) -> String {
    let mut file = File::open(file_name).unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    contents
}

fn main() {
    let code: Vec<isize> = read_file("input.txt")
        .split(',')
        .filter_map(|x| x.trim().parse().ok())
        .collect();
    let mut computer = Computer::from((code.clone(), Vec::from([1])));
    computer.compute();

    if let Some(p1) = computer.outputs.last() {
        println!("Part 1: {}", p1);
    } else {
        println!("Answer not produced for part 1");
    }

    let mut computer = Computer::from((code, Vec::from([5])));
    computer.compute();

    if let Some(p2) = computer.outputs.last() {
        println!("Part 2: {}", p2);
    } else {
        println!("Answer not produced for part 2");
    }
}


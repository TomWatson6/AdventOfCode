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

    let bin: Vec<Vec<char>> = input.lines().into_iter().map(|x| x.chars().collect()).collect();
    let mut gamma: Vec<char> = Vec::new();
    let mut epsilon: Vec<char> = Vec::new();

    for c in 0..bin[0].len() {
        let mut zeros = 0;
        let mut ones = 0;

        for r in 0..bin.len() {
            match bin[r][c] {
                '0' => zeros += 1,
                '1' => ones += 1,
                _ => panic!("Invalid bit: {}", r),
            }
        }

        if ones > zeros {
            gamma.push('1');
            epsilon.push('0');
            continue
        }

        gamma.push('0');
        epsilon.push('1');
    }

    let gamma: String = gamma.into_iter().collect();
    let epsilon: String = epsilon.into_iter().collect();

    let gamma: isize = isize::from_str_radix(gamma.as_str(), 2).unwrap();
    let epsilon: isize = isize::from_str_radix(epsilon.as_str(), 2).unwrap();

    println!("Part 1: {}", gamma * epsilon);

    let mut oxygen = bin.clone();
    let mut c02 = bin.clone();
    let mut count = 0;

    while oxygen.len() > 1 {
    }
}


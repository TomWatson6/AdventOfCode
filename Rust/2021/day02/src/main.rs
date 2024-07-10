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

    let mut pos: i64 = 0;
    let mut pos2: i64 = 0;
    let mut depth: i64 = 0;
    let mut depth2: i64 = 0;
    let mut aim: i64 = 0;

    for line in input.lines() {
        let (cmd, mag) = line.split_once(' ').unwrap();
        let mag: i64 = mag.parse().unwrap();

        match cmd {
            "forward" => {
                pos += mag;
                pos2 += mag;
                depth2 += mag * aim;
            },
            "up" => {
                depth -= mag;
                aim -= mag;
            },
            "down" => {
                depth += mag;
                aim += mag;
            },
            _ => panic!("Invalid command: {}", cmd),
        }
    }

    println!("Part 1: {}", pos * depth);
    println!("Part 2: {}", pos2 * depth2);
}


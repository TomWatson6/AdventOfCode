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

fn get_next_inc(seq: &Vec<i64>) -> i64 {
    let mut diffs: Vec<i64> = Vec::new();

    for i in 0..seq.len() - 1 {
        diffs.push(seq[i + 1] - seq[i]);
    }

    if diffs.iter().all(|x| *x == diffs[0]) {
        return diffs[0];
    }

    diffs[diffs.len() - 1] + get_next_inc(&diffs)
}

fn main() {
    let input = read_file("input.txt");

    for p2 in [false, true] {
        let mut ans = 0;

        for line in input.lines() {
            let mut seq: Vec<i64> = line.split(' ').map(|x| x.parse().unwrap()).collect();

            if p2 {
                seq.reverse();
            }

            ans += seq.last().unwrap() + get_next_inc(&seq);
        }

        println!("Part {}: {}", if p2 { 2 } else { 1 }, ans);
    }
}


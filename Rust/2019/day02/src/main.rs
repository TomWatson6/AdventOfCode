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

    let mut instructions: Vec<usize> = Vec::new();

    for c in input.split(",").map(|x| x.trim()) {
        let n = c.parse::<usize>().unwrap();
        instructions.push(n);
    }
    
    let cached = instructions.clone();
    let output = 19690720;

    for noun in 0..100 {
        for verb in 0..100 {
            instructions = cached.clone();
            let mut ptr = 0;

            instructions[1] = noun;
            instructions[2] = verb;

            while instructions[ptr] != 99 {
                match instructions[ptr] {
                    1 => ptr += add(&mut instructions, ptr),
                    2 => ptr += mul(&mut instructions, ptr),
                    99 => break,
                    _ => panic!("Something went wrong with the program, found: {}", instructions[ptr]),
                }
            }

            if noun == 12 && verb == 2 {
                println!("Part 1: {}", instructions[0]);
            }

            if instructions[0] == output {
                println!("Part 2: {}", 100 * noun + verb);
            }
        }
    }

    

}

fn add(instructions: &mut Vec<usize>, ptr: usize) -> usize {
    let a = instructions[ptr + 1];
    let b = instructions[ptr + 2];
    let c = instructions[ptr + 3];

    instructions[c] = instructions[a] + instructions[b];

    4
}

fn mul(instructions: &mut Vec<usize>, ptr: usize) -> usize {
    let a = instructions[ptr + 1];
    let b = instructions[ptr + 2];
    let c = instructions[ptr + 3];

    instructions[c] = instructions[a] * instructions[b];

    4
}


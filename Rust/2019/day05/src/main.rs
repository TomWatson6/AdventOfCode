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

    let mut instructions: Vec<isize> = Vec::new();

    for c in input.split(',').map(|x| x.trim()) {
        let n = c.parse::<isize>().unwrap();
        instructions.push(n);
    }
    
    let cached = instructions.clone();

    let ins = [3, 0, 4, 0, 99];
    let mut c = Computer::new(ins.to_vec(), 45);
    println!("Output: {}", c.compute());
}

#[derive(Debug)]
struct Computer {
    instructions: Vec<isize>,
    input_value: isize,
    output_value: isize,
    ptr: isize,
}

impl Computer {
    fn new(instructions: Vec<isize>, input_value: isize) -> Computer {
        Computer{instructions, input_value, output_value: 0, ptr: 0}
    }

    fn compute(&mut self) -> isize {
        loop {
            match self.instructions[self.ptr as usize] {
                1 => self.add(),
                2 => self.mul(),
                3 => self.input(),
                4 => self.output(),
                99 => return self.output_value,
                _ => panic!("opcode has not yet been implemented"),
            };
        }
    }

    fn get_values(self, num_params: usize) -> Vec<isize> {
        let mut values: Vec<isize> = Vec::new();
        let opcode: Vec<char> = self.instructions[self.ptr as usize].to_string().chars().rev().collect();

        for _ in 0..num_params.min(opcode.len()) {
        }

        values
    }

    fn add(&mut self) {
        let a = self.instructions[(self.ptr + 1) as usize] as usize;
        let b = self.instructions[(self.ptr + 2) as usize] as usize;
        let c = self.instructions[(self.ptr + 3) as usize] as usize;

        self.instructions[c] = self.instructions[a] + self.instructions[b];
        self.ptr += 4;
    }

    fn mul(&mut self) {
        let a = self.instructions[(self.ptr + 1) as usize] as usize;
        let b = self.instructions[(self.ptr + 2) as usize] as usize;
        let c = self.instructions[(self.ptr + 3) as usize] as usize;

        self.instructions[c] = self.instructions[a] * self.instructions[b];
        self.ptr += 4;
    }

    fn input(&mut self) {
        let pos = self.instructions[(self.ptr + 1) as usize] as usize;

        self.instructions[pos] = self.input_value;
        self.ptr += 2;
    }

    fn output(&mut self) {
        let ptr = self.instructions[(self.ptr + 1) as usize];
        self.output_value = self.instructions[ptr as usize];
        self.ptr += 2;
    }
}



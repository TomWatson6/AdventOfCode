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

fn run(a: i64, instructions: &Vec<Vec<&str>>) -> i64 {
    let mut registers: HashMap<char, i64> = HashMap::new();
    let mut i = 0;
    let mut mult = 0;

    fn get(x: &str, registers: &HashMap<char, i64>) -> i64 {
        return match x.parse() {
            Ok(x) => x,
            Err(_) => **registers.get(&x.chars().nth(0).unwrap()).get_or_insert(&0i64),
        }
    }

    while i < instructions.len() {
        let parts = instructions[i];

        match parts[0] {
            "set" => registers[&parts[1].chars().nth(0).unwrap()] = get(parts[2], &registers),
            "sub" => registers[&parts[1].chars().nth(0).unwrap()] -= get(parts[2], &registers),
            "mul" => registers[&parts[1].chars().nth(0).unwrap()] *= get(parts[2], &registers),
            "jnz" => {
                let val = registers.get(&parts[1].chars().nth(0).unwrap()).get_or_insert(&0i64);
                if **val != 0 {
                    i += get(parts[2])
                }
            },
            _ => panic!("OH NO!"),
        }
    }

    mult
}

fn main() {
    let input = read_file("input.txt");

    let instructions = input.lines().map(|x| x.split(' ').collect::<Vec<_>>()).collect::<Vec<_>>();


}


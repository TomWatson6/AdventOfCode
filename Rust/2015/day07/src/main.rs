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

fn get_value(operations: HashMap<String, String>, item: String, memo: &mut HashMap<String, u16>) -> u16 {
    if let Some(x) = memo.get(&item) {
        return *x;
    }

    let mut output: u16 = 0;
    let mut vals: Vec<&str>;

    match operations.get(&item) {
        Some(x) => vals = x.split(' ').collect(),
        None => return item.parse::<u16>().unwrap(),
    }

    match vals.len() {
        1 => output = get_value(operations.clone(), vals[0].to_string(), memo),
        2 => match vals[1].parse::<u16>() {
            Ok(x) => output = !x,
            Err(_) => output = !get_value(operations.clone(), vals[1].to_string(), memo),
        },
        3 => {
            match vals[1] {
                "AND" => output = get_value(operations.clone(), vals[0].to_string(), memo) & get_value(operations.clone(), vals[2].to_string(), memo),
                "OR" => output = get_value(operations.clone(), vals[0].to_string(), memo) | get_value(operations.clone(), vals[2].to_string(), memo),
                "LSHIFT" => output = get_value(operations.clone(), vals[0].to_string(), memo) << get_value(operations.clone(), vals[2].to_string(), memo),
                "RSHIFT" => output = get_value(operations.clone(), vals[0].to_string(), memo) >> get_value(operations.clone(), vals[2].to_string(), memo),
                _ => output = 0,
            }
        },
        _ => output = 0,
    };

    *memo.entry(item).or_insert(0) = output;

    output
}

fn main() {
    let input = read_file("input.txt");
    let mut operations: HashMap<String, String> = HashMap::new();

    for line in input.lines() {
        let parts = line.split(" -> ").map(|x| x.trim()).collect::<Vec<&str>>();
        assert!(parts.len() == 2);

        operations.insert(parts[1].to_string(), parts[0].to_string());
    }

    let mut memo: HashMap<String, u16> = HashMap::new();

    let v = get_value(operations.clone(), String::from("a"), &mut memo);

    println!("Part 1: {}", v);

    *operations.entry(String::from("b")).or_insert(String::from("0")) = format!("{}", v).to_string();

    let mut memo: HashMap<String, u16> = HashMap::new();

    let v = get_value(operations.clone(), String::from("a"), &mut memo);

    println!("Part 2: {}", v);
}

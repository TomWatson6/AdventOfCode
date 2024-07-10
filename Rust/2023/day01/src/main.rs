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

fn convert(mappings: &Vec<(&str, &str)>, s: String) -> String {
    let mut output = s;

    for (text, rep) in mappings {
        let replacement = format!("{}{}{}", text.chars().next().unwrap(), rep, text.chars().nth(text.len() - 1).unwrap());
        output = output.replace(text, &replacement);
    }

    output.to_string()
}

fn count_numbers(p2: bool) -> i32 {
    let mappings = vec![
        ("one", "1"),
        ("two", "2"),
        ("three", "3"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9"),
    ];

    let input = read_file("input.txt");
    let mut total = 0;

    for mut line in input.lines() {
        if p2 {
            total += assemble_number(convert(&mappings, line.to_string()).as_str());
            continue;
        }

        total += assemble_number(line);
    }

    total
}

fn assemble_number(line: &str) -> i32 {
    let mut nums: Vec<i32> = Vec::new();

    for c in line.chars() {
        match c.to_string().parse::<i32>() {
            Ok(x) => nums.push(x),
            Err(_) => continue,
        }
    }

    let combined = format!("{}{}", nums[0], nums[nums.len()-1]);
    combined.parse::<i32>().unwrap()
}

fn main() {
    println!("Part 1: {}", count_numbers(false));
    println!("Part 2: {}", count_numbers(true));
}


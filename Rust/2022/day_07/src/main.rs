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
    let mut directories: Vec<String> = Vec::new();
    let mut sizes: HashMap<String, i64> = HashMap::new();

    for line in input.lines() {
        let parts = line.split(" ").collect::<Vec<&str>>();

        match parts[0] {
            "$" => match parts[1] {
                "cd" => match parts[2] {
                    ".." => {
                        directories.pop().unwrap();
                    },
                    _ => {
                        let mut name = directories.join("/");
                        name.push_str("/");
                        name.push_str(parts[2]);
                        directories.push(name);
                    },
                },
                "ls" => continue,
                _ => panic!("Unrecognised command: {}", parts[1])
            },
            "dir" => continue,
            _ => {
                let size = parts[0].parse::<i64>().unwrap();
                let curr = directories.last().unwrap();

                for dir in directories.iter() {
                    match sizes.get(dir) {
                        Some(x) => sizes.insert(dir.clone(), x + size),
                        None => sizes.insert(curr.clone(), size),
                    };
                }
            },
        }

        // println!("Line: {}, Directories: {:?}, Sizes: {:?}", line, directories, sizes);
    }

    let mut total = 0;

    for (_, v) in sizes.iter() {
        if *v <= 100_000 {
            total += *v;
        }
    }

    // println!("{:?}", sizes);

    println!("Part 1: {}", total)
}


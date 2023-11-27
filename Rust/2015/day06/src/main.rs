#![allow(unused)]

use std::hash::Hash;
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

    let mut lights: HashMap<(i32, i32), bool> = HashMap::new();
    let mut brightness: HashMap<(i32, i32), i32> = HashMap::new();

    for line in input.lines() {
        let parts = line.split(' ').collect::<Vec<&str>>();

        match parts[0] {
            "turn" => {
                let from = parts[2].split(',').map(|p| p.parse::<i32>().unwrap()).collect::<Vec<i32>>();
                let to = parts[4].split(',').map(|p| p.parse::<i32>().unwrap()).collect::<Vec<i32>>();

                for i in from[0]..to[0] + 1 {
                    for j in from[1]..to[1] + 1 {
                        match parts[1] {
                            "on" => {
                                *lights.entry((i, j)).or_insert(false) = true;
                                *brightness.entry((i, j)).or_insert(0) += 1;
                            },
                            "off" => {
                                *lights.entry((i, j)).or_insert(false) = false;
                                let entry = brightness.entry((i, j)).or_insert(0);
                                if *entry == 0 {
                                    continue
                                }
                                *entry -= 1;
                            },
                            _ => continue,
                        }
                    }
                }
            },
            "toggle" => {
                let from = parts[1].split(',').map(|p| p.parse::<i32>().unwrap()).collect::<Vec<i32>>();
                let to = parts[3].split(',').map(|p| p.parse::<i32>().unwrap()).collect::<Vec<i32>>();

                for i in from[0]..to[0] + 1 {
                    for j in from[1]..to[1] + 1 {
                        let entry = lights.entry((i, j)).or_insert(false);
                        *entry = !*entry;

                        *brightness.entry((i, j)).or_insert(0) += 2;
                    }
                }
            },
            _ => continue,
        }
    }

    let lights_on = lights.values().filter(|x| **x).count();
    let brightness_level = brightness.values().sum::<i32>();

    println!("Part 1: {}", lights_on);
    println!("Part 2: {}", brightness_level);
}


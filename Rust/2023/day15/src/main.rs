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
    contents.trim().to_string()
}

fn hash(s: &str) -> usize {
    let mut val = 0;

    for c in s.chars() {
        val += c as usize;
        val *= 17;
        val %= 256
    }

    val
}

fn main() {
    let input = read_file("input.txt");
    let parts: Vec<&str> = input.split(',').collect();
    let mut total = 0;
    let mut boxes: Vec<Vec<(&str, usize)>> = vec![vec![]; 256];
    let mut power = 0;

    for s in &parts {
        total += hash(s);

        if s.contains('=') {
            let (label, focal_length) = s.split_once('=').unwrap();
            let focal_length: usize = focal_length.parse().unwrap();
            let i = hash(label);
            let mut found = false;

            for (x, b) in boxes.get(i).unwrap().iter().enumerate() {
                if b.0 == label {
                    boxes[i][x] = (label, focal_length);
                    found = true;
                    break;
                }
            }

            if !found {
                boxes[i].push((label, focal_length));
            }
        }

        if s.contains('-') {
            let (label, _) = s.split_once('-').unwrap();
            let i = hash(label);
            let mut to_remove: isize = -1;

            for (j, x) in boxes[i].iter().enumerate() {
                if x.0 == label {
                    to_remove = j as isize;
                    break
                }
            }

            if to_remove != -1 {
                boxes[i].remove(to_remove as usize);
            }
        }
    }

    println!("Part 1: {}", total);

    for (i, b) in boxes.iter().enumerate() {
        for (j, lens) in b.iter().enumerate() {
            power += (i + 1) * (j + 1) * lens.1;
        }
    }

    println!("Part 2: {}", power);
}

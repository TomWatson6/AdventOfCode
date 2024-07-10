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

    let mut wires: Vec<HashSet<(isize, isize)>> = vec![HashSet::new(), HashSet::new()];
    let mut dists: Vec<HashMap<(isize, isize), usize>> = vec![HashMap::new(), HashMap::new()];

    for i in 0..2 {
        let mut pos = (0, 0);
        let mut dist = 0;

        for parts in input.lines().nth(i).unwrap().split(',').collect::<Vec<&str>>() {
            let dir = parts.to_string()[..1].to_string();
            let mag = parts.to_string()[1..].to_string().parse::<usize>().unwrap();
            let mut d = (0, 0);

            match dir.as_str() {
                "L" => d = (0, -1),
                "R" => d = (0, 1),
                "U" => d = (-1, 0),
                "D" => d = (1, 0),
                _ => panic!("Oh Nooo"),
            }

            for _ in 0..mag {
                dist += 1;
                pos = (pos.0 + d.0, pos.1 + d.1);
                wires[i].insert(pos);
                dists[i].insert(pos, dist);
            }
        }
    }
    
    let mut smallest = 9999999999;

    for w in &wires[0] {
        if wires[1].contains(&w) {
            smallest = smallest.min(dists[0].get(w).unwrap() + dists[1].get(w).unwrap());
        }
    }

    let common = wires[0].intersection(&wires[1]);

    let p1 = common.min_by_key(|x| x.0.abs() + x.1.abs()).unwrap();
    println!("Part 1: {:?}", p1.0 + p1.1);
    println!("Part 2: {}", smallest);
}


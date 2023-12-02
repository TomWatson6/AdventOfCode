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
    let req: HashMap<&str, u32> = HashMap::from(vec![
        ("red", 12),
        ("green", 13),
        ("blue", 14),
    ].iter().cloned().collect::<HashMap<_, _>>());

    let input = read_file("input.txt");

    let mut games: Vec<HashMap<&str, u32>> = Vec::new();

    for (i, line) in input.lines().map(|x| x.split(": ").collect::<Vec<&str>>()[1]).enumerate() {
        let parts = line.split("; ").collect::<Vec<&str>>();
        let mut game: HashMap<&str, u32> = HashMap::new();

        for p in parts {
            let colours = p.split(", ")
                .collect::<Vec<&str>>()
                .into_iter()
                .map(|x| x.split(' ')
                     .collect::<Vec<&str>>())
                .collect::<Vec<Vec<&str>>>();
            
            for c in colours {
                *game.entry(c[1]).or_insert(0) = c[0].parse::<u32>().unwrap().max(match game.get(c[1]) {
                    Some(x) => *x,
                    None => 0,
                });
            }
        }

        games.push(game);
    }

    let mut total = 0;
    let mut power = 0;

    for (i, game) in games.iter().enumerate() {
        power += game.values().product::<u32>();

        if game.iter().any(|(k, v)| v > req.get(k).unwrap()) { continue };

        total += i + 1;
    }

    println!("Part 1: {}", total);
    println!("Part 2: {}", power);
}


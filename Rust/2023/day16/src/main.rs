#![allow(unused)]

use std::io::{self, Read};
use std::vec;
use std::io::{Write, BufReader, BufRead, ErrorKind};
use std::fs::File;
use std::cmp::Ordering;
use std::collections::{HashMap, HashSet};
use std::collections::VecDeque;

fn read_file(file_name: &str) -> String {
    let mut file = File::open(file_name).unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    contents
}

#[derive(Eq, PartialEq, Hash, Clone, Copy, Debug)]
struct Wire {
    r: isize,
    c: isize,
    dr: isize,
    dc: isize,
}

fn next(grid: &Vec<Vec<char>>, wire: &Wire) -> Vec<Wire> {
    let mut new_wires = Vec::new();

    let rr = wire.r + wire.dr;
    let cc = wire.c + wire.dc;

    if rr < 0 || rr as usize >= grid.len() || cc < 0 || cc as usize >= grid[0].len() {
        return new_wires;
    }

    match (grid[rr as usize][cc as usize], wire.dr, wire.dc) {
        ('.', _, _) => new_wires.push(Wire{r: rr, c: cc, dr: wire.dr, dc: wire.dc}),
        ('|', _, -1 | 1) => {
            new_wires.push(Wire{r: rr, c: cc, dr: -1, dc: 0});
            new_wires.push(Wire{r: rr, c: cc, dr: 1, dc: 0});
        },
        ('-', -1 | 1, _) => {
            new_wires.push(Wire{r: rr, c: cc, dr: 0, dc: -1});
            new_wires.push(Wire{r: rr, c: cc, dr: 0, dc: 1});
        },
        ('|', -1 | 1, _) => new_wires.push(Wire{r: rr, c: cc, dr: wire.dr, dc: wire.dc}),
        ('-', _, -1 | 1) => new_wires.push(Wire{r: rr, c: cc, dr: wire.dr, dc: wire.dc}),
        ('/', -1, 0) => new_wires.push(Wire{r: rr, c: cc, dr: 0, dc: 1}),
        ('/', 1, 0) => new_wires.push(Wire{r: rr, c: cc, dr: 0, dc: -1}),
        ('/', 0, -1) => new_wires.push(Wire{r: rr, c: cc, dr: 1, dc: 0}),
        ('/', 0, 1) => new_wires.push(Wire{r: rr, c: cc, dr: -1, dc: 0}),
        ('\\', -1, 0) => new_wires.push(Wire{r: rr, c: cc, dr: 0, dc: -1}),
        ('\\', 1, 0) => new_wires.push(Wire{r: rr, c: cc, dr: 0, dc: 1}),
        ('\\', 0, -1) => new_wires.push(Wire{r: rr, c: cc, dr: -1, dc: 0}),
        ('\\', 0, 1) => new_wires.push(Wire{r: rr, c: cc, dr: 1, dc: 0}),
        (_, _, _) => {},
    }

    new_wires
}

fn generate(grid: &Vec<Vec<char>>, r: isize, c: isize, dr: isize, dc: isize) -> usize {
    let mut seen: HashSet<Wire> = HashSet::new();
    let wire = Wire{r, c, dr, dc};
    let mut wires: VecDeque<Wire> = VecDeque::new();
    wires.push_back(wire);

    while !wires.is_empty() {
        let wire = wires.pop_front().unwrap();
        
        if seen.contains(&wire) {
            continue;
        }

        seen.insert(wire);

        let new_wires = next(&grid, &wire);

        for w in new_wires {
            wires.push_back(w);
        }
    }

    let mut seen_pos: HashSet<(isize, isize)> = HashSet::new();
    for s in seen {
        seen_pos.insert((s.r, s.c));
    }

    seen_pos.len() - 1
}

fn main() {
    let input = read_file("input.txt");
    let grid = input.lines().map(|line| line.chars().collect::<Vec<_>>()).collect::<Vec<_>>();
    let p1 = generate(&grid, 0, -1, 0, 1);
    println!("Part 1: {}", p1);

    let mut largest = 0;

    for r in 0..grid.len() {
        largest = largest.max(generate(&grid, r as isize, -1, 0, 1));
        largest = largest.max(generate(&grid, r as isize, grid[0].len() as isize, 0, -1));
    }

    for c in 0..grid[0].len() {
        largest = largest.max(generate(&grid, -1, c as isize, 1, 0));
        largest = largest.max(generate(&grid, grid.len() as isize, c as isize, -1, 0));
    }

    println!("Part 2: {}", largest);
}


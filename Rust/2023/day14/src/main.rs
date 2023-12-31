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

fn score(grid: &Vec<Vec<char>>) -> usize {
    let mut score = 0;

    for (r, row) in grid.iter().enumerate() {
        for (c, ch) in row.iter().enumerate() {
            if *ch == 'O' {
                score += grid.len() - r;
            }
        }
    }

    score
}

fn tilt(grid: &mut Vec<Vec<char>>) {
    for r in 0..grid.len() {
        for c in 0..grid[0].len() {
            if grid[r][c] == '#' || grid[r][c] == 'O' {
                continue
            }

            let mut t = r.clone();

            while t < grid.len() {
                if grid[t][c] == 'O' || grid[t][c] == '#' {
                    if grid[t][c] == '#' {
                        break;
                    }

                    grid[r][c] = 'O';
                    grid[t][c] = '.';
                    break
                }

                t += 1
            }
        }
    }
}

fn rotate(grid: &Vec<Vec<char>>) -> Vec<Vec<char>> {
    let mut new_grid: Vec<Vec<char>> = Vec::new();

    for c in 0..grid[0].len() {
        let mut row: Vec<char> = Vec::new();

        for r in (0..grid.len()).rev() {
            row.push(grid[r][c]);
        }

        new_grid.push(row);
    }

    new_grid
}

fn cycle(mut grid: Vec<Vec<char>>) -> Vec<Vec<char>> {
    for _ in 0..4 {
        tilt(&mut grid);
        grid = rotate(&mut grid);
    }

    grid
}

fn hashable(grid: &Vec<Vec<char>>) -> String {
    grid.into_iter().map(|x| x.into_iter().collect::<String>()).collect()
}

fn main() {
    let input = read_file("input.txt");

    let mut grid: Vec<Vec<char>> = input.lines().into_iter().map(|x| x.chars().collect::<Vec<char>>()).collect();
    let cached = grid.clone();

    tilt(&mut grid);

    let s = score(&grid);

    println!("Part 1: {}", s);

    grid = cached;

    let mut i = 0;
    let iters = 1000000000;
    let mut seen: HashMap<String, usize> = HashMap::new();
    let mut cycled = false;

    while i < iters {
        grid = cycle(grid);
        let t = hashable(&grid);

        if let Some(x) = seen.get(&t) {
            if !cycled {
                let cycle_length = i - x;
                let rem_cycles = iters - i - 1;
                let num_cycles = rem_cycles / cycle_length;
                i += num_cycles * cycle_length;
                cycled = true;
            }
        }

        seen.insert(t, i);
        i += 1;
    }

    let s = score(&grid);

    println!("Part 2: {}", s);
}


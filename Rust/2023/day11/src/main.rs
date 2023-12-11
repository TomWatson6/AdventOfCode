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

fn solve(grid: &Vec<Vec<char>>, p2: bool) -> usize {
    let mut galaxies: Vec<(usize, usize)> = Vec::new();
    let mut empty_rows: Vec<usize> = Vec::new();
    let mut empty_cols: Vec<usize> = Vec::new();

    for (r, row) in grid.iter().enumerate() {
        let mut is_empty = true;

        for (c, ch) in row.iter().enumerate() {
            if *ch == '#' {
                galaxies.push((r, c));
                is_empty = false;
            }
        }

        if is_empty {
            empty_rows.push(r);
        }
    }

    for c in 0..grid[0].len() {
        let mut is_empty = true;

        for r in 0..grid.len() {
            if grid[r][c] != '.' {
                is_empty = false;
                break
            }
        }

        if is_empty {
            empty_cols.push(c);
        }
    }

    let mut total = 0;
    let mut age = if p2 { 1000000 } else { 2 };
    
    for i in 0..galaxies.len() - 1 {
        for j in i..galaxies.len() {
            let a = galaxies[i];
            let b = galaxies[j];

            let dr = empty_rows.iter().filter(|x| (**x > a.0 && **x < b.0) || (**x > b.0 && **x < a.0));
            let dc = empty_cols.iter().filter(|x| (**x > a.1 && **x < b.1) || (**x > b.1 && **x < a.1));

            let r_diff = if a.0 > b.0 { a.0 - b.0 } else { b.0 - a.0 };
            let c_diff = if a.1 > b.1 { a.1 - b.1 } else { b.1 - a.1 };

            total += r_diff + (dr.count() * (age - 1)) + c_diff + (dc.count() * (age - 1));
        }
    }

    total
}

fn main() {
    let input = read_file("input.txt");

    let grid = input.lines().into_iter().map(|x| x.chars().collect::<Vec<char>>()).collect();

    println!("Part 1: {}", solve(&grid, false));
    println!("Part 2: {}", solve(&grid, true));
}


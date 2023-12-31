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

struct Grid {
    points: Vec<Vec<char>>,
    width: usize,
    height: usize,
}

impl Grid {
    fn new(lines: Vec<&str>) -> Self {
        let mut points = Vec::new();
        let height = lines.len();
        let width = lines[0].len();

        for line in lines {
            points.push(line.chars().collect::<Vec<char>>());
        }

        Self { points, width, height }
    }

    fn row_reflection_diff(&self, row: usize) -> usize {
        let mut diff = 0;

        for c in 0..self.width {
            let mut top: i64 = row as i64;
            let mut bottom: i64 = (row + 1) as i64;

            while top >= 0 && bottom < self.height as i64 {
                if self.points[top as usize][c] != self.points[bottom as usize][c] {
                    diff += 1;
                }

                top -= 1;
                bottom += 1;
            }
        }

        diff
    }

    fn col_reflection_diff(&self, col: usize) -> usize {
        let mut diff = 0;

        for r in 0..self.height {
            let mut left: i64 = col as i64;
            let mut right: i64 = (col + 1) as i64;

            while left >= 0 && right < self.width as i64 {
                if self.points[r][left as usize] != self.points[r][right as usize] {
                    diff += 1;
                }

                left -= 1;
                right += 1;
            }
        }

        diff
    }
}

fn main() {
    let input = read_file("input.txt");

    let chunks: Vec<&str> = input.split("\n\n").collect();

    let mut rows = 0;
    let mut cols = 0;
    let mut rows2 = 0;
    let mut cols2 = 0;

    for chunk in chunks {
        let grid = Grid::new(chunk.lines().collect());

        for r in 0..grid.height - 1 {
            let row_reflection_diff = grid.row_reflection_diff(r);
            if row_reflection_diff == 0 {
                rows += r + 1;
            }
            if row_reflection_diff == 1 {
                rows2 += r + 1;
            }
        }

        for c in 0..grid.width - 1 {
            let col_reflection_diff = grid.col_reflection_diff(c);
            if col_reflection_diff == 0 {
                cols += c + 1;
            }
            if col_reflection_diff == 1 {
                cols2 += c + 1;
            }
        }
    }

    println!("Part 1: {}", rows * 100 + cols);
    println!("Part 2: {}", rows2 * 100 + cols2);
}


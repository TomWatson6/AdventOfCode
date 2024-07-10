#![allow(unused)]

use std::io::{self, Read};
use std::vec;
use std::io::{Write, BufReader, BufRead, ErrorKind};
use std::fs::File;
use std::cmp::Ordering;
use std::collections::{HashMap, HashSet, VecDeque, BinaryHeap};

fn read_file(file_name: &str) -> String {
    let mut file = File::open(file_name).unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    contents
}

#[derive(Eq, PartialEq, Clone, Copy, Debug, Ord, PartialOrd)]
struct Move {
    cost: usize,
    r: isize,
    c: isize,
    dist: isize,
    length: usize,
}

fn dijkstra(grid: Vec<Vec<usize>>, start: (usize, usize), dest: (usize, usize)) -> usize {
    let mut queue: BinaryHeap<Move> = BinaryHeap::new();
    queue.push(Move{cost: 0, r: 0, c: 0, dist: -1, length: 0});
    let mut seen: HashMap<(isize, isize, isize, usize), usize> = HashMap::new();

    while !queue.is_empty() {
        let m = queue.pop().unwrap();

        if seen.contains_key(&(m.r, m.c, m.dist, m.length)) {
            continue;
        }

        seen.insert((m.r, m.c, m.dist, m.length), m.cost);

        for (nd, (dr, dc)) in [(0, 1), (1, 0), (0, -1), (-1, 0)].iter().enumerate() {
            let rr = m.r + dr;
            let cc = m.c + dc;
            let new_l = if nd != m.dist as usize { 1 } else { m.length + 1 };

            if rr >= 0 && (rr as usize) < grid.len() && cc >= 0 && (cc as usize) < grid.first().unwrap().len() {
                let rr = rr as usize;
                let cc = cc as usize;

                if new_l <= 3 && ((nd + 2) % 4 != m.dist as usize) {
                    queue.push(Move{cost: m.cost + grid[rr][cc], r: rr as isize, c: cc as isize, dist: nd as isize, length: new_l});
                }
            }
        }
    }

    let mut ans = 999999999;

    for (k, v) in seen.iter() {
        if (k.0 as usize, k.1 as usize) == dest && *v < ans {
            ans = *v;
        }
    }

    ans
}

// To Implement
fn dijkstra2(grid: Vec<Vec<usize>>, start: (usize, usize), dest: (usize, usize)) -> usize {
    let mut queue: BinaryHeap<Move> = BinaryHeap::new();
    queue.push(Move{cost: 0, r: 0, c: 0, dist: -1, length: 0});
    let mut seen: HashMap<(isize, isize, isize, usize), usize> = HashMap::new();

    while !queue.is_empty() {
        let m = queue.pop().unwrap();

        if seen.contains_key(&(m.r, m.c, m.dist, m.length)) {
            continue;
        }

        seen.insert((m.r, m.c, m.dist, m.length), m.cost);

        for (nd, (dr, dc)) in [(0, 1), (1, 0), (0, -1), (-1, 0)].iter().enumerate() {
            let rr = m.r + dr;
            let cc = m.c + dc;
            let new_l = if nd != m.dist as usize { 1 } else { m.length + 1 };

            if rr >= 0 && (rr as usize) < grid.len() && cc >= 0 && (cc as usize) < grid.first().unwrap().len() {
                let rr = rr as usize;
                let cc = cc as usize;

                if new_l <= 3 && ((nd + 2) % 4 != m.dist as usize) {
                    queue.push(Move{cost: m.cost + grid[rr][cc], r: rr as isize, c: cc as isize, dist: nd as isize, length: new_l});
                }
            }
        }
    }

    let mut ans = 999999999;

    for (k, v) in seen.iter() {
        if (k.0 as usize, k.1 as usize) == dest && *v < ans {
            ans = *v;
        }
    }

    ans
}

fn main() {
    let input = read_file("input.txt");
    let grid: Vec<Vec<usize>> = input
        .lines()
        .map(|x| x
             .chars()
             .map(|c| c
                  .to_string()
                  .parse()
                  .unwrap())
             .collect::<Vec<usize>>())
        .collect();

    let start = (0, 0);
    let dest = (grid.len() - 1, grid.first().unwrap().len() - 1);

    let ans = dijkstra(grid, start, dest);

    println!("Part 1: {}", ans);
}


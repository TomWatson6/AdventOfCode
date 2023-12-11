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

fn get_next(grid: &Vec<Vec<char>>, valid_paths: &HashMap<(i64, i64), Vec<char>>, adj_map: &HashMap<char, Vec<(i64, i64)>>,
            last: &(i64, i64), pos: &(i64, i64)) -> (i64, i64) {
    if let Some(adjs) = adj_map.get(&grid[pos.0 as usize][pos.1 as usize]) {
        for (dr, dc) in adjs {
            if dr.abs() == dc.abs() {
                return (0, 0);
            }

            let rr = pos.0 + dr;
            let cc = pos.1 + dc;

            if rr < 0 || rr >= grid.len() as i64 || cc < 0 || cc >= grid[0].len() as i64 {
                continue;
            }

            if (rr, cc) == *last {
                continue;
            }

            match valid_paths.get(&(*dr, *dc)) {
                Some(x) => {
                    if x.contains(&grid[rr as usize][cc as usize]) {
                        return (rr, cc)
                    }
                },
                None => return (0, 0),
            }
        }
    }

    (0, 0)
}

fn inside_loop(pipe: &HashSet<(i64, i64)>, pos: (i64, i64), mut visited: &mut HashSet<(i64, i64)>, bounds: &Bounds) -> bool {
    if visited.contains(&pos) {
        return true;
    }

    visited.insert(pos);

    let (r, c) = pos;

    if r < bounds.r_low || r > bounds.r_high || c < bounds.c_low || c > bounds.c_high {
        return false
    }

    for dr in -1 as i64..2 as i64 {
        for dc in -1 as i64..2 as i64 {
            if dr.abs() == dc.abs() {
                continue;
            }

            let rr = r + dr;
            let cc = c + dc;

            if pipe.contains(&(rr, cc)) {
                continue;
            }

            let output = inside_loop(pipe, (rr, cc), visited, bounds);
            if !output {
                return output;
            }
        }
    }

    true
}

fn flood_fill(pipe: &HashSet<(i64, i64)>, inside: &HashSet<(i64, i64)>, bounds: &Bounds) -> i64 {
    let start: (i64, i64) = (bounds.r_low - 1, bounds.c_low - 1);
    let mut queue: Vec<(i64, i64)> = vec![start];
    let mut seen: HashSet<(i64, i64)> = HashSet::new();

    while let Some((r, c)) = queue.pop() {
        if seen.contains(&(r, c)) {
            continue;
        }

        seen.insert((r, c));

        for dr in [-1, 0, 1] as [i64; 3] {
            for dc in [-1, 0, 1] as [i64; 3] {
                if dr.abs() == dc.abs() {
                    continue;
                }

                let rr = r + dr;
                let cc = c + dc;

                if rr < bounds.r_low - 1 || rr > bounds.r_high * 2 + 2 {
                    continue;
                }

                if cc < bounds.c_low - 1 || cc > bounds.c_high * 2 + 2 {
                    continue;
                }

                if pipe.contains(&(rr, cc)) {
                    continue;
                }

                queue.push((rr, cc));
            }
        }
    }

    let to_remove = seen.intersection(inside);

    to_remove.count() as i64
}

fn expand_pipe(pipe: Vec<(i64, i64)>) -> Vec<(i64, i64)> {
    let mut expanded: Vec<(i64, i64)> = Vec::new();

    for i in 0..pipe.len() - 1 {
        expanded.push((pipe[i].0 * 2, pipe[i].1 * 2));
        let d = (pipe[i + 1].0 - pipe[i].0, pipe[i + 1].1 - pipe[i].1);
        expanded.push((pipe[i].0 * 2 + d.0, pipe[i].1 * 2 + d.1));
    }

    expanded
}

struct Bounds {
    r_low: i64,
    r_high: i64,
    c_low: i64,
    c_high: i64,
}

fn main() {
    let input = read_file("input.txt");

    let valid_paths: HashMap<(i64, i64), Vec<char>> = HashMap::from([
        ((-1, 0), vec!['|', '7', 'F', 'S']), // Up
        ((1, 0), vec!['|', 'L', 'J', 'S']), // Down
        ((0, -1), vec!['-', 'L', 'F', 'S']), // Left
        ((0, 1), vec!['-', 'J', '7', 'S']), // Right
    ]);

    let adj_map: HashMap<char, Vec<(i64, i64)>> = HashMap::from([
        ('S', vec![(1, 0), (-1, 0), (0, 1), (0, -1)]),
        ('F', vec![(1, 0), (0, 1)]),
        ('7', vec![(1, 0), (0, -1)]),
        ('J', vec![(-1, 0), (0, -1)]),
        ('L', vec![(-1, 0), (0, 1)]),
        ('|', vec![(-1, 0), (1, 0)]),
        ('-', vec![(0, -1), (0, 1)]),
    ]);

    let grid: Vec<Vec<char>> = input.lines().map(|x| x.chars().collect()).collect();

    let mut start: (i64, i64) = (0, 0);

    for (r, row) in grid.iter().enumerate() {
        for (c, ch) in row.iter().enumerate() {
            if *ch == 'S' {
                start = (r as i64, c as i64);
            }
        }
    }

    let mut pos = start;
    let mut last = start;
    let mut pipe: Vec<(i64, i64)> = vec![start];
    let mut count = 0;

    loop {
        let next = get_next(&grid, &valid_paths, &adj_map, &last, &pos);
        pipe.push(next);
        last = pos;
        pos = next;
        count += 1;

        if pos == start {
            break
        }
    }

    count /= 2;

    println!("Part 1: {}", count);

    let pipe_set: HashSet<(i64, i64)> = pipe.clone().into_iter().collect();

    let r_low = pipe.iter().map(|x| x.0).min().unwrap();
    let r_high = pipe.iter().map(|x| x.0).max().unwrap();
    let c_low = pipe.iter().map(|x| x.1).min().unwrap();
    let c_high = pipe.iter().map(|x| x.1).max().unwrap();

    let bounds = Bounds{r_low, r_high, c_low, c_high};
    let mut inside: Vec<(i64, i64)> = Vec::new();

    let mut total = 0;

    for r in r_low..r_high + 1 {
        for c in c_low..c_high + 1 {
            if pipe.contains(&(r, c)) {
                continue;
            }

            let mut visited: HashSet<(i64, i64)> = HashSet::new();

            if inside_loop(&pipe_set, (r, c), &mut visited, &bounds) {
                total += 1;
                inside.push((r, c));
            }
        }
    }

    let pipe: HashSet<(i64, i64)> = expand_pipe(pipe).into_iter().collect();
    let inside: HashSet<(i64, i64)> = inside.into_iter().map(|(a, b)| (a * 2, b * 2)).collect();

    let num_inside = flood_fill(&pipe, &inside, &bounds);

    println!("Part 2: {}", total - num_inside);
}


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

fn dfs(mask: &Vec<char>, crit: &Vec<usize>, index: usize, crit_index: usize, count: usize, memo: &mut HashMap<(usize, usize, usize), usize>) -> usize {
    let key = (index, crit_index, count);

    if let Some(x) = memo.get(&key) {
        return *x;
    }

    if index == mask.len() {
        if crit_index == crit.len() && count == 0 {
            return 1;
        }
        else if crit_index == crit.len() - 1 && crit[crit_index] == count {
            return 1;
        }
        else {
            return 0;
        }
    }

    let mut output = 0;

    for c in ['.', '#'] {
        if mask[index] == c || mask[index] == '?' {
            if c == '.' && count == 0 {
                output += dfs(mask, crit, index + 1, crit_index, 0, memo);
            }
            else if c == '.' && count > 0 && crit_index < crit.len() && crit[crit_index] == count {
                output += dfs(mask, crit, index + 1, crit_index + 1, 0, memo);
            }
            else if c == '#' {
                output += dfs(mask, crit, index + 1, crit_index, count + 1, memo);
            }
        }
    }

    *memo.entry(key).or_insert(0) = output;

    output
}

fn expand(mask: Vec<char>, crit: Vec<usize>) -> (Vec<char>, Vec<usize>) {
    let mut new_mask: Vec<char> = Vec::new();
    let mut new_crit: Vec<usize> = Vec::new();

    for i in 0..5 {
        for m in mask.iter() {
            new_mask.push(*m);
        }

        for c in crit.iter() {
            new_crit.push(*c);
        }

        if i == 4 {
            break;
        }

        new_mask.push('?');
    }

    (new_mask, new_crit)
}

fn main() {
    let input = read_file("input.txt");
    let mut total = 0;
    let mut total2 = 0;

    for line in input.lines() {
        let (mask, crit) = line.split_once(' ').unwrap();
        let crit: Vec<usize> = crit.split(',').collect::<Vec<&str>>().into_iter().map(|x| x.parse().unwrap()).collect();
        let mut curr: Vec<char> = Vec::new();
        let mut memo: HashMap<(usize, usize, usize), usize> = HashMap::new();
        let mask = mask.chars().collect();

        let amount = dfs(&mask, &crit, 0, 0, 0, &mut memo);
        total += amount;

        let mut memo: HashMap<(usize, usize, usize), usize> = HashMap::new();
        let (mask, crit) = expand(mask, crit);

        let amount = dfs(&mask, &crit, 0, 0, 0, &mut memo);
        total2 += amount;
    }

    println!("Part 1: {}", total);
    println!("Part 2: {}", total2);
}


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

fn parse_input(input: String) -> (Vec<Vec<char>>, Vec<String>) {
    let parts = input.split("\n\n").collect::<Vec<&str>>();
    let mut rows: Vec<Vec<char>> = Vec::new();

    for line in parts[0].lines() {
        let chars = line.chars().collect::<Vec<char>>();
        let mut row: Vec<char> = Vec::new();
        let mut i = 1;

        assert!(line.len() > 1);

        while i < line.len() {
            let c = chars[i];
            row.push(c);
            i += 4;
        }

        rows.push(row);
    }

    let rows = &rows[..rows.len() - 1];

    let height = rows.len();
    let width = rows[0].len();

    let mut stacks: Vec<Vec<char>> = Vec::new();

    for w in 0..width {
        let mut stack: Vec<char> = Vec::new();

        for h in (0..height).rev() {
            if rows[h][w] != ' ' {
                stack.push(rows[h][w]);
            }
        }

        stacks.push(stack);
    }

    (stacks, parts[1].lines().map(|x| x.to_string()).collect())
}

fn main() {
    let input = read_file("input.txt");
    let (mut stacks, instructions) = parse_input(input);
    let mut cached = stacks.clone();

    for i in instructions.clone() {
        let parts = i.split(" ").collect::<Vec<&str>>();

        let amt = parts[1].parse::<usize>().unwrap();
        let from = parts[3].parse::<usize>().unwrap() - 1;
        let to = parts[5].parse::<usize>().unwrap() - 1;

        for _ in 0..amt {
            let c = stacks[from].pop().unwrap();
            stacks[to].push(c);
        }
    }

    let mut output = String::new();

    for s in stacks {
        output.push_str(&s.last().unwrap().to_string());
    }

    println!("Part 1: {}", output);

    stacks = cached;

    for i in instructions {
        let parts = i.split(" ").collect::<Vec<&str>>();

        let amt = parts[1].parse::<usize>().unwrap();
        let from = parts[3].parse::<usize>().unwrap() - 1;
        let to = parts[5].parse::<usize>().unwrap() - 1;

        let to_move = stacks[from][stacks[from].len() - amt..stacks[from].len()].to_vec();
        
        for m in to_move {
            stacks[to].push(m);
        }

        stacks[from] = stacks[from][..stacks[from].len() - amt].to_vec();
    }

    let mut output = String::new();

    for s in stacks {
        output.push_str(&s.last().unwrap().to_string());
    }

    println!("Part 2: {}", output)
}


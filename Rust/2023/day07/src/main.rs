#![allow(unused)]

use std::io::{self, Read};
use std::vec;
use std::io::{Write, BufReader, BufRead, ErrorKind};
use std::fs::File;
use std::cmp::Ordering;
use std::collections::{HashMap, HashSet};
use std::dbg;

fn read_file(file_name: &str) -> String {
    let mut file = File::open(file_name).unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    contents
}

fn strength(hand: String, p2: bool) -> (usize, String) {
    let tuples: Vec<(char, char)> = vec![('T', 'A'), ('J', 'B'), ('Q', 'C'), ('K', 'D'), ('A', 'E')];
    let mut rep: HashMap<_, _> = tuples.into_iter().collect();

    if p2 {
        *rep.entry('J').or_insert('B') = '1';
    }

    let tuples: Vec<(usize, Vec<usize>)> = vec![
        (6, vec![5]),
        (5, vec![1, 4]),
        (4, vec![2, 3]),
        (3, vec![1, 1, 3]),
        (2, vec![1, 2, 2]),
        (1, vec![1, 1, 1, 2]),
    ];
    let types: HashMap<_, _> = tuples.into_iter().collect();

    let hand: String = hand
        .chars()
        .map(|x| match rep.get(&x) {
            Some(&y) => y,
            None => x,
        })
        .collect();

    let mut counts: HashMap<char, usize> = HashMap::new();

    for card in hand.chars() {
        *counts.entry(card).or_insert(0) += 1;
    }

    if p2 {
        let mut target = counts.keys().next().unwrap();

        for (card, count) in &counts {
            if *card != '1' {
                if let Some(x) = counts.get(target) {
                    if count > x || *target == '1' {
                        target = card;
                    }
                }
            }
        }

        if *target != '1' {
            if let Some(&x) = &counts.get(&'1') {
                *counts.entry(*target).or_insert(0) += x;
                counts.remove(&'1');
            }
        }
    }

    let mut values: Vec<&usize> = counts.values().collect();
    values.sort();

    for (score, config) in types {
        if values.iter().zip(config).all(|(a, b)| **a == b) {
            return (score, hand);
        }
    }

    (0, hand)
}

fn main() {
    let input = read_file("input.txt");

    let mut bids: HashMap<&str, usize> = HashMap::new();

    for line in input.lines() {
        if let Some((cards, bid)) = line.split_once(' ') {
            bids.insert(cards, bid.parse::<usize>().unwrap());
        }
    }

    for p2 in [false, true] {
        let mut hands: Vec<String> = bids.keys().map(|x| x.to_string()).collect();
        hands.sort_by_key(|x| strength(x.clone(), p2));

        let mut total = 0;

        for (i, h) in hands.iter().enumerate() {
            if let Some(x) = bids.get(h.as_str()) {
                total += (i + 1) * x;
                continue
            }
            panic!("Bid not found for {}", h);
        }

        match p2 {
            false => println!("Part 1: {}", total),
            true => println!("Part 2: {}", total),
        }
    }
}


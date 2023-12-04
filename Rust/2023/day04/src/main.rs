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

fn get_num_cards(cards: &HashMap<i32, (HashSet<i32>, HashSet<i32>)>, id: &i32, winning_cards: &HashMap<i32, i32>, memo: &mut HashMap<i32, i32>) -> i32 {
    if let Some(x) = memo.get(id) {
        return *x;
    }

    let mut total = 0;

    if let Some(x) = winning_cards.get(id) {
        total += x;

        for i in id + 1..id + x + 1 {
            total += get_num_cards(cards, &i, winning_cards, memo);
        }

        *memo.entry(*id).or_insert(0) = total;

        return total;
    }

    0
}

fn main() {
    let input = read_file("input.txt");

    let mut cards: HashMap<i32, (HashSet<i32>, HashSet<i32>)> = HashMap::new();
    let mut winning_cards: HashMap<i32, i32> = HashMap::new();

    for line in input.lines() {
        let parts: Vec<&str> = line.split(' ').filter(|x| !x.is_empty()).collect();

        let id = match parts.get(1) {
            Some(x) => {
                let mut ch = x.chars().collect::<Vec<char>>();
                ch = ch[..ch.len() - 1].to_vec();
                let id_str = ch.into_iter().collect::<String>();
                match id_str.parse::<i32>() {
                    Ok(x) => x,
                    Err(e) => panic!("{} -> {:?}", id_str, e),
                }
            },
            None => panic!("No ID found in line: {}", line),
        };

        let mut winning: HashSet<i32> = HashSet::new();
        let mut owned: HashSet<i32> = HashSet::new();
        let mut winners = true;

        for i in 2..parts.len() {
            if parts[i] == "|" {
                winners = false;
                continue
            }

            match parts[i].parse::<i32>() {
                Ok(x) => {
                    if winners {
                        winning.insert(x);
                        continue;
                    }

                    owned.insert(x);
                },
                Err(e) => panic!("{} -> {:?}", parts[i], e)
            }
        }

        *cards.entry(id).or_insert((HashSet::new(), HashSet::new())) = (winning, owned);
    }

    let mut total = 0;

    for (id, sets) in cards.iter() {
        let winners: HashSet<&i32> = sets.0.intersection(&sets.1).collect();

        if winners.len() > 0 {
            *winning_cards.entry(*id).or_insert(0) = winners.len() as i32;

            let base: i32 = 2;
            let count = base.pow((winners.len() - 1) as u32);
            total += count;
        }
    }

    println!("Part 1: {}", total);

    total = 0;
    let mut memo: HashMap<i32, i32> = HashMap::new();

    for (id, _) in cards.iter() {
        total += get_num_cards(&cards, &id, &winning_cards, &mut memo)
    }
    
    println!("Part 2: {}", total);
}


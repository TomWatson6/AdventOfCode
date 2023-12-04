#![allow(unused)]

use peak_alloc::PeakAlloc;

#[global_allocator]
static PEAK_ALLOC: PeakAlloc = PeakAlloc;

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

fn get_num_cards(cards: &HashMap<usize, (HashSet<usize>, HashSet<usize>)>, id: &usize, winning_cards: &HashMap<usize, usize>, memo: &mut HashMap<usize, usize>) -> usize {
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

    let mut cards: HashMap<usize, (HashSet<usize>, HashSet<usize>)> = HashMap::new();
    let mut winning_cards: HashMap<usize, usize> = HashMap::new();

    for line in input.lines() {
        let parts: Vec<&str> = line.split(' ').filter(|x| !x.is_empty()).collect();

        let id = match parts.get(1) {
            Some(x) => {
                let mut ch = x.chars().collect::<Vec<char>>();
                ch = ch[..ch.len() - 1].to_vec();
                let id_str = ch.into_iter().collect::<String>();
                match id_str.parse::<usize>() {
                    Ok(x) => x,
                    Err(e) => panic!("{} -> {:?}", id_str, e),
                }
            },
            None => panic!("No ID found in line: {}", line),
        };

        let mut winning: HashSet<usize> = HashSet::new();
        let mut owned: HashSet<usize> = HashSet::new();
        let mut winners = true;

        for i in 2..parts.len() {
            if parts[i] == "|" {
                winners = false;
                continue
            }

            match parts[i].parse::<usize>() {
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

    let mut total: usize = 0;

    for (id, sets) in cards.iter() {
        let winners: HashSet<&usize> = sets.0.intersection(&sets.1).collect();

        if winners.len() > 0 {
            *winning_cards.entry(*id).or_insert(0) = winners.len() as usize;

            let base: usize = 2;
            let count: usize = base.pow((winners.len() - 1) as u32) as usize;
            total += count;
        }
    }

    println!("Part 1: {}", total);

    total = cards.len();
    let mut memo: HashMap<usize, usize> = HashMap::new();

    for (id, _) in cards.iter() {
        total += get_num_cards(&cards, &id, &winning_cards, &mut memo)
    }
    
    println!("Part 2: {}", total);


    let peak_mem = PEAK_ALLOC.peak_usage_as_mb();
    println!("The max amount that was used {}", peak_mem);
}


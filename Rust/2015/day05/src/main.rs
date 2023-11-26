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

fn has_three_vowels(s: &str) -> bool {
    let mut vowels = 0;

    for c in s.chars() {
        match c {
            'a' | 'e' | 'i' | 'o' | 'u' => vowels += 1,
            _ => continue,
        };
    }

    vowels >= 3
}

fn has_double_letter(s: &str) -> bool {
    let chars = s.chars().collect::<Vec<char>>();

    for i in 1..chars.len() {
        if chars[i] == chars[i-1] {
            return true;
        }
    }

    false
}

fn no_bad_strings(s: &str) -> bool {
    let chars = s.chars().collect::<Vec<char>>();

    for i in 1..chars.len() {
        match format!("{}{}", chars[i-1], chars[i]).as_str() {
            "ab" | "cd" | "pq" | "xy" => return false,
            _ => continue,
        };
    }

    true
}

fn has_two_pairs(s: &str) -> bool {
    let mut pairs: HashMap<String, i32> = HashMap::new();
    let mut last = String::from("");
    let chars = s.chars().collect::<Vec<char>>();

    for i in 0..chars.len() - 1 {
        let curr = format!("{}{}", chars[i], chars[i+1]);

        if curr == last {
            continue;
        }

        *pairs.entry(curr.clone()).or_insert(0) += 1;
        last = curr;
    }

    pairs.values().any(|&count| count >= 2)
}

fn sandwiches(s: &str) -> bool {
    let chars = s.chars().collect::<Vec<char>>();

    for i in 0..chars.len() - 2 {
        if chars[i] == chars[i + 2] {
            return true;
        }
    }

    false
}

fn main() {
    let input = read_file("input.txt");
    let mut nice = 0;
    let mut nice2 = 0;

    for line in input.lines() {
        if has_three_vowels(line) && has_double_letter(line) && no_bad_strings(line) {
            nice += 1;
        }
        
        if has_two_pairs(line) && sandwiches(line) {
            nice2 += 1;
        }
    }

    println!("Part 1: {}", nice);
    println!("Part 2: {}", nice2);
}


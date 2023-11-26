#![allow(unused)]

use std::io::{self, Read};
use std::vec;
use std::io::{Write, BufReader, BufRead, ErrorKind};
use std::fs::File;
use std::cmp::Ordering;

fn read_file(file_name: &str) -> String {
    let mut file = File::open(file_name).unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    contents
}

fn main() {
    let input = read_file("input.txt");

    let mut score1 = 0;
    let mut score2 = 0;

    for line in input.lines() {
        if line == "" {
            continue;
        }

        let parts: Vec<&str> = line.split(" ").collect();

        match (parts[0], parts[1]) {
            ("A", "X") => score1 += 4, // Rock (1) and Draw (3)
            ("A", "Y") => score1 += 8, // Paper(2) and Win(6)
            ("A", "Z") => score1 += 3, // Scissors(3) and Loss(0)
            ("B", "X") => score1 += 1, // Rock (1) and Loss(0)
            ("B", "Y") => score1 += 5, // Paper(2) and Draw(3)
            ("B", "Z") => score1 += 9, // Scissors(3) and Win(6)
            ("C", "X") => score1 += 7, // Rock(1) and Win(6)
            ("C", "Y") => score1 += 2, // Paper(2) and Loss(0)
            ("C", "Z") => score1 += 6, // Scissors(3) and Draw(3)
            (&_, _) => todo!()
        }

        match (parts[0], parts[1]) {
            ("A", "X") => score2 += 3, // Choose Scissors(3) to Lose(0)
            ("A", "Y") => score2 += 4, // Choose Rock(1) to Draw(3)
            ("A", "Z") => score2 += 8, // Choose Paper(2) to Win(6)
            ("B", "X") => score2 += 1, // Choose Rock(1) to Lose(0)
            ("B", "Y") => score2 += 5, // Choose Paper(2) to Draw(3)
            ("B", "Z") => score2 += 9, // Choose Scissors(3) to Win(6)
            ("C", "X") => score2 += 2, // Choose Paper(2) to Lose(0)
            ("C", "Y") => score2 += 6, // Choose Scissors(3) to Draw(3)
            ("C", "Z") => score2 += 7, // Choose Rock(1) to Win(6)
            (&_, _) => todo!()
        }
    }

    println!("Part 1: {}", score1);
    println!("Part 2: {}", score2)
}


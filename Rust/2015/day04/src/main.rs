#![allow(unused)]

use std::io::{self, Read};
use std::vec;
use std::io::{Write, BufReader, BufRead, ErrorKind};
use std::fs::File;
use std::cmp::Ordering;
use std::collections::{HashMap, HashSet};

fn main() {
    let input = String::from("iwrupvqb");
    let mut p1_done = false;
    let mut i = 0;

    loop {
        let mut h = input.clone();
        h = format!("{}{}", h, i).to_string();
        let hash = format!("{:x}", md5::compute(h));
        let first = hash[..5].to_string();
        let first2 = hash[..6].to_string();
        if first == "00000" && !p1_done {
            println!("Part 1: {}", i);
            p1_done = true;
        }

        if first2 == "000000" {
            println!("Part 2: {}", i);
            break;
        }
        
        i += 1;
    }
}


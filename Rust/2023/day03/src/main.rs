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

fn get_char(input: String, r: usize, c: usize) -> char {
    input.lines().nth(r).unwrap()
        .chars().nth(c).unwrap()
}

fn get_bounding_box_coords(input: String, r: i32, c: i32, t: i32) -> HashSet<(usize, usize)> {
    let mut bounding_box_coords: HashSet<(usize, usize)> = HashSet::new();

    for rr in r-1..r+2 {
        for cc in c-1..c+t+1 {
            if rr < 0 || cc < 0 {
                continue;
            }

            match input.lines().nth(rr as usize) {
                Some(x) => match x.chars().nth(cc as usize) {
                    Some(y) => bounding_box_coords.insert((rr as usize, cc as usize)),
                    None => continue,
                },
                None => continue,
            };
        }
    }

    bounding_box_coords
}

fn main() {
    let input = read_file("input.txt");

    let mut bounding_boxes: Vec<(i32, HashSet<(usize, usize)>)> = Vec::new();

    for (i, line) in input.lines().enumerate() {
        let mut j = 0;
        let chars = line.chars().collect::<Vec<char>>();

        while j < chars.len() {
            let mut n: Vec<char> = Vec::new();

            if chars[j].is_numeric() {
                let mut t = 0;
                
                while chars[j + t].is_numeric() {
                    n.push(chars[j + t]);

                    t += 1;

                    if j + t >= chars.len() {
                        break
                    }
                }

                let n: String = n.into_iter().collect();

                bounding_boxes.push(
                    (
                        n.parse().unwrap(), 
                        get_bounding_box_coords(
                            input.clone(), 
                            i.try_into().unwrap(), 
                            j.try_into().unwrap(), 
                            t.try_into().unwrap()
                        )
                    )
                );

                j += t;
            }

            j += 1
        }
    }

    let mut total = 0;

    for (num, bounding_box_coord) in bounding_boxes.clone() {
        for coord in bounding_box_coord {
            let c = get_char(input.clone(), coord.0, coord.1);
            if !c.is_numeric() && c != '.' {
                total += num;
                break;
            }
        }
    }

    println!("Part 1: {}", total);

    total = 0;

    for i in 0..bounding_boxes.len() - 1 {
        let set1 = &bounding_boxes[i].1;

        for j in i + 1..bounding_boxes.len() {
            let set2 = &bounding_boxes[j].1;

            let intersection = set1.intersection(set2);

            if intersection.clone().count() > 0 {
                for coord in intersection {
                    if get_char(input.clone(), coord.0, coord.1) == '*' {
                        total += bounding_boxes[i].0 * bounding_boxes[j].0;
                    }
                }
            }
        }
    }

    println!("Part 2: {}", total);
}


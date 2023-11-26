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

fn surface_area(l: usize, w: usize, h: usize) -> usize {
    2*l*w + 2*w*h + 2*h*l
}

fn smallest_size(l: usize, w: usize, h: usize) -> usize {
    let mut sides = [l * w, w * h, h * l];
    sides.sort();
    sides[0]
}

fn ribbon_around_box(l: usize, w: usize, h: usize) -> usize {
    let mut faces = [2 * (l + w), 2 * (w + h), 2 * (h + l)];
    faces.sort();
    faces[0]
}

fn volume(l: usize, w: usize, h: usize) -> usize {
    l * w * h
}

fn main() {
    let input = read_file("input.txt");
    let mut total = 0;
    let mut ribbon = 0;

    for line in input.lines() {
        let parts = line.split('x').collect::<Vec<&str>>();

        let length: usize = parts[0].parse().unwrap();
        let width: usize = parts[1].parse().unwrap();
        let height: usize = parts[2].parse().unwrap();

        total += surface_area(length, width, height) + smallest_size(length, width, height);
        ribbon += ribbon_around_box(length, width, height) + volume(length, width, height);
    }

    println!("Part 1: {}", total);
    println!("Part 2: {}", ribbon)
}


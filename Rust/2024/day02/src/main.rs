use std::fs::File;
use std::io::Read;
use std::collections::HashMap;

fn read_input(file_name: &str) -> String {
    let mut file = File::open(file_name).unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    contents
}

fn part1(left: &Vec<usize>, right: &Vec<usize>) -> usize {
    0
}

fn part2(left: &Vec<usize>, right: &Vec<usize>) -> usize {
    0
}

fn main() {
    let input = read_input("input.txt");
    let mut total = 0;

    for line in input.lines() {
        let safe = line.split(' ')
            .collect::<Vec<_>>()
            .iter()
            .filter_map(|x| x.parse::<usize>().ok())
            .collect::<Vec<usize>>()
            .windows(2)
            // .all(|x| *x.0 < *x.1 && *x.0.);
    }
}

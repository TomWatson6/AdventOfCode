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
    left.iter()
        .zip(right)
        .fold(0, |curr, (l, r)| curr + (*l as isize - *r as isize).abs() as usize)
}

fn part2(left: &Vec<usize>, right: &Vec<usize>) -> usize {
    let mut counts: HashMap<usize, usize> = HashMap::new();

    for r in right {
        match counts.get(r) {
            Some(x) => counts.insert(*r, x + 1),
            None => counts.insert(*r, 1),
        };
    }

    left.iter()
        .filter(|x| counts.contains_key(x))
        .map(|x| x * counts.get(x).unwrap())
        .sum()
}

fn main() {
    let input = read_input("input.txt");
<<<<<<< HEAD
    let mut left: Vec<usize> = Vec::new();
    let mut right: Vec<usize> = Vec::new();

    for line in input.lines() {
        let (l, r) = line.split_once("   ").unwrap();
        left.push(l.parse::<usize>().unwrap());
        right.push(r.parse::<usize>().unwrap());
    }

    left.sort();
    right.sort();

    println!("Part 1: {}", part1(&left, &right));
    println!("Part 2: {}", part2(&left, &right));
=======
    let mut l1: Vec<usize> = Vec::new();
    let mut l2: Vec<usize> = Vec::new();

    for line in input.lines() {
        let parts = line.split_whitespace().collect::<Vec<_>>();
        let left: usize = parts[0].parse().unwrap();
        let right: usize = parts[1].parse().unwrap();
        l1.push(left);
        l2.push(right);
    }

    l1.sort();
    l2.sort();
    let mut counts: HashMap<usize, usize> = HashMap::new();

    let mut total = 0;

    for i in 0..l1.len() {
        total += l1[i].abs_diff(l2[i]);
        
        if let Some(x) = counts.get(&l2[i]) {
            counts.insert(l2[i], x + 1);
        } else {
            counts.insert(l2[i], 1);
        }
    }

    let mut total2 = 0;

    for num in l1 {
        if let Some(x) = counts.get(&num) {
            total2 += num * x;
        }
    }

    println!("Part 1: {}", total);
    println!("Part 2: {}", total2);
>>>>>>> 025dc72fb86e5a140557e7b519cde7c49e544d8c
}

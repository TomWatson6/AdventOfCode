use std::fs::File;
use std::io::Read;
use std::collections::HashMap;

fn read_input(file_name: &str) -> String {
    let mut file = File::open(file_name).unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    contents
}

fn main() {
    let input = read_input("input.txt");
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
}

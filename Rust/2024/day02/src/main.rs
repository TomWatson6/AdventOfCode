use std::fs::File;
use std::io::Read;

fn read_input(file_name: &str) -> String {
    let mut file = File::open(file_name).unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    contents
}

fn main() {
    let input = read_input("input.txt");
    let mut total = 0;

    for line in input.lines() {
        let nums: Vec<usize> = line.split_whitespace().map(|x| x.parse::<usize>().unwrap()).collect();

        let ascending = nums.windows(2).all(|x| x[0] < x[1]);
        let descending = nums.windows(2).all(|x| x[0] > x[1]);
        let diffs_check = nums.windows(2).all(|x| x[0].abs_diff(x[1]) <= 3);

        let valid = (ascending || descending) && diffs_check;
        if valid {
            total += 1;
        }
    }

    println!("Part 1: {}", total);
    total = 0;

    for line in input.lines() {
        let nums: Vec<usize> = line.split_whitespace().map(|x| x.parse::<usize>().unwrap()).collect();

        for i in 0..nums.len() {
            let mut copy = nums.clone();
            copy.remove(i);

            let ascending = copy.windows(2).all(|x| x[0] < x[1]);
            let descending = copy.windows(2).all(|x| x[0] > x[1]);
            let diffs_check = copy.windows(2).all(|x| x[0].abs_diff(x[1]) <= 3);

            let valid = (ascending || descending) && diffs_check;
            if valid {
                total += 1;
                break;
            }
        }
    }

    println!("Part 2: {}", total);
}

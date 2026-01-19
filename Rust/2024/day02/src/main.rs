use std::fs::File;
use std::io::Read;
<<<<<<< HEAD
use std::collections::HashMap;
=======
>>>>>>> 025dc72fb86e5a140557e7b519cde7c49e544d8c

fn read_input(file_name: &str) -> String {
    let mut file = File::open(file_name).unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    contents
}

<<<<<<< HEAD
fn part1(left: &Vec<usize>, right: &Vec<usize>) -> usize {
    0
}

fn part2(left: &Vec<usize>, right: &Vec<usize>) -> usize {
    0
}

=======
>>>>>>> 025dc72fb86e5a140557e7b519cde7c49e544d8c
fn main() {
    let input = read_input("input.txt");
    let mut total = 0;

    for line in input.lines() {
<<<<<<< HEAD
        let safe = line.split(' ')
            .collect::<Vec<_>>()
            .iter()
            .filter_map(|x| x.parse::<usize>().ok())
            .collect::<Vec<usize>>()
            .windows(2)
            // .all(|x| *x.0 < *x.1 && *x.0.);
    }
=======
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
>>>>>>> 025dc72fb86e5a140557e7b519cde7c49e544d8c
}

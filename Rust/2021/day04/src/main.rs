use std::fs::File;
use std::io::Read;
use std::collections::{HashMap, HashSet};

fn read_file(file_name: &str) -> String {
    let mut file = File::open(file_name).unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    contents
}

#[derive(Debug, Clone)]
struct Board {
    numbers: HashMap<usize, (usize, usize)>,
    marked: HashSet<(usize, usize)>
}

impl From<&str> for Board {
    fn from(value: &str) -> Self {
        let mut numbers: HashMap<usize, (usize, usize)> = HashMap::new();

        for (i, line) in value.lines().enumerate() {
            let nums: Vec<usize> = line
                .split(' ')
                .filter_map(|x| x.parse().ok())
                .collect();

            for (j, num) in nums.iter().enumerate() {
                numbers.insert(*num, (i, j));
            }
        }

        Self {
            numbers,
            marked: HashSet::new(),
        }
    }
}

impl Board {
    fn mark(&mut self, number: usize) {
        if let Some(x) = self.numbers.get(&number) {
            self.marked.insert(*x);
        }
    }

    fn marked(&self) -> usize {
        self.marked.len()
    }

    fn is_winner(&self) -> bool {
        for i in 0..5 {
            if self.marked
                .iter()
                .filter(|x| x.0 == i)
                .count() == 5 {
                    return true;
                }

            if self.marked
                .iter()
                .filter(|x| x.1 == i)
                .count() == 5 {
                    return true;
                }
        }

        false
    }
}

fn main() {
    let input = read_file("input.txt");

    let nums: Vec<usize> = input
        .lines()
        .next()
        .unwrap()
        .split(',')
        .map(|x| x.parse().unwrap())
        .collect();

    let boards: Vec<Board> = input
        .split("\n\n")
        .skip(1)
        .map(Board::from)
        .collect();

    let boards = boards.clone();

    'outer: for num in nums {
        for mut board in boards.clone() {
            board.mark(num);
            if board.is_winner() {
                println!("We have a winner: {:?}", board);
                break 'outer;
            }
        }
    }
}

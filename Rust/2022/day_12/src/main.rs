use std::fs::File;
use std::io::Read;
use std::collections::{HashMap, HashSet, VecDeque};

fn read_file(file_name: &str) -> String {
    let mut file = File::open(file_name).unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    contents
}

#[derive(Debug)]
struct Grid {
    squares: HashMap<(isize, isize), char>,
    start: (isize, isize),
    dest: (isize, isize),
}

impl From<String> for Grid {
    fn from(value: String) -> Self {
        let mut squares: HashMap<(isize, isize), char> = HashMap::new();
        let mut start: (isize, isize) = (0, 0);
        let mut dest: (isize, isize) = (0, 0);

        for (i, line) in value.lines().enumerate() {
            for (j, c) in line.chars().enumerate() {
                let i = i as isize;
                let j = j as isize;

                match c {
                    'S' => start = (i, j),
                    'E' => dest = (i, j),
                    _ => {},
                }

                squares.insert((i, j), c);
            }
        }

        Self {
            squares,
            start,
            dest,
        }
    }
}

impl Grid {
    fn get_valid_adjacents(&self, loc: (isize, isize)) -> Vec<(isize, isize)>  {
        let mut adjacents: Vec<(isize, isize)> = Vec::new();
        let curr = match self.squares.get(&loc).unwrap() {
            'S' => 'a',
            other => *other,
        };

        // List of possible directions (up, down, left, right)
        let directions = [(1, 0), (-1, 0), (0, 1), (0, -1)];

        for (dr, dc) in &directions {
            let rr = loc.0 + dr;
            let cc = loc.1 + dc;

            if let Some(&neighbor_char) = self.squares.get(&(rr, cc)) {
                let neighbor = match neighbor_char {
                    'E' => 'z',
                    other => other,
                };

                // Allow moves to neighbors that are within one alphabetical step forward
                if (neighbor as usize) <= (curr as usize) + 1 {
                    adjacents.push((rr, cc));
                }
            }
        }

        adjacents
    }

    fn find(&self, start: (isize, isize)) -> Option<usize> {
        let mut queue: VecDeque<((isize, isize), usize)> = VecDeque::new();
        let mut seen: HashSet<(isize, isize)> = HashSet::new();
        seen.insert(start);
        queue.push_back((start, 0));

        while let Some((curr, depth)) = queue.pop_front() {
            if *self.squares.get(&curr).unwrap() == 'E' {
                return Some(depth);
            }

            let adjacents = self.get_valid_adjacents(curr);

            for adj in adjacents {
                if !seen.contains(&adj) {
                    seen.insert(adj);
                    queue.push_back((adj, depth + 1));
                }
            }
        }

        None
    }
}

fn main() {
    let input = read_file("simple_input.txt");
    let grid = Grid::from(input);
    let dist = grid.find(grid.start);

    match dist {
        Some(d) => println!("{}", d),
        None => println!("No path found"),
    }
}


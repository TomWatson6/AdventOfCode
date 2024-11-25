use std::fs::File;
use std::io::Read;
use std::collections::{HashMap, HashSet};

fn read_file(file_name: &str) -> String {
    let mut file = File::open(file_name).unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    contents
}

#[derive(Debug)]
struct Grid {
    trees: HashMap<(isize, isize), isize>
}

impl From<String> for Grid {
    fn from(value: String) -> Self {
        let mut trees: HashMap<(isize, isize), isize> = HashMap::new();

        for (i, line) in value.lines().enumerate() {
            for (j, c) in line.chars().enumerate() {
                trees.insert((i as isize, j as isize), c.to_string().parse().unwrap());
            }
        }

        Self {
            trees
        }
    }
}

impl Grid {
    fn visible(&self, loc: (isize, isize), dir: (isize, isize)) -> HashSet<(isize, isize)> {
        let mut seen: HashSet<(isize, isize)> = HashSet::new();
        seen.insert(loc);
        let mut curr = (loc.0 + dir.0, loc.1 + dir.1);
        let mut prev: isize = 0;

        while let Some(x) = self.trees.get(&curr) {
            if *x > prev {
                println!("{:?} {:?} -> {} > {}", loc, dir, *x, prev);
                seen.insert(curr);
            } else {
                break
            }

            curr = (curr.0 + dir.0, curr.1 + dir.1);
            prev = *x;
        };

        seen
    }
}

fn main() {
    let input = read_file("simple_input.txt");
    let grid = Grid::from(input);

    let max_r = grid.trees.keys().map(|x| x.0).max().unwrap();
    let max_c = grid.trees.keys().map(|x| x.1).max().unwrap();

    let mut visible: HashSet<(isize, isize)> = HashSet::new();

    for i in 0..max_r {
        visible = visible.union(&grid.visible((i, 0), (0, 1))).map(|x| *x).collect();
        visible = visible.union(&grid.visible((i, max_c), (0, -1))).map(|x| *x).collect();
    }

    for i in 0..max_c {
        visible = visible.union(&grid.visible((0, i), (1, 0))).map(|x| *x).collect();
        visible = visible.union(&grid.visible((max_r, i), (-1, 0))).map(|x| *x).collect();
    }

    println!("Visible: {:?}", visible);
    println!("Part 1: {}", visible.len());
}

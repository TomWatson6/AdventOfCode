use std::fs::File;
use std::io::Read;
use std::collections::HashSet;

#[derive(Debug)]
struct Bound {
    lower: isize,
    upper: isize,
}

impl From<&str> for Bound {
    fn from(value: &str) -> Self {
        match value.split_once("..") {
            Some((lower, upper)) => {
                Self {
                    lower: lower.parse().unwrap(),
                    upper: upper.parse().unwrap(),
                }
            }
            _ => {
                if let Ok(x) = value.parse::<isize>() {
                    return Self {
                        lower: x,
                        upper: x,
                    }
                }

                Self {
                    lower: 0,
                    upper: 0,
                }
            }
        }
    }
}

#[derive(Debug)]
struct Coords {
    x: Bound,
    y: Bound,
}

impl From<&str> for Coords {
    fn from(value: &str) -> Self {
        let (mut left, mut right) = value
            .split_once(", ")
            .unwrap();

        if left.contains("x=") {
            left = &left[2..];
            right = &right[2..];
        } else {
            let temp = left;
            left = &right[2..];
            right = &temp[2..];
        }

        Self {
            x: Bound::from(left),
            y: Bound::from(right),
        }
    }
}

struct Grid {
    clay: HashSet<(isize, isize)>,
    water: HashSet<(isize, isize)>,
}

impl Grid {
    fn new() -> Self {
        Self {
            clay: HashSet::new(),
            water: HashSet::new(),
        }
    }

    fn get_bounds(&self) -> Coords {
        let low_x = self.clay.iter().map(|x| x.1).min().unwrap() - 1;
        let high_x = self.clay.iter().map(|x| x.1).max().unwrap() + 1;
        let low_y = self.clay.iter().map(|x| x.0).min().unwrap();
        let high_y = self.clay.iter().map(|x| x.0).max().unwrap();

        Coords {
            x: Bound {
                lower: low_x,
                upper: high_x,
            },
            y: Bound {
                lower: low_y,
                upper: high_y,
            }
        }
    }

    fn print(&self, bounds: &Coords) {
        for y in bounds.y.lower..bounds.y.upper + 1 {
            for x in bounds.x.lower..bounds.x.upper + 1 {
                match self.clay.get(&(y, x)) {
                    Some(_) => print!("#"),
                    _ => match self.water.get(&(y, x)) {
                        Some(_) => print!("~"),
                        _ => print!("."),
                    }
                }
            }

            println!();
        }
    }

    // Insert into water seen hashset up to and excluding dest
    fn insert_seen(&mut self, start: &(isize, isize), dest: &(isize, isize), offset: &(isize, isize)) {
        let mut loc = *start;

        while loc != *dest {
            self.water.insert(loc);
            loc = (loc.0 + offset.0, loc.1 + offset.1);
        }
    }

    // Returns amount in direction until wall, and if it's hit an edge so we know to terminate
    // scanning
    fn scan(&mut self, loc: &(isize, isize), offset: (isize, isize), bounds: &Coords) -> (isize, bool) {
        let mut next = *loc;
        let mut scanned: isize = 0;

        // While not hitting wall, and it hasn't fallen
        while !self.clay.contains(&next) && (self.clay.contains(&(next.0 + 1, next.1)) || self.water.contains(&(next.0 + 1, next.1))) {
            next = (next.0 + offset.0, next.1 + offset.1);

            if next.1 < bounds.x.lower || next.1 > bounds.x.upper {
                return (0, false);
            }

            if self.clay.contains(&next) {
                self.insert_seen(loc, &next, &offset);
                break;
            }
            
            if self.clay.contains(&(next.0 + 1, next.1 - offset.1)) && !self.clay.contains(&(next.0 + 1, next.1)) && !self.water.contains(&(next.0 + 1, next.1)) {
                self.insert_seen(loc, &(next.0 + offset.0, next.1 + offset.1), &offset);
                let (filled, fallen) = self.fill((next.0, next.1), bounds);
                return (scanned + filled, fallen);
            }

            scanned += 1;
        }

        (scanned, false)
    }

    fn fill(&mut self, loc: (isize, isize), bounds: &Coords) -> (isize, bool) {
        let mut curr = loc;
        let mut filled = 1; // including starting location
        
        while !self.clay.contains(&(curr.0 + 1, curr.1)) && !self.water.contains(&(curr.0 + 1, curr.1)) && curr.0 < bounds.y.upper {
            self.water.insert(curr);
            curr = (curr.0 + 1, curr.1);
            filled += 1;
        }

        self.water.insert(curr);

        if curr.0 >= bounds.y.upper {
            return (filled, true);
        }

        loop {
            let (left_amt, left_fall) = self.scan(&curr, (0, -1), bounds);
            let (right_amt, right_fall) = self.scan(&curr, (0, 1), bounds);

            filled += left_amt;
            filled += right_amt;

            if left_fall || right_fall {
                return (filled, true);
            }

            curr.0 -= 1;

            if curr.0 <= loc.0 {
                break;
            }
        }

        (filled, false)
    }
}

fn read_input(file_name: &str) -> Vec<Coords> {
    let mut file = File::open(file_name).unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    
    let mut coords: Vec<Coords> = Vec::new();

    for line in contents.lines() {
        coords.push(Coords::from(line));
    }

    coords
}

fn main() {
    let coords = read_input("input.txt");
    let mut grid: Grid = Grid::new();

    for coord in coords {
        for y in coord.y.lower..coord.y.upper + 1 {
            for x in coord.x.lower..coord.x.upper + 1 {
                grid.clay.insert((y, x));
            }
        }
    }

    let bounds = grid.get_bounds();

    let (total, _) = grid.fill((1, 500), &bounds);
    grid.print(&bounds);
    println!("Part 1: {}", total);
}

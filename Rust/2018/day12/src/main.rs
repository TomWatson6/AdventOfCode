use std::fs::File;
use std::io::Read;
use std::collections::{HashSet, HashMap};

fn read_input(file_name: &str) -> String {
    let mut file = File::open(file_name).unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    contents
}

#[derive(Debug)]
struct State {
    plants: HashMap<isize, String>,
    start: isize,
    end: isize
}

impl From<&str> for State {
    fn from(plants: &str) -> Self {
        let mut plants_map: HashMap<isize, String> = HashMap::new();
        let p: Vec<char> = plants.chars().collect();

        for i in 0..plants.len() {
            plants_map.insert(i as isize, p[i].to_string());
        }

        Self {
            plants: plants_map,
            start: 0,
            end: plants.len() as isize,
        }
    }
}

impl State {
    pub fn string(&self) -> String {
        let mut output = String::new();

        for i in self.start..self.end {
            match self.plants.get(&i) {
                Some(s) => output.push_str(s),
                _ => {},
            }
        }

        output
    }

    pub fn evolve(&mut self, transformations: &HashMap<&str, &str>, iterations: usize) -> isize {
        let mut seen: HashSet<String> = HashSet::new();
        let mut c = 0;
        
        while c < iterations {
            seen.insert(self.string());

            let mut next: HashMap<isize, String> = HashMap::new();

            let mut low = self.end;
            let mut high = self.start;

            for i in self.start-4..self.end+4 {
                let segment: String = (i-2..i+3)
                    .map(|x| match self.plants.get(&x) {
                        Some(v) => v,
                        _ => ".",
                    })
                    .collect();

                next.insert(
                    i,
                    match transformations.get(segment.as_str()) {
                        Some(x) => {
                            if *x == "#" {
                                low = std::cmp::min(low, i);
                                high = std::cmp::max(high, i + 1);
                            }
                            (*x).to_string()
                        },
                        _ => ".".to_string(),
                    }
                );
            }

            self.start = low;
            self.end = high;
            self.plants = next;

            if seen.get(&self.string()).is_some() {
                let rem = iterations - c - 1;
                return rem as isize
            }

            c += 1;
        }

        0
    }

    pub fn total_plants(&self, offset: isize) -> usize {
        let mut total = 0;

        for (k, v) in self.plants.iter() {
            if *v == "#" {
                total += *k + offset;
            }
        }

        total as usize
    }
}

fn main() {
    let input = read_input("input.txt");
    let (mut initial, transformations) = input.split_once("\n\n").unwrap();
    initial = initial.split_once(": ").unwrap().1;
    let transformations = transformations.lines()
        .filter_map(|x| x.split_once(" => "))
        .collect::<HashMap<&str, &str>>();
    let mut state = State::from(initial);
    let mut state2 = State::from(initial);

    let offset = state.evolve(&transformations, 20);
    println!("Part 1: {}", state.total_plants(offset));

    let offset = state2.evolve(&transformations, 50000000000);
    println!("Part 2: {}", state2.total_plants(offset));
}

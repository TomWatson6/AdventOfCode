use std::collections::{HashSet, VecDeque};

#[derive(Clone, PartialEq, Eq, Hash)]
struct State {
    elevator: u8,              // Current floor of the elevator (0-3)
    chips: Vec<u8>,            // Floors of microchips
    generators: Vec<u8>,       // Floors of generators
}

impl State {
    fn is_goal(&self) -> bool {
        self.elevator == 3
            && self.chips.iter().all(|&floor| floor == 3)
            && self.generators.iter().all(|&floor| floor == 3)
    }
}

fn parse_input(input: &str) -> State {
    let mut elements = Vec::new(); // To map element names to indices
    let mut chips = Vec::new();
    let mut generators = Vec::new();

    for (floor_idx, line) in input.lines().enumerate() {
        let line = line.to_lowercase();
        for part in line.split(" a ") {
            if part.contains("microchip") {
                let element = part.split("-compatible microchip").next().unwrap().trim();
                let idx = elements.iter().position(|e| e == element).unwrap_or_else(|| {
                    elements.push(element.to_string());
                    elements.len() - 1
                });
                if idx >= chips.len() {
                    chips.resize(idx + 1, 0);
                }
                chips[idx] = floor_idx as u8;
            } else if part.contains("generator") {
                let element = part.split(" generator").next().unwrap().trim();
                let idx = elements.iter().position(|e| e == element).unwrap_or_else(|| {
                    elements.push(element.to_string());
                    elements.len() - 1
                });
                if idx >= generators.len() {
                    generators.resize(idx + 1, 0);
                }
                generators[idx] = floor_idx as u8;
            }
        }
    }

    State {
        elevator: 0,
        chips,
        generators,
    }
}

use std::collections::hash_map::DefaultHasher;
use std::hash::{Hash, Hasher};

impl State {
    fn canonical_form(&self) -> u64 {
        // Pair chips and generators and sort them to create a canonical form
        let mut pairs: Vec<(u8, u8)> = self.chips.iter().zip(&self.generators).map(|(&c, &g)| (c, g)).collect();
        pairs.sort();
        let mut s = DefaultHasher::new();
        self.elevator.hash(&mut s);
        pairs.hash(&mut s);
        s.finish()
    }
}

impl State {
    fn is_valid(&self) -> bool {
        for floor in 0..4 {
            let mut gens_present = false;
            let mut unprotected_chips = false;

            for (&_chip_floor, &gen_floor) in self.chips.iter().zip(&self.generators) {
                    if gen_floor == floor {
                    gens_present = true;
                }
            }

            for (&chip_floor, &gen_floor) in self.chips.iter().zip(&self.generators) {
                if chip_floor == floor && chip_floor != gen_floor {
                    unprotected_chips = true;
                }
            }

            if unprotected_chips && gens_present {
                return false;
            }
        }
        true
    }
}

fn generate_moves(state: &State) -> Vec<State> {
    let mut next_states = Vec::new();
    let current_floor = state.elevator;
    let mut items_on_floor = Vec::new();

    // Collect indices of items on the current floor
    for (idx, &floor) in state.chips.iter().enumerate() {
        if floor == current_floor {
            items_on_floor.push((idx, true)); // (index, is_chip)
        }
    }
    for (idx, &floor) in state.generators.iter().enumerate() {
        if floor == current_floor {
            items_on_floor.push((idx, false)); // (index, is_chip)
        }
    }

    // Generate combinations of items to move (one or two items)
    let item_combinations = generate_item_combinations(&items_on_floor);

    // Possible directions to move
    let mut directions = Vec::new();
    if current_floor < 3 {
        directions.push(current_floor + 1);
    }
    if current_floor > 0 {
        directions.push(current_floor - 1);
    }

    for &next_floor in &directions {
        for items_to_move in &item_combinations {
            let mut new_state = state.clone();
            new_state.elevator = next_floor;

            for &(idx, is_chip) in items_to_move {
                if is_chip {
                    new_state.chips[idx] = next_floor;
                } else {
                    new_state.generators[idx] = next_floor;
                }
            }

            if new_state.is_valid() {
                next_states.push(new_state);
            }
        }
    }

    next_states
}

fn generate_item_combinations(items: &Vec<(usize, bool)>) -> Vec<Vec<(usize, bool)>> {
    let mut combinations = Vec::new();

    // Move one item
    for &item in items {
        combinations.push(vec![item]);
    }

    // Move two items
    for i in 0..items.len() {
        for j in (i + 1)..items.len() {
            combinations.push(vec![items[i], items[j]]);
        }
    }

    combinations
}

fn bfs(initial_state: State) -> Option<usize> {
    let mut visited = HashSet::new();
    let mut queue = VecDeque::new();

    queue.push_back((initial_state, 0));

    while let Some((state, steps)) = queue.pop_front() {
        let state_key = state.canonical_form();
        if visited.contains(&state_key) {
            continue;
        }
        visited.insert(state_key);

        if state.is_goal() {
            return Some(steps);
        }

        for next_state in generate_moves(&state) {
            queue.push_back((next_state, steps + 1));
        }
    }

    None
}

fn add_additional_items(state: &mut State) {
    // Assume that existing elements are indexed from 0 to N-1
    // New elements will be added at the end
    // Elements to add: "elerium" and "dilithium"

    // Add new chips and generators on the first floor (floor index 0)
    state.chips.push(0);       // Elerium chip
    state.generators.push(0);  // Elerium generator
    state.chips.push(0);       // Dilithium chip
    state.generators.push(0);  // Dilithium generator
}

fn main() {
    let input = include_str!("../input.txt");
    let mut initial_state = parse_input(input);

    // Part 2: Add new elements to the first floor
    add_additional_items(&mut initial_state);

    if let Some(steps) = bfs(initial_state) {
        println!("Minimum number of moves: {}", steps);
    } else {
        println!("No solution found.");
    }
}


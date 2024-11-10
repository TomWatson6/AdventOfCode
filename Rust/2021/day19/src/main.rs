use std::collections::{HashMap, HashSet};

type Point = (i32, i32, i32);

struct Scanner {
    beacons: Vec<Point>,
    position: Option<Point>,     // Position relative to the reference scanner
    orientation: Option<usize>,  // Index of the rotation applied
}

fn parse_input(input: &str) -> Vec<Scanner> {
    let mut scanners = Vec::new();
    for block in input.trim().split("\n\n") {
        let beacons = block
            .lines()
            .skip(1) // Skip the scanner header line
            .map(|line| {
                let coords: Vec<i32> = line.split(',').map(|n| n.parse().unwrap()).collect();
                (coords[0], coords[1], coords[2])
            })
            .collect();
        scanners.push(Scanner {
            beacons,
            position: None,
            orientation: None,
        });
    }
    scanners
}

fn all_rotations(point: &Point) -> Vec<Point> {
    let (x, y, z) = *point;
    vec![
        (x, y, z),
        (x, -z, y),
        (x, -y, -z),
        (x, z, -y),
        (-x, -y, z),
        (-x, -z, -y),
        (-x, y, -z),
        (-x, z, y),
        (y, x, -z),
        (y, -x, z),
        (y, z, x),
        (y, -z, -x),
        (-y, x, z),
        (-y, -x, -z),
        (-y, -z, x),
        (-y, z, -x),
        (z, x, y),
        (z, -x, -y),
        (z, -y, x),
        (z, y, -x),
        (-z, x, -y),
        (-z, -x, y),
        (-z, y, x),
        (-z, -y, -x),
    ]
}

fn align_scanners(scanners: &mut Vec<Scanner>) {
    // Assume scanner 0 is at the origin with no rotation
    scanners[0].position = Some((0, 0, 0));
    scanners[0].orientation = Some(0);

    let mut aligned = vec![0];
    let mut to_align: HashSet<usize> = (1..scanners.len()).collect();

    while !to_align.is_empty() {
        let mut newly_aligned = Vec::new();

        for &i in &aligned {
            for &j in &to_align {
                if let Some((pos, rot)) = match_scanners(&scanners[i], &scanners[j]) {
                    scanners[j].position = Some(pos);
                    scanners[j].orientation = Some(rot);
                    newly_aligned.push(j);
                }
            }
        }

        if newly_aligned.is_empty() {
            panic!("No new scanners could be aligned!");
        }

        for idx in &newly_aligned {
            to_align.remove(idx);
        }
        aligned = newly_aligned;
    }
}

fn match_scanners(s1: &Scanner, s2: &Scanner) -> Option<(Point, usize)> {
    let s1_beacons: HashSet<Point> = s1
        .beacons
        .iter()
        .map(|&p| apply_rotation(p, s1.orientation.unwrap()))
        .map(|p| add_points(p, s1.position.unwrap()))
        .collect();

    for rot_idx in 0..24 {
        let rotated_beacons: Vec<Point> = s2.beacons.iter().map(|&p| apply_rotation(p, rot_idx)).collect();

        let mut deltas = HashMap::new();

        for &p1 in &s1_beacons {
            for &p2 in &rotated_beacons {
                let delta = subtract_points(p1, p2);
                *deltas.entry(delta).or_insert(0) += 1;
            }
        }

        // Check if any delta occurs at least 12 times
        for (delta, count) in deltas {
            if count >= 12 {
                // Found a matching orientation and position
                return Some((delta, rot_idx));
            }
        }
    }

    None
}

fn apply_rotation(point: Point, rot_idx: usize) -> Point {
    all_rotations(&point)[rot_idx]
}

fn add_points(a: Point, b: Point) -> Point {
    (a.0 + b.0, a.1 + b.1, a.2 + b.2)
}

fn subtract_points(a: Point, b: Point) -> Point {
    (a.0 - b.0, a.1 - b.1, a.2 - b.2)
}

fn calculate_results(scanners: &Vec<Scanner>) {
    let mut all_beacons = HashSet::new();

    for scanner in scanners {
        let beacons = scanner
            .beacons
            .iter()
            .map(|&p| {
                let rotated = apply_rotation(p, scanner.orientation.unwrap());
                add_points(rotated, scanner.position.unwrap())
            });
        all_beacons.extend(beacons);
    }

    println!("Total unique beacons: {}", all_beacons.len());

    let positions: Vec<Point> = scanners.iter().map(|s| s.position.unwrap()).collect();

    let max_distance = positions
        .iter()
        .flat_map(|&a| positions.iter().map(move |&b| manhattan_distance(a, b)))
        .max()
        .unwrap();

    println!("Largest Manhattan distance: {}", max_distance);
}

fn manhattan_distance(a: Point, b: Point) -> i32 {
    (a.0 - b.0).abs() + (a.1 - b.1).abs() + (a.2 - b.2).abs()
}

fn main() {
    let input = std::fs::read_to_string("input.txt").expect("Failed to read input file");
    let mut scanners = parse_input(&input);
    align_scanners(&mut scanners);
    calculate_results(&scanners);
}



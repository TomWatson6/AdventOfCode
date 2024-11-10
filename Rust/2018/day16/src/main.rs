use std::fs::File;
use std::io::Read;

fn read_input(file_name: &str) -> (Vec<String>, Vec<String>) {
    let mut file = File::open(file_name).unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    let (top, bottom) = contents.split_once("\n\n\n\n").unwrap();
    (
        top
            .split("\n\n")
            .map(|x| x.to_string())
            .collect::<Vec<String>>(),
        bottom
            .split('\n')
            .map(|x| x.to_string())
            .collect::<Vec<String>>()
    )
}

#[derive(Debug)]
struct Instructions(isize, isize, isize, isize);

impl From<String> for Instructions {
    fn from(value: String) -> Self {
        let parts = value.split(" ")
            .map(|x| x.parse::<isize>().unwrap())
            .collect::<Vec<isize>>();

        Self(parts[0], parts[1], parts[2], parts[3])
    }
}

impl Instructions {
    pub fn new() -> Self {
        Self(0, 0, 0, 0)
    }
}

fn main() {
    let (top, bottom) = read_input("input.txt");
    let instructions: Vec<Instructions> = bottom
        .iter()
        .map(|x| Instructions::from(x.to_string()))
        .collect();
    println!("{:?}", instructions[0]);
}

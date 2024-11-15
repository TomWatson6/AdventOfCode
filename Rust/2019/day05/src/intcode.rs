use std::collections::VecDeque;

pub struct Computer {
    pub code: Vec<isize>,
    pub input_queue: VecDeque<isize>,
    pub outputs: Vec<isize>,
}

impl From<Vec<isize>> for Computer {
    fn from(value: Vec<isize>) -> Self {
        Self {
            code: value,
            input_queue: VecDeque::new(),
            outputs: Vec::new(),
        }
    }
}

impl From<(Vec<isize>, Vec<isize>)> for Computer {
    fn from(value: (Vec<isize>, Vec<isize>)) -> Self {
        Self {
            code: value.0,
            input_queue: VecDeque::from(value.1),
            outputs: Vec::new(),
        }
    }
}

impl Computer {
    pub fn compute(&mut self) -> isize {
        let mut pointer: usize = 0;

        loop {
            match self.code.get(pointer) {
                Some(mut x) => {
                    let opcode = x.to_string();
                    let modes: Vec<isize> = if opcode.len() > 2 { 
                        opcode[..opcode.len()-2]
                            .to_string()
                            .chars()
                            .map(|n| n.to_string().parse::<isize>().unwrap())
                            .collect::<Vec<isize>>()
                    } else {
                        Vec::new()
                    };

                    let mut op = *x;

                    if opcode.len() > 2 {
                        op = opcode[opcode.len() - 2..].parse().unwrap();
                    }

                    match op {
                        1 => {
                            let params = self.parse_params(modes, VecDeque::from(self.code[pointer + 1..pointer + 3].to_vec()));
                            let output = self.get(Parameter::from((0, (pointer + 3) as isize)));
                            self.code[output as usize] = self.add(params);
                            pointer += 4;
                        },
                        2 => {
                            let params = self.parse_params(modes, VecDeque::from(self.code[pointer + 1..pointer + 3].to_vec()));
                            let output = self.get(Parameter::from((0, (pointer + 3) as isize)));
                            self.code[output as usize] = self.mult(params);
                            pointer += 4;
                        },
                        3 => {
                            let output = self.get(Parameter::from((0, (pointer + 1) as isize)));
                            self.code[output as usize] = self.input();
                            pointer += 2;
                        },
                        4 => {
                            let params = self.parse_params(modes, VecDeque::from(self.code[pointer + 1..pointer + 2].to_vec()));
                            let output = self.output(params);
                            self.outputs.push(output);

                            pointer += 2;
                        },
                        5 => {
                            let params = self.parse_params(modes, VecDeque::from(self.code[pointer + 1..pointer + 3].to_vec()));
                            let dest = self.jump_if_true(params);
                            let output = self.get(Parameter::from((0, (pointer + 2) as isize)));
                            if dest != 0 {
                                pointer = dest as usize;
                            } else {
                                pointer += 3;
                            }
                        }
                        6 => {
                            let params = self.parse_params(modes, VecDeque::from(self.code[pointer + 1..pointer + 3].to_vec()));
                            let dest = self.jump_if_false(params);
                            let output = self.get(Parameter::from((0, (pointer + 2) as isize)));
                            if dest != 0 {
                                pointer = dest as usize;
                            } else {
                                pointer += 3;
                            }
                        }
                        7 => {
                            let params = self.parse_params(modes, VecDeque::from(self.code[pointer + 1..pointer + 3].to_vec()));
                            let value = self.less_than(params);
                            let output = self.get(Parameter::from((0, (pointer + 3) as isize)));
                            self.code[output as usize] = value;

                            pointer += 4;
                        }
                        8 => {
                            let params = self.parse_params(modes, VecDeque::from(self.code[pointer + 1..pointer + 3].to_vec()));
                            let value = self.equals(params);
                            let output = self.get(Parameter::from((0, (pointer + 3) as isize)));
                            self.code[output as usize] = value;

                            pointer += 4;
                        }
                        99 => break,
                        _ => panic!("Invalid opcode: {}", x),
                    }
                },
                None => panic!("Opcode not found"),
            }
        }

        self.code[0]
    }

    fn get(&self, param: Parameter) -> isize {
        match param.mode {
            ParamMode::Position => match self.code.get(param.value as usize) {
                Some(x) => *x,
                _ => panic!("Value not found at position: {}", param.value),
            },
            ParamMode::Immediate => param.value,
        }
    }

    fn parse_params(&self, mut modes: Vec<isize>, mut operands: VecDeque<isize>) -> Vec<Parameter> {
        let mut params: Vec<Parameter> = Vec::new();

        while let Some(x) = operands.pop_front() {
            params.push(Parameter::from((modes.pop().unwrap_or(0), x)))
        }

        params
    }

    fn add(&mut self, params: Vec<Parameter>) -> isize {
        assert_eq!(2, params.len());

        let a = self.get(*params.first().unwrap());
        let b = self.get(*params.last().unwrap());

        a + b
    }

    fn mult(&mut self, params: Vec<Parameter>) -> isize {
        assert_eq!(2, params.len());

        let a = self.get(*params.first().unwrap());
        let b = self.get(*params.last().unwrap());

        a * b
    }

    fn input(&mut self) -> isize {
        self.input_queue.pop_front().expect("No input left on input queue")
    }

    fn output(&self, params: Vec<Parameter>) -> isize {
        assert_eq!(1, params.len());

        self.get(*params.first().unwrap())
    }

    fn jump_if_true(&self, params: Vec<Parameter>) -> isize {
        assert_eq!(2, params.len());

        let check = self.get(*params.first().unwrap());
        let value = self.get(*params.last().unwrap());

        if check != 0 {
            value
        } else {
            0
        }
    }

    fn jump_if_false(&self, params: Vec<Parameter>) -> isize {
        assert_eq!(2, params.len());

        let check = self.get(*params.first().unwrap());
        let value = self.get(*params.last().unwrap());

        if check == 0 {
            value
        } else {
            0
        }
    }

    fn less_than(&self, params: Vec<Parameter>) -> isize {
        assert_eq!(2, params.len());

        let left = self.get(*params.first().unwrap());
        let right = self.get(*params.last().unwrap());

        if left < right {
            1
        } else {
            0
        }
    }

    fn equals(&self, params: Vec<Parameter>) -> isize {
        assert_eq!(2, params.len());

        let left = self.get(*params.first().unwrap());
        let right = self.get(*params.last().unwrap());

        if left == right {
            1
        } else {
            0
        }
    }
}

#[derive(Copy, Clone, Debug)]
pub struct Parameter {
    mode: ParamMode,
    value: isize,
}

impl From<(isize, isize)> for Parameter {
    fn from(value: (isize, isize)) -> Self {
        let param_mode = match value.0 {
            0 => ParamMode::Position,
            1 => ParamMode::Immediate,
            _ => panic!("Invalid param mode supplied"),
        };

        Self {
            mode: param_mode,
            value: value.1,
        }
    }
}

#[derive(Copy, Clone, Debug)]
enum ParamMode {
    Position,
    Immediate,
}


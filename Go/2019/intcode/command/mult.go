package command

import "fmt"

type Mult struct {
	length int
}

func NewMult() Mult {
	return Mult{length: 4}
}

func (m Mult) Run(ptr *int, program []int) error {
	if *ptr+m.length >= len(program) {
		return fmt.Errorf("program has run off the end of the tape")
	}

	first := program[*ptr+1]
	second := program[*ptr+2]
	third := program[*ptr+3]

	num1 := program[first]
	num2 := program[second]

	program[third] = num1 * num2

	(*ptr) += m.length

	return nil
}

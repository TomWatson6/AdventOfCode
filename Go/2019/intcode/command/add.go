package command

import "fmt"

type Add struct {
	length int
}

func NewAdd() Add {
	return Add{length: 4}
}

func (a Add) Run(ptr *int, program []int) error {
	if *ptr+a.length >= len(program) {
		return fmt.Errorf("program has run off the end of the tape")
	}

	first := program[*ptr+1]
	second := program[*ptr+2]
	third := program[*ptr+3]

	num1 := program[first]
	num2 := program[second]

	program[third] = num1 + num2

	(*ptr) += a.length

	return nil
}

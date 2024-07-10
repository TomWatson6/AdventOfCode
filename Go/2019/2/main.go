package main

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/TomWatson6/AdventOfCode/Go/2019/intcode"
	"github.com/TomWatson6/AdventOfCode/Go/2019/utils"
)

func main() {
	program, err := readCodes("input.txt")
	if err != nil {
		panic(err)
	}

	programCopy := append([]int{}, program...)

	program[1] = 12
	program[2] = 2

	computer := intcode.New(program)
	err = computer.Run()
	if err != nil {
		panic(err)
	}

	fmt.Printf("Part 1: %d\n", computer.Program[0])

outer:
	for a := 0; a < 100; a++ {
		for b := 0; b < 100; b++ {
			program = append([]int{}, programCopy...)

			program[1] = a
			program[2] = b

			computer = intcode.New(program)
			err = computer.Run()
			if err != nil {
				panic(err)
			}

			if computer.Program[0] == 19690720 {
				fmt.Printf("Part 2: %d\n", a*100+b)
				break outer
			}
		}
	}
}

func readCodes(fileName string) ([]int, error) {
	input, err := utils.ReadFile(fileName)
	if err != nil {
		return nil, err
	}

	parts := strings.Split(input, ",")
	codes := []int{}

	for _, part := range parts {
		code, err := strconv.Atoi(part)
		if err != nil {
			return nil, err
		}

		codes = append(codes, code)
	}

	return codes, nil
}

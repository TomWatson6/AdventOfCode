package main

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/TomWatson6/AdventOfCode/Go/2019/utils"
)

func main() {
	file, err := utils.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}

	parts := strings.Split(file, ",")
	program := []int{}

	for _, p := range parts {
		val, err := strconv.Atoi(p)
		if err != nil {
			panic(err)
		}

		program = append(program, val)
	}

	fmt.Printf("Program: %v\n", program)
}

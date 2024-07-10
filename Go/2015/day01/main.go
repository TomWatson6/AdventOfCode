package main

import (
	"fmt"
	"os"
)

func getInput(fileName string) string {
	bytes, err := os.ReadFile(fileName)
	if err != nil {
		panic(err)
	}

	return string(bytes)
}

func part1(input string) {
	floor := 0

	for _, char := range input {
		if char == '(' {
			floor += 1
		} else {
			floor -= 1
		}
	}

	fmt.Printf("Part 1: %d\n", floor)
}

func part2(input string) {
	floor := 0
	counter := 0

	for floor >= 0 {
		if input[counter] == '(' {
			floor += 1
		} else {
			floor -= 1
		}

		counter += 1
	}

	fmt.Printf("Part 2: %d\n", counter)
}

func main() {
	input := getInput("input.txt")
	part1(input)
	part2(input)
}

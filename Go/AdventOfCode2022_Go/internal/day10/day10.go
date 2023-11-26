package day10

import (
	"strconv"
	"strings"

	"github.com/tomwatson6/AdventOfCode2022_Go/pkg/input"
	"github.com/tomwatson6/AdventOfCode2022_Go/pkg/util"
)

func Part1(fileName string) (int, error) {
	i, err := input.ReadFile(fileName)
	if err != nil {
		return 0, err
	}

	lines := input.GetLines(i)
	var signals []int
	strength := 1
	cycle := 0
	counter := 0

	for len(signals) < 6 {
		line := lines[counter%len(lines)]
		cycle += 1

		for i := 20; i <= 220; i += 40 {
			if cycle == i {
				signals = append(signals, cycle*strength)
			}
		}

		if line == "noop" {
			counter += 1
			continue
		}

		cycle += 1

		for i := 20; i <= 220; i += 40 {
			if cycle == i {
				signals = append(signals, cycle*strength)
			}
		}

		parts := strings.Split(line, " ")
		mag, err := strconv.Atoi(parts[1])
		if err != nil {
			return 0, err
		}

		strength += mag
		counter += 1
	}

	total := 0

	for _, signal := range signals {
		total += signal
	}

	return total, nil
}

func Part2(fileName string) (string, error) {
	i, err := input.ReadFile(fileName)
	if err != nil {
		return "", err
	}

	lines := input.GetLines(i)
	crt := map[util.Coord]bool{}
	position := 1
	cycle := -1
	counter := 0

	for cycle <= 240 {
		line := lines[counter%len(lines)]
		cycle += 1

		if position-1 <= cycle%40 && cycle%40 <= position+1 {
			crt[util.Coord{X: cycle % 40, Y: cycle / 40}] = true
		}

		if line == "noop" {
			counter += 1
			continue
		}

		cycle += 1

		if position-1 <= cycle%40 && cycle%40 <= position+1 {
			crt[util.Coord{X: cycle % 40, Y: cycle / 40}] = true
		}

		parts := strings.Split(line, " ")
		mag, err := strconv.Atoi(parts[1])
		if err != nil {
			return "", err
		}

		position += mag
		counter += 1
	}

	output := ""

	for y := 0; y < 6; y++ {
		for x := 0; x < 40; x++ {
			if _, ok := crt[util.Coord{X: x, Y: y}]; ok {
				output += "#"
			} else {
				output += " "
			}
		}

		output += "\n"
	}

	return output, nil
}

package day2

import (
	"strings"

	"github.com/tomwatson6/AdventOfCode2022_Go/pkg/input"
)

const (
	Rock int = iota + 1
	Paper
	Scissors
)

var moveMap = map[string]int{
	"A": Rock,
	"B": Paper,
	"C": Scissors,
	"X": Rock,
	"Y": Paper,
	"Z": Scissors,
}

var outcomeMap = map[string]int{
	"X": 0,
	"Y": 3,
	"Z": 6,
}

var responseMap = map[string]map[string]int{
	"X": {
		"A": Scissors,
		"B": Rock,
		"C": Paper,
	},
	"Y": {
		"A": Rock,
		"B": Paper,
		"C": Scissors,
	},
	"Z": {
		"A": Paper,
		"B": Scissors,
		"C": Rock,
	},
}

func Part1(fileName string) (int, error) {
	i, err := input.ReadFile(fileName)
	if err != nil {
		return 0, err
	}

	lines := input.GetLines(i)
	score := 0

	for _, line := range lines {
		moves := strings.Split(line, " ")
		out := outcome(moves[1], moves[0])
		score += moveMap[moves[1]] + out
	}

	return score, nil
}

func Part2(fileName string) (int, error) {
	i, err := input.ReadFile(fileName)
	if err != nil {
		return 0, err
	}

	lines := input.GetLines(i)
	score := 0

	for _, line := range lines {
		moves := strings.Split(line, " ")
		resp := responseMap[moves[1]][moves[0]]
		out := outcomeMap[moves[1]]
		score += resp + out
	}

	return score, nil
}

func outcome(p1, p2 string) int {
	m1 := moveMap[p1]
	m2 := moveMap[p2]

	switch {
	case m1 == m2:
		return 3
	case m1 == Rock && m2 == Scissors:
		return 6
	case m1 == Scissors && m2 == Paper:
		return 6
	case m1 == Paper && m2 == Rock:
		return 6
	default:
		return 0
	}
}

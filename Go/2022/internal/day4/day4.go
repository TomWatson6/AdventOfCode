package day4

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

	pairs, err := parseInput(lines)
	if err != nil {
		return 0, err
	}

	total := 0

	for _, pair := range pairs {
		if pair[0].Upper-pair[0].Lower >= pair[1].Upper-pair[1].Lower {
			if Contains(pair[0], pair[1]) {
				total += 1
			}
		} else {
			if Contains(pair[1], pair[0]) {
				total += 1
			}
		}
	}

	return total, nil
}

func Part2(fileName string) (int, error) {
	i, err := input.ReadFile(fileName)
	if err != nil {
		return 0, err
	}

	lines := input.GetLines(i)

	pairs, err := parseInput(lines)
	if err != nil {
		return 0, err
	}

	total := 0

	for _, pair := range pairs {
		if Overlaps(pair[0], pair[1]) {
			total += 1
		}
	}

	return total, nil
}

func Contains(left, right util.Bounds) bool {
	return right.Lower >= left.Lower && right.Upper <= left.Upper
}

func Overlaps(left, right util.Bounds) bool {
	return !(left.Lower > right.Upper || right.Lower > left.Upper)
}

func parseInput(lines []string) ([][]util.Bounds, error) {
	var pairs [][]util.Bounds

	for _, line := range lines {
		pair, err := parseLine(line)
		if err != nil {
			return pairs, err
		}

		pairs = append(pairs, pair)
	}

	return pairs, nil
}

func parseLine(line string) ([]util.Bounds, error) {
	var bounds []util.Bounds
	split := strings.Split(line, ",")

	for _, elem := range split {
		parts := strings.Split(elem, "-")

		lower, err := strconv.Atoi(parts[0])
		if err != nil {
			return bounds, err
		}

		upper, err := strconv.Atoi(parts[1])
		if err != nil {
			return bounds, err
		}

		bounds = append(bounds, util.Bounds{Lower: lower, Upper: upper})
	}

	return bounds, nil
}

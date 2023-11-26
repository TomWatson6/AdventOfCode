package day3

import (
	"fmt"
	"unicode"

	"github.com/tomwatson6/AdventOfCode2022_Go/pkg/input"
)

func Part1(fileName string) (int, error) {
	i, err := input.ReadFile(fileName)
	if err != nil {
		return 0, err
	}

	lines := input.GetLines(i)

	total := 0

	for _, line := range lines {
		common := Intersection(line[:len(line)/2], line[len(line)/2:])
		priority := Priority(common)
		total += priority
	}

	return total, nil
}

func Part2(fileName string) (int, error) {
	i, err := input.ReadFile(fileName)
	if err != nil {
		return 0, err
	}

	lines := input.GetLines(i)

	if len(lines)%3 != 0 {
		return 0, fmt.Errorf("incorrect number of rucksacks to be divided into groups of 3 elves")
	}

	total := 0

	for i := 0; i < len(lines); i += 3 {
		group := []string{
			lines[i],
			lines[i+1],
			lines[i+2],
		}

		common, err := CommonItem(group)
		if err != nil {
			return 0, err
		}

		priority := Priority(common)
		total += priority
	}

	return total, nil
}

func Intersection(left, right string) rune {
	seen := map[rune]bool{}

	for _, c := range left {
		seen[c] = true
	}

	for _, c := range right {
		if _, ok := seen[c]; ok {
			return c
		}
	}

	return 0
}

func CommonItem(rucksacks []string) (rune, error) {
	seen := map[rune]int{}

	for _, rucksack := range rucksacks {
		currSeen := map[rune]bool{}

		for _, c := range rucksack {
			if _, ok := currSeen[c]; !ok {
				seen[c] += 1
			}

			currSeen[c] = true
		}
	}

	var mostCommon []rune

	for k, v := range seen {
		if v == len(rucksacks) {
			mostCommon = append(mostCommon, k)
		}
	}

	if len(mostCommon) > 1 {
		return 0, fmt.Errorf("more than 1 item that appears in all rucksacks: %v", mostCommon)
	}

	if len(mostCommon) == 0 {
		return 0, fmt.Errorf("no common item found across the rucksacks provided")
	}

	return mostCommon[0], nil
}

func Priority(char rune) int {
	if unicode.IsLower(char) {
		return int(char) - 96
	} else {
		return int(char) - 38
	}
}

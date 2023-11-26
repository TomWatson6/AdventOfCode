package day1

import (
	"sort"
	"strconv"

	"github.com/tomwatson6/AdventOfCode2022_Go/pkg/input"
)

func Part1(fileName string) (int, error) {
	fileString, err := input.ReadFile(fileName)
	if err != nil {
		return 0, err
	}

	elves := input.GetLines(fileString)

	calories := getCalories(elves)
	largest := 0

	for _, num := range calories {
		if num > largest {
			largest = num
		}
	}

	return largest, nil
}

func Part2(fileName string) (int, error) {
	fileString, err := input.ReadFile(fileName)
	if err != nil {
		return 0, err
	}

	elves := input.GetLines(fileString)

	calories := getCalories(elves)
	sort.Ints(calories)

	largest := 0

	for _, elf := range calories[len(calories)-3:] {
		largest += elf
	}

	return largest, nil
}

func getCalories(elves []string) []int {
	var calories []int
	curr := 0

	for _, elf := range elves {
		elfNum, err := strconv.Atoi(elf)
		if err != nil {
			calories = append(calories, curr)
			curr = 0
			continue
		}

		curr += elfNum
	}

	calories = append(calories, curr)

	return calories
}

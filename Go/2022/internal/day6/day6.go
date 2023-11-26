package day6

import "github.com/tomwatson6/AdventOfCode2022_Go/pkg/input"

func Part1(fileName string) (int, error) {
	i, err := input.ReadFile(fileName)
	if err != nil {
		return 0, err
	}

	marker := FindMarker(i, 4)

	return marker, nil
}

func Part2(fileName string) (int, error) {
	i, err := input.ReadFile(fileName)
	if err != nil {
		return 0, err
	}

	marker := FindMarker(i, 14)

	return marker, nil
}

func FindMarker(input string, uniqueChars int) int {
	for i := 0; i < len(input)-uniqueChars+1; i++ {
		slice := input[i : i+uniqueChars]
		chars := map[rune]bool{}

		for _, c := range slice {
			chars[c] = true
		}

		if len(slice) == len(chars) {
			return i + uniqueChars
		}
	}

	return 0
}

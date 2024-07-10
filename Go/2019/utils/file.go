package utils

import (
	"os"
	"strconv"
	"strings"
)

func ReadFile(fileName string) (string, error) {
	data, err := os.ReadFile(fileName)
	if err != nil {
		return "", err
	}

	return string(data), nil
}

func ReadLines(fileName string) ([]string, error) {
	text, err := ReadFile(fileName)
	if err != nil {
		return nil, err
	}

	var lines []string
	splitLines := strings.Split(text, "\n")

	for _, line := range splitLines {
		line = strings.Trim(line, "\r")
		lines = append(lines, line)
	}

	return lines, nil
}

func ReadNumbers(fileName string) ([]int, error) {
	lines, err := ReadLines(fileName)
	if err != nil {
		return nil, err
	}

	nums := []int{}

	for _, line := range lines {
		num, err := strconv.Atoi(line)
		if err != nil {
			return nil, err
		}

		nums = append(nums, num)
	}

	return nums, nil
}

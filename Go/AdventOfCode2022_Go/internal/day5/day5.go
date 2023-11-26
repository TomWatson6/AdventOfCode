package day5

import (
	"strings"

	"github.com/tomwatson6/AdventOfCode2022_Go/pkg/input"
	"github.com/tomwatson6/AdventOfCode2022_Go/pkg/util"
)

func Part1(fileName string) (string, error) {
	stacks, instructions, err := getInput(fileName)
	if err != nil {
		return "", err
	}

	for _, ins := range instructions {
		parts := strings.Split(ins, " ")
		partsStr := []string{parts[1], parts[3], parts[5]}
		nums, err := input.ToIntArray(partsStr)
		if err != nil {
			return "", err
		}

		Transfer(&stacks, nums[0], nums[1]-1, nums[2]-1, false)
	}

	output := ""

	for _, s := range stacks {
		output += string(s[len(s)-1])
	}

	return output, nil
}

func Part2(fileName string) (string, error) {
	stacks, instructions, err := getInput(fileName)
	if err != nil {
		return "", err
	}

	for _, ins := range instructions {
		parts := strings.Split(ins, " ")
		partsStr := []string{parts[1], parts[3], parts[5]}
		nums, err := input.ToIntArray(partsStr)
		if err != nil {
			return "", err
		}

		Transfer(&stacks, nums[0], nums[1]-1, nums[2]-1, true)
	}

	output := ""

	for _, s := range stacks {
		output += string(s[len(s)-1])
	}

	return output, nil
}

func Transfer(stacks *[]util.Stack[rune], quantity, from, to int, retainOrder bool) error {
	var temp []rune

	for i := 0; i < quantity; i++ {
		item, err := (*stacks)[from].Pop()
		if err != nil {
			return err
		}

		temp = append(temp, *item)
	}

	if retainOrder {
		var temp2 util.Stack[rune]
		for i := len(temp) - 1; i >= 0; i-- {
			temp2 = append(temp2, temp[i])
		}
		temp = temp2
	}

	for _, t := range temp {
		(*stacks)[to].Push(t)
	}

	return nil
}

func getInput(fileName string) ([]util.Stack[rune], []string, error) {
	i, err := input.ReadFile(fileName)
	if err != nil {
		return nil, []string{}, err
	}

	i = strings.ReplaceAll(i, "\r", "")
	split := strings.Split(i, "\n\n")
	top := strings.Split(split[0], "\n")
	top = top[:len(top)-1]
	instructions := strings.Split(split[1], "\n")

	var rows [][]rune

	for _, line := range top {
		var row []rune

		for i := 1; i < len(line); i += 4 {
			row = append(row, []rune(line)[i])
		}

		rows = append(rows, row)
	}

	var stacks []util.Stack[rune]

	for x := 0; x < len(rows[0]); x++ {
		var stack util.Stack[rune]

		for y := len(rows) - 1; y >= 0; y-- {
			if rows[y][x] == ' ' {
				break
			}

			stack.Push(rows[y][x])
		}

		stacks = append(stacks, stack)
	}

	return stacks, instructions, nil
}

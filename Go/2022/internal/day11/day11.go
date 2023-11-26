package day11

import (
	"sort"
	"strings"

	"github.com/tomwatson6/AdventOfCode2022_Go/pkg/input"
)

func Part1(fileName string) (int, error) {
	return evolve(fileName, false, 20)
}

func Part2(fileName string) (int, error) {
	return evolve(fileName, true, 10000)
}

func evolve(fileName string, part2 bool, rounds int) (int, error) {
	i, err := input.ReadFile(fileName)
	if err != nil {
		return 0, err
	}

	sections := strings.Split(i, "\r\n\r\n")
	var monkeys []Monkey

	for _, section := range sections {
		monkey, err := NewMonkey(section)
		if err != nil {
			return 0, err
		}

		monkeys = append(monkeys, monkey)
	}

	lcm := 1

	for _, m := range monkeys {
		lcm *= m.DivisibleBy
	}

	var activity []int

	for i := 0; i < len(monkeys); i++ {
		activity = append(activity, 0)
	}

	for round := 0; round < rounds; round++ {
		for i := 0; i < len(monkeys); i++ {
			items := len(monkeys[i].Items)
			activity[i] += items

			for j := 0; j < items; j++ {
				err := monkeys[i].Inspect(monkeys, part2, lcm)
				if err != nil {
					return 0, err
				}
			}
		}
	}

	sort.Ints(activity)

	return activity[len(activity)-2] * activity[len(activity)-1], nil
}

package day11

import (
	"errors"
	"strconv"
	"strings"

	"github.com/tomwatson6/AdventOfCode2022_Go/pkg/input"
)

var (
	// ErrorNoMoreItems is thrown when the current monkey has no more items
	ErrorNoMoreItems = errors.New("monkey has no more items")
)

type Monkey struct {
	Items                   []int
	Operation               []string
	DivisibleBy             int
	MonkeyTrue, MonkeyFalse int
}

func NewMonkey(details string) (Monkey, error) {
	var monkey Monkey
	lines := input.GetLines(details)

	for i := 0; i < len(lines); i++ {
		lines[i] = strings.TrimLeft(lines[i], " ")
	}

	split := strings.Split(lines[1], " ")[2:]
	var items []int

	for _, s := range split {
		val, err := strconv.Atoi(strings.Trim(s, ","))
		if err != nil {
			return monkey, err
		}

		items = append(items, val)
	}

	monkey.Items = items

	split = strings.Split(lines[2], " ")
	monkey.Operation = split[len(split)-3:]

	split = strings.Split(lines[3], " ")
	val, err := strconv.Atoi(split[len(split)-1])
	if err != nil {
		return monkey, err
	}
	monkey.DivisibleBy = val

	split = strings.Split(lines[4], " ")
	val, err = strconv.Atoi(split[len(split)-1])
	if err != nil {
		return monkey, err
	}
	monkey.MonkeyTrue = val

	split = strings.Split(lines[5], " ")
	val, err = strconv.Atoi(split[len(split)-1])
	if err != nil {
		return monkey, err
	}
	monkey.MonkeyFalse = val

	return monkey, nil
}

func (m *Monkey) Inspect(monkeys []Monkey, part2 bool, lcm int) error {
	if len(m.Items) == 0 {
		return ErrorNoMoreItems
	}

	outcome, err := m.DoOperation(part2)
	if err != nil {
		return err
	}

	if outcome%m.DivisibleBy != 0 {
		monkeys[m.MonkeyFalse].Items = append(monkeys[m.MonkeyFalse].Items, outcome%lcm)
	} else {
		monkeys[m.MonkeyTrue].Items = append(monkeys[m.MonkeyTrue].Items, outcome%lcm)
	}

	m.Items = append([]int{}, m.Items[1:]...)

	return nil
}

func (m Monkey) DoOperation(part2 bool) (int, error) {
	var left int

	if m.Operation[0] == "old" {
		left = m.Items[0]
	} else {
		val, err := strconv.Atoi(m.Operation[0])
		if err != nil {
			return 0, err
		}
		left = val
	}

	var right int

	if m.Operation[2] == "old" {
		right = m.Items[0]
	} else {
		val, err := strconv.Atoi(m.Operation[2])
		if err != nil {
			return 0, err
		}
		right = val
	}

	if m.Operation[1] == "+" {
		if part2 {
			return left + right, nil
		} else {
			return (left + right) / 3, nil
		}
	} else {
		if part2 {
			return left * right, nil
		} else {
			return (left * right) / 3, nil
		}
	}
}

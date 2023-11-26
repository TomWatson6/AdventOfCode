package day8

import (
	"sort"
	"strconv"

	"github.com/tomwatson6/AdventOfCode2022_Go/pkg/input"
	"github.com/tomwatson6/AdventOfCode2022_Go/pkg/util"
)

func Part1(fileName string) (int, error) {
	i, err := input.ReadFile(fileName)
	if err != nil {
		return 0, err
	}

	lines := input.GetLines(i)
	grid, XS, YS, err := ParseInput(lines)
	if err != nil {
		return 0, err
	}

	total := 0

	for y := 0; y < YS; y++ {
		for x := 0; x < XS; x++ {
			if IsVisible(grid, util.Coord{X: x, Y: y}, XS, YS) {
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
	grid, XS, YS, err := ParseInput(lines)
	if err != nil {
		return 0, err
	}

	var scores []int

	for y := 0; y < YS; y++ {
		for x := 0; x < XS; x++ {
			scores = append(scores, GetScenicScore(grid, util.Coord{X: x, Y: y}, XS, YS))
		}
	}

	sort.Ints(scores)

	return scores[len(scores)-1], nil
}

func IsVisible(grid map[util.Coord]int, coord util.Coord, XS, YS int) bool {
	dirs := []util.Coord{
		{X: 0, Y: 1},  // DOWN
		{X: 0, Y: -1}, // UP
		{X: 1, Y: 0},  // RIGHT
		{X: -1, Y: 0}, // LEFT
	}

	for _, dir := range dirs {
		curr := coord
		curr.Add(dir)
		visible := true

		for curr.X >= 0 && curr.X < XS && curr.Y >= 0 && curr.Y < YS {
			if grid[curr] >= grid[coord] {
				visible = false
				break
			}

			curr.Add(dir)
		}

		if visible {
			return true
		}
	}

	return false
}

func GetScenicScore(grid map[util.Coord]int, coord util.Coord, XS, YS int) int {
	dirs := []util.Coord{
		{X: 0, Y: 1},  // DOWN
		{X: 0, Y: -1}, // UP
		{X: 1, Y: 0},  // RIGHT
		{X: -1, Y: 0}, // LEFT
	}

	var toMult []int

	for _, dir := range dirs {
		curr := coord
		curr.Add(dir)
		trees := 0

		for curr.X >= 0 && curr.X < XS && curr.Y >= 0 && curr.Y < YS {
			trees += 1
			if grid[curr] >= grid[coord] {
				break
			}

			curr.Add(dir)
		}

		toMult = append(toMult, trees)
	}

	product := 1

	for _, mult := range toMult {
		product *= mult
	}

	return product
}

func ParseInput(lines []string) (map[util.Coord]int, int, int, error) {
	grid := map[util.Coord]int{}
	XS := len(lines[0])
	YS := len(lines)

	for y, line := range lines {
		for x := 0; x < len(line); x++ {
			val, err := strconv.Atoi(string([]rune(line)[x]))
			if err != nil {
				return grid, 0, 0, err
			}

			grid[util.Coord{X: x, Y: y}] = val
		}
	}

	return grid, XS, YS, nil
}

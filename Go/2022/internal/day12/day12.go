package day12

import (
	"math"
	"sort"

	"github.com/tomwatson6/AdventOfCode2022_Go/pkg/algo"
	"github.com/tomwatson6/AdventOfCode2022_Go/pkg/input"
	"github.com/tomwatson6/AdventOfCode2022_Go/pkg/util"
)

func Part1(fileName string) (int, error) {
	i, err := input.ReadFile(fileName)
	if err != nil {
		return 0, err
	}

	lines := input.GetLines(i)

	grid := map[util.Coord]int{}
	var start util.Coord
	var goal util.Coord

	for y := 0; y < len(lines); y++ {
		for x := 0; x < len(lines[0]); x++ {
			c := util.Coord{X: x, Y: y}
			curr := []rune(lines[y])[x]

			if curr == 'S' {
				start = c
			}

			if curr == 'E' {
				goal = c
			}

			grid[c] = int([]rune(lines[y])[x])
		}
	}

	XS := len(lines[0])
	YS := len(lines)

	heuristic := func(grid map[util.Coord]int, c, dest util.Coord) int {
		h := math.Abs(float64(dest.X-c.X)) + math.Abs(float64(dest.Y-c.Y))

		var start int
		if grid[c] == 'S' {
			start = 97
		}

		var finish int
		if grid[dest] == 'E' {
			finish = 122
		}

		diff := finish - start

		if diff > int(h) {
			return diff
		}

		return int(h)
	}

	possible := func(grid map[util.Coord]int, c, dest util.Coord) bool {
		from := grid[c]
		to := grid[dest]

		if from == 'S' {
			return to == 'a'
		}

		if to == 'E' {
			return from == 'z' || from == 'y'
		}

		return to-from <= 1
	}

	weight := func(grid map[util.Coord]int, c, dest util.Coord) int {
		return 1
	}

	info := algo.AStarInfo{
		Grid:      grid,
		XS:        XS,
		YS:        YS,
		Start:     start,
		Goal:      goal,
		Heuristic: heuristic,
		Possible:  possible,
		Weight:    weight,
	}

	path := algo.AStar(info)

	pathSet := util.NewFromSlice(path)

	return len(pathSet) - 1, nil
}

func Part2(fileName string) (int, error) {
	i, err := input.ReadFile(fileName)
	if err != nil {
		return 0, err
	}

	lines := input.GetLines(i)

	grid := map[util.Coord]int{}
	var goal util.Coord

	for y := 0; y < len(lines); y++ {
		for x := 0; x < len(lines[0]); x++ {
			c := util.Coord{X: x, Y: y}
			curr := []rune(lines[y])[x]

			if curr == 'E' {
				goal = c
			}

			grid[c] = int([]rune(lines[y])[x])
		}
	}

	XS := len(lines[0])
	YS := len(lines)

	heuristic := func(grid map[util.Coord]int, c, dest util.Coord) int {
		h := math.Abs(float64(dest.X-c.X)) + math.Abs(float64(dest.Y-c.Y))

		diff := grid[dest] - grid[c]

		if diff > int(h) {
			return diff
		}

		return int(h)
	}

	possible := func(grid map[util.Coord]int, c, dest util.Coord) bool {
		from := grid[c]
		to := grid[dest]

		if from == 'S' {
			return to == 'a'
		}

		if to == 'E' {
			return from == 'z' || from == 'y'
		}

		return to-from <= 1
	}

	weight := func(grid map[util.Coord]int, c, dest util.Coord) int {
		return 1
	}

	lengths := []int{}

	for coord, val := range grid {
		if val == 'a' {
			info := algo.AStarInfo{
				Grid:      grid,
				XS:        XS,
				YS:        YS,
				Start:     coord,
				Goal:      goal,
				Heuristic: heuristic,
				Possible:  possible,
				Weight:    weight,
			}

			path := algo.AStar(info)
			if len(path) != 0 {
				lengths = append(lengths, len(path))
			}
		}
	}

	sort.Ints(lengths)

	return lengths[0] - 1, nil
}

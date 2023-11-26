package day9

import (
	"math"
	"strconv"
	"strings"

	"github.com/tomwatson6/AdventOfCode2022_Go/pkg/input"
	"github.com/tomwatson6/AdventOfCode2022_Go/pkg/util"
)

type Move struct {
	Dir string
	Mag int
}

var Directions = map[string]util.Coord{
	"U": {X: 0, Y: -1},
	"D": {X: 0, Y: 1},
	"L": {X: -1, Y: 0},
	"R": {X: 1, Y: 0},
}

func Part1(fileName string) (int, error) {
	i, err := input.ReadFile(fileName)
	if err != nil {
		return 0, err
	}

	lines := input.GetLines(i)
	moves, err := ParseInput(lines)
	if err != nil {
		return 0, err
	}

	visited := map[util.Coord]bool{}

	head := util.Coord{X: 0, Y: 0}
	tail := util.Coord{X: 0, Y: 0}

	for _, move := range moves {
		for i := 0; i < move.Mag; i++ {
			head = util.Coord{X: head.X + Directions[move.Dir].X, Y: head.Y + Directions[move.Dir].Y}
			tail = Trail(head, tail)
			visited[tail] = true
		}
	}

	return len(visited), nil
}

func Part2(fileName string) (int, error) {
	i, err := input.ReadFile(fileName)
	if err != nil {
		return 0, err
	}

	lines := input.GetLines(i)
	moves, err := ParseInput(lines)
	if err != nil {
		return 0, err
	}

	visited := map[util.Coord]bool{}

	var rope []util.Coord

	for i := 0; i < 10; i++ {
		rope = append(rope, util.Coord{X: 0, Y: 0})
	}

	for _, move := range moves {
		for i := 0; i < move.Mag; i++ {
			rope[0] = util.Coord{X: rope[0].X + Directions[move.Dir].X, Y: rope[0].Y + Directions[move.Dir].Y}
			for j := 0; j < len(rope)-1; j++ {
				rope[j+1] = Trail(rope[j], rope[j+1])
			}

			visited[rope[len(rope)-1]] = true
		}
	}

	return len(visited), nil
}

func Trail(head, tail util.Coord) util.Coord {
	dx := math.Abs(float64(head.X) - float64(tail.X))
	dy := math.Abs(float64(head.Y) - float64(tail.Y))

	if dx == 2 && dy == 2 {
		/*
			H = Head, T = Tail, X = Destination

			T...T
			.X.X.
			..H..
			.X.X.
			T...T
		*/
		switch {
		case head.X > tail.X && head.Y > tail.Y:
			tail = util.Coord{X: head.X - 1, Y: head.Y - 1}
		case head.X > tail.X && head.Y < tail.Y:
			tail = util.Coord{X: head.X - 1, Y: head.Y + 1}
		case head.X < tail.X && head.Y > tail.Y:
			tail = util.Coord{X: head.X + 1, Y: head.Y - 1}
		case head.X < tail.X && head.Y < tail.Y:
			tail = util.Coord{X: head.X + 1, Y: head.Y + 1}
		}

		return tail
	}

	/*
		H = Head, T = Tail, X = Destination

		.TTT.
		T.X.T
		TXHXT
		T.X.T
		.TTT.
	*/
	switch {
	case head.X-tail.X > 1:
		tail = util.Coord{X: head.X - 1, Y: head.Y}
	case tail.X-head.X > 1:
		tail = util.Coord{X: head.X + 1, Y: head.Y}
	case head.Y-tail.Y > 1:
		tail = util.Coord{X: head.X, Y: head.Y - 1}
	case tail.Y-head.Y > 1:
		tail = util.Coord{X: head.X, Y: head.Y + 1}
	}

	return tail
}

func ParseInput(lines []string) ([]Move, error) {
	var directions []Move

	for _, line := range lines {
		parts := strings.Split(line, " ")

		mag, err := strconv.Atoi(parts[1])
		if err != nil {
			return directions, err
		}

		directions = append(directions, Move{Dir: parts[0], Mag: mag})
	}

	return directions, nil
}

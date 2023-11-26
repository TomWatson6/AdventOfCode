package algo

import (
	"fmt"
	"math"

	"github.com/tomwatson6/AdventOfCode2022_Go/pkg/util"
)

type AStarInfo struct {
	Grid        map[util.Coord]int
	XS, YS      int
	Start, Goal util.Coord
	Heuristic   func(map[util.Coord]int, util.Coord, util.Coord) int
	Possible    func(map[util.Coord]int, util.Coord, util.Coord) bool
	Weight      func(map[util.Coord]int, util.Coord, util.Coord) int
}

func AStar(info AStarInfo) []util.Coord {
	openSet := util.Set[util.Coord]{}
	openSet.Add(info.Start)
	cameFrom := map[util.Coord]util.Coord{}

	gScore := map[util.Coord]int{}
	gScore[info.Start] = 0

	fScore := map[util.Coord]int{}
	fScore[info.Start] = info.Heuristic(info.Grid, info.Start, info.Goal)

	for openSet.Length() > 0 {
		current := minExisting(fScore, openSet)

		if current == info.Goal {
			path := reconstructPath(cameFrom, current)
			return path
		}

		openSet.Remove(current)

		neighbours := getNeighbours(info, current)

		for _, neighbour := range neighbours {
			tentativeGScore := gScore[current] + info.Weight(info.Grid, current, neighbour)
			g := math.MaxInt

			if score, ok := gScore[neighbour]; ok {
				g = score
			}

			if tentativeGScore < g {
				cameFrom[neighbour] = current
				gScore[neighbour] = tentativeGScore
				fScore[neighbour] = tentativeGScore + info.Heuristic(info.Grid, neighbour, info.Goal)

				if !openSet.Contains(neighbour) {
					openSet.Add(neighbour)
				}
			}
		}
	}

	return []util.Coord{}
}

func PrintPath(grid map[util.Coord]int, XS, YS int, path []util.Coord) {
	for y := 0; y < YS; y++ {
		for x := 0; x < XS; x++ {
			contains := false

			for _, p := range path {
				if p.X == x && p.Y == y {
					contains = true
					break
				}
			}

			curr := util.Coord{X: x, Y: y}

			if grid[curr] == 'S' {
				fmt.Print("S")
			} else if grid[curr] == 'E' {
				fmt.Print("E")
			} else if contains {
				fmt.Print("#")
			} else {
				fmt.Print(".")
			}
		}
		fmt.Println()
	}
}

func getNeighbours(info AStarInfo, c util.Coord) []util.Coord {
	var coords []util.Coord

	for y := -1; y < 2; y++ {
		for x := -1; x < 2; x++ {
			if x == y || x == -y {
				continue
			}

			xx, yy := c.X+x, c.Y+y
			to := util.Coord{X: xx, Y: yy}

			if isWithinBounds(info.Grid, info.XS, info.YS, to) {
				if info.Possible(info.Grid, c, to) {
					coords = append(coords, to)
				}
			}
		}
	}

	return coords
}

func isWithinBounds(grid map[util.Coord]int, XS, YS int, c util.Coord) bool {
	if c.X >= 0 && c.X < XS {
		if c.Y >= 0 && c.Y < YS {
			return true
		}
	}

	return false
}

func reconstructPath(cameFrom map[util.Coord]util.Coord, current util.Coord) []util.Coord {
	totalPath := []util.Coord{
		current,
	}

	for {
		if c, ok := cameFrom[current]; ok {
			current = c
			totalPath = append(totalPath, current)
		} else {
			break
		}
	}

	reversed := []util.Coord{}

	for i := len(totalPath) - 1; i >= 0; i-- {
		reversed = append(reversed, totalPath[i])
	}

	return reversed
}

func minExisting(scores map[util.Coord]int, openSet util.Set[util.Coord]) util.Coord {
	score := math.MaxInt
	var current util.Coord

	for c, active := range openSet {
		if !active {
			continue
		}

		if s, ok := scores[c]; ok {
			if s < score {
				score = s
				current = c
			}
		}
	}

	return current
}

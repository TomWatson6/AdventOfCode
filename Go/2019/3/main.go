package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"

	"github.com/TomWatson6/AdventOfCode/Go/2019/utils"
)

type Coord struct {
	X int
	Y int
}

func (c *Coord) Add(co Coord) {
	c.X += co.X
	c.Y += co.Y
}

func (c Coord) Distance() int {
	return int(math.Abs(float64(c.X)) + math.Abs(float64(c.Y)))
}

func main() {
	lines, err := utils.ReadLines("input.txt")
	if err != nil {
		panic(err)
	}

	w1, err := getWire(lines[0])
	if err != nil {
		panic(err)
	}

	w2, err := getWire(lines[1])
	if err != nil {
		panic(err)
	}

	inter := intersections(w1, w2)

	smallest := int(1e9)

	for _, i := range inter {
		val := i.Distance()
		if val < smallest {
			smallest = val
		}
	}

	fmt.Printf("Part 1: %d\n", smallest)

	s1, err := getSteps(lines[0], inter)
	if err != nil {
		panic(err)
	}

	s2, err := getSteps(lines[1], inter)
	if err != nil {
		panic(err)
	}

	smallest = int(1e9)

	for c, s := range s1 {
		total := s + s2[c]
		if total < smallest {
			smallest = total
		}
	}

	fmt.Printf("Part 2: %d\n", smallest)
}

func getSteps(line string, inter []Coord) (map[Coord]int, error) {
	stepsMap := map[Coord]int{}
	coordMap := map[Coord]bool{}

	for _, c := range inter {
		if c.X == 0 && c.Y == 0 {
			continue
		}

		coordMap[c] = true
	}

	pos := Coord{0, 0}
	steps := 0

	for _, val := range strings.Split(line, ",") {
		dir := val[0]
		length, err := strconv.Atoi(val[1:])
		if err != nil {
			return nil, err
		}

		d := getDirection(rune(dir))

		for range length {
			pos.Add(d)
			steps += 1
			if _, ok := coordMap[pos]; ok {
				stepsMap[pos] = steps
			}
		}
	}

	return stepsMap, nil
}

func getWire(line string) (map[Coord]bool, error) {
	wire := map[Coord]bool{
		{0, 0}: true,
	}
	pos := Coord{0, 0}

	for _, val := range strings.Split(line, ",") {
		dir := val[0]
		length, err := strconv.Atoi(val[1:])
		if err != nil {
			return nil, err
		}

		d := getDirection(rune(dir))

		for range length {
			pos.Add(d)
			wire[pos] = true
		}
	}

	return wire, nil
}

func getDirection(dir rune) Coord {
	switch dir {
	case 'U':
		return Coord{-1, 0}
	case 'D':
		return Coord{1, 0}
	case 'L':
		return Coord{0, -1}
	case 'R':
		return Coord{0, 1}
	}

	return Coord{}
}

func intersections(w1, w2 map[Coord]bool) []Coord {
	intersections := []Coord{}

	for w := range w1 {
		if w.X == 0 && w.Y == 0 {
			continue
		}

		if _, ok := w2[w]; ok {
			intersections = append(intersections, w)
		}
	}

	return intersections
}

package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type Dimensions struct {
	L, W, H int
}

func (d Dimensions) Area() int {
	return (2 * d.L * d.W) + (2 * d.W * d.H) + (2 * d.H * d.L)
}

func (d Dimensions) SmallestSide() int {
	smallest := math.Min(float64(d.L*d.W), float64(d.W*d.H))
	smallest = math.Min(smallest, float64(d.H*d.L))

	return int(smallest)
}

// The elves also need a little extra paper for each present: the area of the smallest side.

func getInt(str string) int {
	val, err := strconv.Atoi(str)
	if err != nil {
		panic(err)
	}

	return val
}

func readFile(fileName string) []Dimensions {
	bytes, err := os.ReadFile(fileName)
	if err != nil {
		panic(err)
	}

	content := string(bytes)
	dimensions := []Dimensions{}

	for _, line := range strings.Split(content, "\n") {
		parts := strings.Split(line, "x")

		dimensions = append(dimensions, Dimensions{
			L: getInt(parts[0]),
			W: getInt(parts[1]),
			H: getInt(parts[2]),
		})
	}

	return dimensions
}

func main() {
	dimensions := readFile("input.txt")
	total := 0

	for _, dim := range dimensions {
		total += dim.Area() + dim.SmallestSide()
	}

	fmt.Printf("Part 1: %d\n", total)
}

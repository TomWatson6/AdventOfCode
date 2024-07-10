package main

import (
	"fmt"

	"github.com/TomWatson6/AdventOfCode/Go/2019/utils"
)

func main() {
	masses, err := utils.ReadNumbers("input.txt")
	if err != nil {
		panic(err)
	}

	total := 0
	total2 := 0

	for _, mass := range masses {
		total += Fuel(mass, false)
		total2 += Fuel(mass, true)
	}

	fmt.Printf("Part 1: %d\n", total)
	fmt.Printf("Part 2: %d\n", total2)
}

func Fuel(mass int, p2 bool) int {
	ans := mass / 3
	ans = ans - 2

	if p2 && ans > 0 {
		next := Fuel(ans, p2)
		if next > 0 {
			ans += next
		}
	}

	return ans
}

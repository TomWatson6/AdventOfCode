package main

import (
	"fmt"
	"strconv"
	"strings"
	"sync"
	"time"

	"github.com/tomwatson6/AdventOfCode2022_Go/internal/day1"
	"github.com/tomwatson6/AdventOfCode2022_Go/internal/day10"
	"github.com/tomwatson6/AdventOfCode2022_Go/internal/day11"
	"github.com/tomwatson6/AdventOfCode2022_Go/internal/day12"
	"github.com/tomwatson6/AdventOfCode2022_Go/internal/day2"
	"github.com/tomwatson6/AdventOfCode2022_Go/internal/day3"
	"github.com/tomwatson6/AdventOfCode2022_Go/internal/day4"
	"github.com/tomwatson6/AdventOfCode2022_Go/internal/day5"
	"github.com/tomwatson6/AdventOfCode2022_Go/internal/day6"
	"github.com/tomwatson6/AdventOfCode2022_Go/internal/day7"
	"github.com/tomwatson6/AdventOfCode2022_Go/internal/day8"
	"github.com/tomwatson6/AdventOfCode2022_Go/internal/day9"
)

var days = []func(string) string{
	d1, d2, d3, d4, d5, d6, d7, d8, d9, d10,
	// d11, d12,
}

func main() {
	output := make([]string, len(days))
	mu := &sync.Mutex{}
	wg := &sync.WaitGroup{}
	wg.Add(len(days))

	start := time.Now()

	path := "internal/dayX/input.txt"
	for i, d := range days {
		go func(index int, path string, day func(string) string, mu *sync.Mutex, wg *sync.WaitGroup) {
			p := strings.Replace(path, "X", strconv.Itoa(index+1), 1)
			solStart := time.Now()

			solution := day(p)

			solElapsed := time.Since(solStart)

			solution += fmt.Sprintf("Time Taken: %d ms\n\n", solElapsed.Milliseconds())

			mu.Lock()
			output[index] = solution
			mu.Unlock()

			wg.Done()
		}(i, path, d, mu, wg)
	}

	wg.Wait()

	for _, out := range output {
		fmt.Print(out)
	}

	elapsed := time.Since(start)

	fmt.Printf("Total Time Taken: %d ms", elapsed.Milliseconds())
}

func d1(fileName string) string {
	output := "--- Day 1 ---\n"

	d1p1, err := day1.Part1(fileName)
	if err != nil {
		panic(err)
	}

	output += fmt.Sprintf("Part 1: %d\n", d1p1)

	d1p2, err := day1.Part2(fileName)
	if err != nil {
		panic(err)
	}

	output += fmt.Sprintf("Part 2: %d\n", d1p2)

	return output
}

func d2(fileName string) string {
	output := "--- Day 2 ---\n"

	d2p1, err := day2.Part1(fileName)
	if err != nil {
		panic(err)
	}

	output += fmt.Sprintf("Part 1: %d\n", d2p1)

	d2p2, err := day2.Part2(fileName)
	if err != nil {
		panic(err)
	}

	output += fmt.Sprintf("Part 2: %d\n", d2p2)

	return output
}

func d3(fileName string) string {
	output := "--- Day 3 ---\n"

	d3p1, err := day3.Part1(fileName)
	if err != nil {
		panic(err)
	}

	output += fmt.Sprintf("Part 1: %d\n", d3p1)

	d3p2, err := day3.Part2(fileName)
	if err != nil {
		panic(err)
	}

	output += fmt.Sprintf("Part 2: %d\n", d3p2)

	return output
}

func d4(fileName string) string {
	output := "--- Day 4 ---\n"

	d4p1, err := day4.Part1(fileName)
	if err != nil {
		panic(err)
	}

	output += fmt.Sprintf("Part 1: %d\n", d4p1)

	d4p2, err := day4.Part2(fileName)
	if err != nil {
		panic(err)
	}

	output += fmt.Sprintf("Part 2: %d\n", d4p2)

	return output
}

func d5(fileName string) string {
	output := "--- Day 5 ---\n"

	d5p1, err := day5.Part1(fileName)
	if err != nil {
		panic(err)
	}

	output += fmt.Sprintf("Part 1: %s\n", d5p1)

	d5p2, err := day5.Part2(fileName)
	if err != nil {
		panic(err)
	}

	output += fmt.Sprintf("Part 2: %s\n", d5p2)

	return output
}

func d6(fileName string) string {
	output := "--- Day 6 ---\n"

	d6p1, err := day6.Part1(fileName)
	if err != nil {
		panic(err)
	}

	output += fmt.Sprintf("Part 1: %d\n", d6p1)

	d6p2, err := day6.Part2(fileName)
	if err != nil {
		panic(err)
	}

	output += fmt.Sprintf("Part 2: %d\n", d6p2)

	return output
}

func d7(fileName string) string {
	output := "--- Day 7 ---\n"

	d7p1, err := day7.Part1(fileName)
	if err != nil {
		panic(err)
	}

	output += fmt.Sprintf("Part 1: %d\n", d7p1)

	d7p2, err := day7.Part2(fileName)
	if err != nil {
		panic(err)
	}

	output += fmt.Sprintf("Part 2: %d\n", d7p2)

	return output
}

func d8(fileName string) string {
	output := "--- Day 8 ---\n"

	d8p1, err := day8.Part1(fileName)
	if err != nil {
		panic(err)
	}

	output += fmt.Sprintf("Part 1: %d\n", d8p1)

	d8p2, err := day8.Part2(fileName)
	if err != nil {
		panic(err)
	}

	output += fmt.Sprintf("Part 2: %d\n", d8p2)

	return output
}

func d9(fileName string) string {
	output := "--- Day 9 ---\n"

	d9p1, err := day9.Part1(fileName)
	if err != nil {
		panic(err)
	}

	output += fmt.Sprintf("Part 1: %d\n", d9p1)

	d9p2, err := day9.Part2(fileName)
	if err != nil {
		panic(err)
	}

	output += fmt.Sprintf("Part 2: %d\n", d9p2)

	return output
}

func d10(fileName string) string {
	output := "--- Day 10 ---\n"

	d10p1, err := day10.Part1(fileName)
	if err != nil {
		panic(err)
	}

	output += fmt.Sprintf("Part 1: %d\n", d10p1)

	d10p2, err := day10.Part2(fileName)
	if err != nil {
		panic(err)
	}

	output += fmt.Sprintf("Part 2:\n%s", d10p2)

	return output
}

func d11(fileName string) string {
	output := "--- Day 11 ---\n"

	d11p1, err := day11.Part1(fileName)
	if err != nil {
		panic(err)
	}

	output += fmt.Sprintf("Part 1: %d\n", d11p1)

	d11p2, err := day11.Part2(fileName)
	if err != nil {
		panic(err)
	}

	output += fmt.Sprintf("Part 2: %d\n", d11p2)

	return output
}

func d12(fileName string) string {
	output := "--- Day 12 ---\n"

	d12p1, err := day12.Part1(fileName)
	if err != nil {
		panic(err)
	}

	output += fmt.Sprintf("Part 1: %d\n", d12p1)

	d12p2, err := day12.Part2(fileName)
	if err != nil {
		panic(err)
	}

	output += fmt.Sprintf("Part 2: %d\n", d12p2)

	return output
}

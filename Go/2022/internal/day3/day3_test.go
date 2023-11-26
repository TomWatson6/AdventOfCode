package day3_test

import (
	"testing"

	"github.com/tomwatson6/AdventOfCode2022_Go/internal/day3"
)

func TestD3P1(t *testing.T) {
	score, err := day3.Part1("simple_input.txt")
	if err != nil {
		t.Fatal(err)
	}

	expected := 157

	if score != expected {
		t.Fatalf("got incorrect score for day 3 part 1, got: %d, expected: %d", score, expected)
	}
}

func TestIntersection(t *testing.T) {
	line := "vJrwpWtwJgWrhcsFMMfFFhFp"

	common := day3.Intersection(line[:len(line)/2], line[len(line)/2:])
	expected := 'p'

	if common != expected {
		t.Fatalf("intersection func not working correctly, expected: %v, got: %v", expected, common)
	}
}

func TestPriorityLower(t *testing.T) {
	input := 'p'

	priority := day3.Priority(input)
	expected := 16

	if priority != expected {
		t.Fatalf("priority func not working correctly, expected: %d, got: %d", expected, priority)
	}
}

func TestPriorityUpper(t *testing.T) {
	input := 'P'

	priority := day3.Priority(input)
	expected := 42

	if priority != expected {
		t.Fatalf("priority func not working correctly, expected: %d, got: %d", expected, priority)
	}
}

func TestD3P2(t *testing.T) {
	score, err := day3.Part2("simple_input.txt")
	if err != nil {
		t.Fatal(err)
	}

	expected := 70

	if score != expected {
		t.Fatalf("got incorrect score for day 3 part 2, got: %d, expected: %d", score, expected)
	}
}

func TestCommonItem(t *testing.T) {
	rucksacks := []string{
		"vJrwpWtwJgWrhcsFMMfFFhFp",
		"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
		"PmmdzqPrVvPwwTWBwg",
	}

	common, err := day3.CommonItem(rucksacks)
	if err != nil {
		t.Fatal(err)
	}

	expected := 'r'

	if common != expected {
		t.Fatalf("commonitem func not working correctly, expected: %v, got: %v", expected, common)
	}
}

func BenchmarkD3P1(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_, err := day3.Part1("simple_input.txt")
		if err != nil {
			b.Fatalf("benchmarking invalid on non-working solution for day 3, part 1")
		}
	}
}

func BenchmarkD3P2(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_, err := day3.Part2("simple_input.txt")
		if err != nil {
			b.Fatalf("benchmarking invalid on non-working solution for day 3, part 2")
		}
	}
}

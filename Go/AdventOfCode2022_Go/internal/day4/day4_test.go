package day4_test

import (
	"testing"

	"github.com/tomwatson6/AdventOfCode2022_Go/internal/day4"
)

func TestD4P1(t *testing.T) {
	ans, err := day4.Part1("simple_input.txt")
	if err != nil {
		t.Fatal(err)
	}

	expected := 2

	if ans != expected {
		t.Fatalf("got incorrect answer for day 4 part 1, got: %d, expected: %d", ans, expected)
	}
}

func TestD4P2(t *testing.T) {
	ans, err := day4.Part2("simple_input.txt")
	if err != nil {
		t.Fatal(err)
	}

	expected := 4

	if ans != expected {
		t.Fatalf("got incorrect answer for day 4 part 2, got: %d, expected, %d", ans, expected)
	}
}

func BenchmarkD4P1(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_, err := day4.Part1("simple_input.txt")
		if err != nil {
			b.Fatalf("benchmarking invalid on non-working solution for day 4, part 1")
		}
	}
}

func BenchmarkD4P2(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_, err := day4.Part2("simple_input.txt")
		if err != nil {
			b.Fatalf("benchmarking invalid on non-working solution for day 4, part 2")
		}
	}
}

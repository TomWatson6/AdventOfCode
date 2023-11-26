package day12_test

import (
	"testing"

	"github.com/tomwatson6/AdventOfCode2022_Go/internal/day12"
)

func TestD12P1(t *testing.T) {
	ans, err := day12.Part1("simple_input.txt")
	if err != nil {
		t.Fatal(err)
	}

	expected := 31

	if ans != expected {
		t.Fatalf("got incorrect answer for day 12 part 1, got: %d, expected: %d", ans, expected)
	}
}

func TestD12P2(t *testing.T) {
	ans, err := day12.Part2("simple_input.txt")
	if err != nil {
		t.Fatal(err)
	}

	expected := 29

	if ans != expected {
		t.Fatalf("got incorrect answer for day 12 part 2, got: %d, expected, %d", ans, expected)
	}
}

func BenchmarkD12P1(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_, err := day12.Part1("simple_input.txt")
		if err != nil {
			b.Fatalf("benchmarking invalid on non-working solution for day 12, part 1")
		}
	}
}

func BenchmarkD12P2(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_, err := day12.Part2("simple_input.txt")
		if err != nil {
			b.Fatalf("benchmarking invalid on non-working solution for day 12, part 2")
		}
	}
}

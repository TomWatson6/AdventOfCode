package day9_test

import (
	"testing"

	"github.com/tomwatson6/AdventOfCode2022_Go/internal/day9"
)

func TestD9P1(t *testing.T) {
	ans, err := day9.Part1("simple_input.txt")
	if err != nil {
		t.Fatal(err)
	}

	expected := 13

	if ans != expected {
		t.Fatalf("got incorrect answer for day 9 part 1, got: %d, expected: %d", ans, expected)
	}
}

func TestD9P2(t *testing.T) {
	ans, err := day9.Part2("simple_input2.txt")
	if err != nil {
		t.Fatal(err)
	}

	expected := 36

	if ans != expected {
		t.Fatalf("got incorrect answer for day 9 part 2, got: %d, expected, %d", ans, expected)
	}
}

func BenchmarkD9P1(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_, err := day9.Part1("simple_input.txt")
		if err != nil {
			b.Fatalf("benchmarking invalid on non-working solution for day 9, part 1")
		}
	}
}

func BenchmarkD9P2(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_, err := day9.Part2("simple_input.txt")
		if err != nil {
			b.Fatalf("benchmarking invalid on non-working solution for day 9, part 2")
		}
	}
}

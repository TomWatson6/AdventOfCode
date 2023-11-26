package day7_test

import (
	"testing"

	"github.com/tomwatson6/AdventOfCode2022_Go/internal/day7"
)

func TestD7P1(t *testing.T) {
	ans, err := day7.Part1("simple_input.txt")
	if err != nil {
		t.Fatal(err)
	}

	expected := 95437

	if ans != expected {
		t.Fatalf("got incorrect answer for day 7 part 1, got: %d, expected: %d", ans, expected)
	}
}

func TestD7P2(t *testing.T) {
	ans, err := day7.Part2("simple_input.txt")
	if err != nil {
		t.Fatal(err)
	}

	expected := 24933642

	if ans != expected {
		t.Fatalf("got incorrect answer for day 7 part 2, got: %d, expected, %d", ans, expected)
	}
}

func BenchmarkD7P1(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_, err := day7.Part1("simple_input.txt")
		if err != nil {
			b.Fatalf("benchmarking invalid on non-working solution for day 7, part 1")
		}
	}
}

func BenchmarkD7P2(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_, err := day7.Part2("simple_input.txt")
		if err != nil {
			b.Fatalf("benchmarking invalid on non-working solution for day 7, part 2")
		}
	}
}

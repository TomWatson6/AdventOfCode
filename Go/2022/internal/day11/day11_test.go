package day11_test

import (
	"testing"

	"github.com/tomwatson6/AdventOfCode2022_Go/internal/day11"
)

func TestD11P1(t *testing.T) {
	ans, err := day11.Part1("simple_input.txt")
	if err != nil {
		t.Fatal(err)
	}

	expected := 10605

	if ans != expected {
		t.Fatalf("got incorrect answer for day 11 part 1, got: %d, expected: %d", ans, expected)
	}
}

func TestD11P2(t *testing.T) {
	ans, err := day11.Part2("simple_input.txt")
	if err != nil {
		t.Fatal(err)
	}

	expected := 2713310158

	if ans != expected {
		t.Fatalf("got incorrect answer for day 11 part 2, got: %d, expected, %d", ans, expected)
	}
}

func BenchmarkD11P1(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_, err := day11.Part1("simple_input.txt")
		if err != nil {
			b.Fatalf("benchmarking invalid on non-working solution for day 11, part 1")
		}
	}
}

func BenchmarkD11P2(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_, err := day11.Part2("simple_input.txt")
		if err != nil {
			b.Fatalf("benchmarking invalid on non-working solution for day 11, part 2")
		}
	}
}

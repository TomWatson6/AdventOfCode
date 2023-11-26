package day2_test

import (
	"testing"

	"github.com/tomwatson6/AdventOfCode2022_Go/internal/day2"
)

func TestD2P1(t *testing.T) {
	score, err := day2.Part1("simple_input.txt")
	if err != nil {
		t.Fatal(err)
	}

	expected := 15

	if score != expected {
		t.Fatalf("got incorrect score for day 2 part 1, got: %d, expected: %d", score, expected)
	}
}

func TestD2P2(t *testing.T) {
	score, err := day2.Part2("simple_input.txt")
	if err != nil {
		t.Fatal(err)
	}

	expected := 12

	if score != expected {
		t.Fatalf("got incorrect score for day 2 part 2, got: %d, expected: %d", score, expected)
	}
}

func BenchmarkD2P1(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_, err := day2.Part1("simple_input.txt")
		if err != nil {
			b.Fatalf("benchmarking invalid on non-working solution for day 2, part 1")
		}
	}
}

func BenchmarkD2P2(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_, err := day2.Part2("simple_input.txt")
		if err != nil {
			b.Fatalf("benchmarking invalid on non-working solution for day 2, part 2")
		}
	}
}

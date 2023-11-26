package day6_test

import (
	"testing"

	"github.com/tomwatson6/AdventOfCode2022_Go/internal/day6"
)

func TestD6P1(t *testing.T) {
	ans, err := day6.Part1("simple_input.txt")
	if err != nil {
		t.Fatal(err)
	}

	expected := 7

	if ans != expected {
		t.Fatalf("got incorrect answer for day 6 part 1, got: %d, expected: %d", ans, expected)
	}
}

func TestFindMarker(t *testing.T) {
	input := "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

	ans := day6.FindMarker(input, 4)

	expected := 7

	if ans != expected {
		t.Fatalf("find marker did not produce the correct result: expected: %d, got: %d", expected, ans)
	}
}

func TestD6P2(t *testing.T) {
	ans, err := day6.Part2("simple_input.txt")
	if err != nil {
		t.Fatal(err)
	}

	expected := 19

	if ans != expected {
		t.Fatalf("got incorrect answer for day 6 part 2, got: %d, expected, %d", ans, expected)
	}
}

func BenchmarkD6P1(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_, err := day6.Part1("simple_input.txt")
		if err != nil {
			b.Fatalf("benchmarking invalid on non-working solution for day 6, part 1")
		}
	}
}

func BenchmarkD6P2(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_, err := day6.Part2("simple_input.txt")
		if err != nil {
			b.Fatalf("benchmarking invalid on non-working solution for day 6, part 2")
		}
	}
}

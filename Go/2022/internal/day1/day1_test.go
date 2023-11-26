package day1_test

import (
	"testing"

	"github.com/tomwatson6/AdventOfCode2022_Go/internal/day1"
)

func TestD1P1(t *testing.T) {
	ans, err := day1.Part1("simple_input.txt")
	if err != nil {
		t.Fatal(err)
	}

	expected := 24000

	if ans != expected {
		t.Fatalf("incorrect answer, expected: %d, got: %d", expected, ans)
	}
}

func TestD1P2(t *testing.T) {
	ans, err := day1.Part2("simple_input.txt")
	if err != nil {
		t.Fatal(err)
	}

	expected := 45000

	if ans != expected {
		t.Fatalf("incorrect answer, expected %d, got %d", expected, ans)
	}
}

func BenchmarkD1P1(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_, err := day1.Part1("simple_input.txt")
		if err != nil {
			b.Fatal("benchmarking invalid on non-working solution for day 1, part 1")
		}
	}
}

func BenchmarkD1P2(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_, err := day1.Part2("simple_input.txt")
		if err != nil {
			b.Fatal("benchmarking invalid on non-working solution for day 1, part 2")
		}
	}
}

package day5_test

import (
	"reflect"
	"testing"

	"github.com/tomwatson6/AdventOfCode2022_Go/internal/day5"
	"github.com/tomwatson6/AdventOfCode2022_Go/pkg/util"
)

func TestD5P1(t *testing.T) {
	ans, err := day5.Part1("simple_input.txt")
	if err != nil {
		t.Fatal(err)
	}

	expected := "CMZ"

	if ans != expected {
		t.Fatalf("got incorrect answer for day 5 part 1, got: %s, expected: %s", ans, expected)
	}
}

func TestD5P2(t *testing.T) {
	ans, err := day5.Part2("simple_input.txt")
	if err != nil {
		t.Fatal(err)
	}

	expected := "MCD"

	if ans != expected {
		t.Fatalf("got incorrect answer for day 5 part 2, got: %s, expected, %s", ans, expected)
	}
}

func TestTransfer(t *testing.T) {
	stacks := &[]util.Stack[rune]{
		{'A', 'B', 'C', 'D'},
		{'E', 'F', 'G', 'H'},
	}

	day5.Transfer(stacks, 3, 0, 1, false)

	expected := &[]util.Stack[rune]{
		{'A'},
		{'E', 'F', 'G', 'H', 'D', 'C', 'B'},
	}

	if !reflect.DeepEqual(stacks, expected) {
		t.Fatalf("transfer failed, expected: %v, got: %v", expected, stacks)
	}
}

func TestTransferOrderRetained(t *testing.T) {
	stacks := &[]util.Stack[rune]{
		{'A', 'B', 'C', 'D'},
		{'E', 'F', 'G', 'H'},
	}

	day5.Transfer(stacks, 2, 1, 0, true)

	expected := &[]util.Stack[rune]{
		{'A', 'B', 'C', 'D', 'G', 'H'},
		{'E', 'F'},
	}

	if !reflect.DeepEqual(stacks, expected) {
		t.Fatalf("transfer failed, expected: %v, got: %v", expected, stacks)
	}
}

func BenchmarkD5P1(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_, err := day5.Part1("simple_input.txt")
		if err != nil {
			b.Fatalf("benchmarking invalid on non-working solution for day 5, part 1")
		}
	}
}

func BenchmarkD5P2(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_, err := day5.Part2("simple_input.txt")
		if err != nil {
			b.Fatalf("benchmarking invalid on non-working solution for day 5, part 2")
		}
	}
}

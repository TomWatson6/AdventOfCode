package day8_test

import (
	"testing"

	"github.com/tomwatson6/AdventOfCode2022_Go/internal/day8"
	"github.com/tomwatson6/AdventOfCode2022_Go/pkg/input"
	"github.com/tomwatson6/AdventOfCode2022_Go/pkg/util"
)

func TestD8P1(t *testing.T) {
	ans, err := day8.Part1("simple_input.txt")
	if err != nil {
		t.Fatal(err)
	}

	expected := 21

	if ans != expected {
		t.Fatalf("got incorrect answer for day 8 part 1, got: %d, expected: %d", ans, expected)
	}
}

func TestD8P2(t *testing.T) {
	ans, err := day8.Part2("simple_input.txt")
	if err != nil {
		t.Fatal(err)
	}

	expected := 8

	if ans != expected {
		t.Fatalf("got incorrect answer for day 8 part 2, got: %d, expected, %d", ans, expected)
	}
}

func TestIsVisible(t *testing.T) {
	i, err := input.ReadFile("simple_input.txt")
	if err != nil {
		t.Fatal(err)
	}

	lines := input.GetLines(i)
	grid, XS, YS, err := day8.ParseInput(lines)
	if err != nil {
		t.Fatal(err)
	}

	tcs := []struct {
		name     string
		test     util.Coord
		expected bool
	}{
		{
			name:     "TopLeft",
			test:     util.Coord{X: 1, Y: 1},
			expected: true,
		},
		{
			name:     "TopRight",
			test:     util.Coord{X: 3, Y: 1},
			expected: false,
		},
	}

	for _, tc := range tcs {
		v := day8.IsVisible(grid, tc.test, XS, YS)
		if v != tc.expected {
			t.Fatalf("isVisible not working correctly, expected: %v, got: %v", tc.expected, v)
		}
	}
}

func TestGetScenicScore(t *testing.T) {
	i, err := input.ReadFile("simple_input.txt")
	if err != nil {
		t.Fatal(err)
	}

	lines := input.GetLines(i)
	grid, XS, YS, err := day8.ParseInput(lines)
	if err != nil {
		t.Fatal(err)
	}

	tcs := []struct {
		name     string
		test     util.Coord
		expected int
	}{
		{
			name:     "TopMiddle",
			test:     util.Coord{X: 2, Y: 1},
			expected: 4,
		},
		{
			name:     "BottomMiddle",
			test:     util.Coord{X: 2, Y: 3},
			expected: 8,
		},
	}

	for _, tc := range tcs {
		v := day8.GetScenicScore(grid, tc.test, XS, YS)
		if v != tc.expected {
			t.Fatalf("getScenicScore not working correctly, expected: %v, got: %v", tc.expected, v)
		}
	}
}

func BenchmarkD8P1(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_, err := day8.Part1("simple_input.txt")
		if err != nil {
			b.Fatalf("benchmarking invalid on non-working solution for day 8, part 1")
		}
	}
}

func BenchmarkD8P2(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_, err := day8.Part2("simple_input.txt")
		if err != nil {
			b.Fatalf("benchmarking invalid on non-working solution for day 8, part 2")
		}
	}
}

package day10_test

import (
	"testing"

	"github.com/tomwatson6/AdventOfCode2022_Go/internal/day10"
)

func TestD10P1(t *testing.T) {
	ans, err := day10.Part1("simple_input.txt")
	if err != nil {
		t.Fatal(err)
	}

	expected := 13140

	if ans != expected {
		t.Fatalf("got incorrect answer for day 10 part 1, got: %d, expected: %d", ans, expected)
	}
}

func TestD10P2(t *testing.T) {
	ans, err := day10.Part2("simple_input.txt")
	if err != nil {
		t.Fatal(err)
	}

	expected := `##  ##  ##  ##  ##  ##  ##  ##  ##  ##  
###   ###   ###   ###   ###   ###   ### 
####    ####    ####    ####    ####    
#####     #####     #####     #####     
######      ######      ######      ####
#######       #######       #######     
`

	if ans != expected {
		t.Fatalf("got incorrect answer for day 10 part 2, got:\n%s\nexpected:\n%s\n", ans, expected)
	}
}

func BenchmarkD10P1(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_, err := day10.Part1("simple_input.txt")
		if err != nil {
			b.Fatalf("benchmarking invalid on non-working solution for day 10, part 1")
		}
	}
}

func BenchmarkD10P2(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_, err := day10.Part2("simple_input.txt")
		if err != nil {
			b.Fatalf("benchmarking invalid on non-working solution for day 10, part 2")
		}
	}
}

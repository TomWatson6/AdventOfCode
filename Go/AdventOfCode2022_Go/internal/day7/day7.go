package day7

import (
	"sort"
	"strconv"
	"strings"

	"github.com/tomwatson6/AdventOfCode2022_Go/pkg/input"
)

type file struct {
	name string
	size int
}

type directory struct {
	name        string
	parent      *directory
	files       []*file
	directories []*directory
}

func NewDirectory(name string, parent *directory) *directory {
	return &directory{
		name:        name,
		parent:      parent,
		files:       []*file{},
		directories: []*directory{},
	}
}

func (d directory) calculateDirSizes(sizes *[]int) int {
	total := 0

	for _, file := range d.files {
		total += file.size
	}

	for _, dir := range d.directories {
		total += dir.calculateDirSizes(sizes)
	}

	*sizes = append(*sizes, total)
	return total
}

func Part1(fileName string) (int, error) {
	i, err := input.ReadFile(fileName)
	if err != nil {
		return 0, err
	}

	lines := input.GetLines(i)

	fileSystem, err := mapFileSystem(lines)
	if err != nil {
		return 0, err
	}

	sizes := []int{}
	fileSystem.calculateDirSizes(&sizes)

	total := 0

	for _, size := range sizes {
		if size <= 100000 {
			total += size
		}
	}

	return total, nil
}

func Part2(fileName string) (int, error) {
	i, err := input.ReadFile(fileName)
	if err != nil {
		return 0, err
	}

	lines := input.GetLines(i)

	fileSystem, err := mapFileSystem(lines)
	if err != nil {
		return 0, err
	}

	sizes := []int{}
	fileSystem.calculateDirSizes(&sizes)

	total := sizes[len(sizes)-1]
	toDelete := 30000000 - (70000000 - total)

	sort.Ints(sizes)
	selected := 0

	for _, s := range sizes {
		if s > toDelete {
			selected = s
			break
		}
	}

	return selected, nil
}

func mapFileSystem(lines []string) (*directory, error) {
	level := 0
	root := NewDirectory("root", nil)
	curr := root

	for _, line := range lines {
		parts := strings.Split(line, " ")

		if parts[0] == "$" {
			if parts[1] == "cd" {
				if parts[2] == ".." {
					curr = curr.parent
					level -= 1
				} else {
					curr.directories = append(curr.directories, NewDirectory(parts[2], curr))
					curr = curr.directories[len(curr.directories)-1]
					level += 1
				}
			} else {
				continue
			}
		} else {
			if parts[0] == "dir" {
				continue
			}
			size, err := strconv.Atoi(parts[0])
			if err != nil {
				return nil, err
			}

			curr.files = append(curr.files, &file{name: parts[1], size: size})
		}
	}

	return root, nil
}

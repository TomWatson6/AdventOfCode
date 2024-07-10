package intcode

import "github.com/TomWatson6/AdventOfCode/Go/2019/intcode/command"

type Computer struct {
	Program []int
}

func New(program []int) Computer {
	return Computer{
		Program: program,
	}
}

func (c *Computer) Run() error {
	ptr := 0

	for c.Program[ptr] != 99 {
		com := command.ParseCommand(c.Program[ptr])
		if err := com.Run(&ptr, c.Program); err != nil {
			return err
		}
	}

	return nil
}

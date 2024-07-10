package command

type Command interface {
	Run(ptr *int, program []int) error
}

func ParseCommand(code int) Command {
	switch code {
	case 1:
		return NewAdd()
	case 2:
		return NewMult()
	}

	return nil
}

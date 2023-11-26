package util

import "fmt"

type Stack[T any] []T

func (s *Stack[T]) Push(item T) {
	*s = append(*s, item)
}

func (s *Stack[T]) Pop() (*T, error) {
	if len(*s) == 0 {
		return nil, fmt.Errorf("cannot pop item from empty stack")
	}

	ret := (*s)[len(*s)-1]
	*s = (*s)[:len(*s)-1]
	return &ret, nil
}

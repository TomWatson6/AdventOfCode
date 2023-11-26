package util

type Set[T comparable] map[T]bool

func NewFromSlice[T comparable](items []T) Set[T] {
	set := make(Set[T])

	set.AddMany(items)

	return set
}

func NewFromMapKeys[T comparable, R comparable](kvp map[T]R) Set[T] {
	set := make(Set[T])

	for k := range kvp {
		set.Add(k)
	}

	return set
}

func NewFromMapValues[T comparable, R comparable](kvp map[T]R) Set[R] {
	set := make(Set[R])

	for _, v := range kvp {
		set.Add(v)
	}

	return set
}

func (s *Set[T]) Add(item T) {
	(*s)[item] = true
}

func (s *Set[T]) AddMany(items []T) {
	for _, item := range items {
		(*s)[item] = true
	}
}

func (s *Set[T]) Remove(item T) {
	(*s)[item] = false
}

func (s *Set[T]) RemoveMany(items []T) {
	for _, item := range items {
		(*s)[item] = false
	}
}

func (s Set[T]) Contains(t T) bool {
	for elem := range s {
		if elem == t {
			return s[elem]
		}
	}

	return false
}

func (s Set[T]) Intersect(t Set[T]) Set[T] {
	intersection := Set[T]{}

	for elem := range s {
		if _, ok := t[elem]; ok {
			intersection[elem] = true
		}
	}

	return intersection
}

func (s Set[T]) Length() int {
	length := 0

	for _, t := range s {
		if t {
			length += 1
		}
	}

	return length
}

func (s Set[T]) ToArray() []T {
	var arr []T

	for item := range s {
		arr = append(arr, item)
	}

	return arr
}

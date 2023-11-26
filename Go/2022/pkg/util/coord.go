package util

type Coord struct {
	X, Y int
}

func (c *Coord) Add(c1 Coord) {
	c.X += c1.X
	c.Y += c1.Y
}

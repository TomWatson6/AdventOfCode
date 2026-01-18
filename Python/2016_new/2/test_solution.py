import unittest
import solution

input = open("simple_input.txt").read().strip()

class Day02Test(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(1985, solution.part1(input))

    def test_part2(self):
        self.assertEqual("5DB3", solution.part2(input))

if __name__ == "__main__":
    unittest.main()


















import unittest
import solution

input = open("simple_input.txt").read().strip()

class Day18Test(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(22, solution.part1(input, 6, 12))

    def test_part2(self):
        self.assertEqual("6,1", solution.part2(input, 6))

if __name__ == "__main__":
    unittest.main()



















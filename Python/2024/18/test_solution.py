import unittest
import solution

input = open("simple_input.txt").read().strip()

class Day18Test(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(22, solution.part1(input, 6))

    def test_part2(self):
        self.assertEqual(0, solution.part2(input))

if __name__ == "__main__":
    unittest.main()



















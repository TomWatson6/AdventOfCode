import unittest
import solution

input = open("simple_input.txt").read().strip()

class Day14Test(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(12, solution.part1(input, 11, 7))

    def test_part2(self):
        self.assertEqual(0, solution.part2(input, 11, 7))

if __name__ == "__main__":
    unittest.main()



















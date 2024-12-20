import unittest
import solution

input = open("simple_input.txt").read().strip()

class Day20Test(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(0, solution.part1(input))

    def test_part2(self):
        self.assertEqual(285, solution.part2(input))

if __name__ == "__main__":
    unittest.main()



















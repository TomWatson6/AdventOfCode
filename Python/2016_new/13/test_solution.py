import unittest
import solution

input = open("simple_input.txt").read().strip()

class Day13Test(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(11, solution.part1(input, (7, 4)))

    def test_part2(self):
        self.assertEqual(151, solution.part2(input, (7, 4)))

if __name__ == "__main__":
    unittest.main()


















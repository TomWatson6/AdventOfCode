import unittest
import solution

input = open("simple_input.txt").read().strip()
input2 = open("simple_input2.txt").read().strip()

class Day03Test(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(161, solution.part1(input))

    def test_part2(self):
        self.assertEqual(48, solution.part2(input2))

if __name__ == "__main__":
    unittest.main()


















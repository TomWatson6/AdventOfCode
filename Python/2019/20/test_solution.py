import unittest
import solution

input = open("simple_input.txt").read()
input2 = open("simple_input2.txt").read()
input3 = open("simple_input3.txt").read()

class Day20Test(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(23, solution.part1(input))
        self.assertEqual(58, solution.part1(input2))

    def test_part2(self):
        self.assertEqual(396, solution.part2(input3))

if __name__ == "__main__":
    unittest.main()


















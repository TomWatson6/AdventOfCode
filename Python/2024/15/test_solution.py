import unittest
import solution

input = open("simple_input.txt").read().strip()
input2 = open("simple_input2.txt").read().strip()
small_input = open("simple_input_small.txt").read().strip()

class Day15Test(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(2028, solution.part1(small_input))
        self.assertEqual(10092, solution.part1(input))

    def test_part2(self):
        self.assertEqual(9021, solution.part2(input))

if __name__ == "__main__":
    unittest.main()



















import unittest
import solution

input = open("simple_input.txt").read().strip()
input2 = open("simple_input2.txt").read().strip()

class Day22Test(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(37327623, solution.part1(input))

    def test_part2(self):
        self.assertEqual(23, solution.part2(input2))

if __name__ == "__main__":
    unittest.main()



















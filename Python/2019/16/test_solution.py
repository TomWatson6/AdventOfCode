import unittest
import solution

input = open("simple_input.txt").read().strip()
input2 = open("simple_input2.txt").read().strip()

class Day16Test(unittest.TestCase):
    def test_part1(self):
        self.assertEqual("01029498", solution.part1(input))

    def test_part2(self):
        self.assertEqual("84462026", solution.part2(input2))

if __name__ == "__main__":
    unittest.main()


















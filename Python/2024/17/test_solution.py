import unittest
import solution

input = open("simple_input.txt").read().strip()
input2 = open("simple_input2.txt").read().strip()

class Day17Test(unittest.TestCase):
    def test_part1(self):
        self.assertEqual("4,6,3,5,6,3,5,2,1,0", solution.part1(input))

    def test_part2(self):
        self.assertEqual(117440, solution.part2(input2))

if __name__ == "__main__":
    unittest.main()



















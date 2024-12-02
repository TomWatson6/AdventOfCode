from collections import defaultdict

input = open("input.txt").read().strip()

class Report:
    def __init__(self, line: str):
        self.nums = [int(x.strip()) for x in line.split(" ")]

    def safe(self) -> bool:
        increasing = 0
        decreasing = 0
        for a, b in list(zip(self.nums, self.nums[1:])):
            if a < b:
                if b - a > 3:
                    return False
                decreasing += 1
            elif a > b:
                if a - b > 3:
                    return False
                increasing += 1
            else:
                return False

        if increasing and not decreasing:
            return True

        if decreasing and not increasing:
            return True

        return False

    def safe2(self) -> bool:
        valid = False
        valid = self.nums == sorted(self.nums) or (self.nums == sorted(self.nums, reverse=True))
        valid = valid and all([0 < abs(a - b) <= 3 for a, b in list(zip(self.nums, self.nums[1:]))])
        if valid:
            return True

        for nums in [[x for i, x in enumerate(self.nums) if i != r] for r in range(len(self.nums))]:
            valid = False
            valid = nums == sorted(nums) or nums == sorted(nums, reverse=True)
            valid = valid and all([0 < abs(a - b) <= 3 for a, b in list(zip(nums, nums[1:]))])
            if valid:
                return True

        return False

    def __repr__(self) -> str:
        return f"{' '.join([str(x) for x in self.nums])}"


def part1(input: str) -> int:
    reports = [Report(x.strip()) for x in input.split("\n")]
    valid = sum([report.safe() for report in reports])

    return valid

def part2(input: str) -> int:
    reports = [Report(x.strip()) for x in input.split("\n")]
    valid = sum([report.safe2() for report in reports])

    return valid

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))

















input = open("input.txt").read().strip()

class Intcode:
    def __init__(self, input):
        top, bottom = input.split("\n\n")
        self.registers = [int(x.split(": ")[1]) for x in top.splitlines()]
        self.program = [int(x) for x in bottom.split(": ")[1].split(",")]
        self.ptr = 0

    def get_operand(self, operand):
        if operand in range(4):
            return operand
        
        match operand:
            case 4:
                return self.registers[0]
            case 5:
                return self.registers[1]
            case 6:
                return self.registers[2]
            case _:
                assert False, f"invalid operand: {operand}"

    def run(self):
        outputs = []

        while self.ptr < len(self.program):
            opcode = self.program[self.ptr]

            match opcode:
                case 0: # adv
                    num = self.registers[0]
                    combo_op = self.get_operand(self.program[self.ptr + 1])
                    den = 2 ** combo_op
                    self.registers[0] = num // den
                case 1: # bxl
                    operand = self.program[self.ptr + 1]
                    self.registers[1] = self.registers[1] ^ operand
                case 2: # bst
                    combo_op = self.get_operand(self.program[self.ptr + 1])
                    self.registers[1] = combo_op % 8
                case 3: # jnz
                    if self.registers[0] != 0:
                        self.ptr = self.program[self.ptr + 1]
                        continue
                case 4: # bxc
                    self.registers[1] = self.registers[1] ^ self.registers[2]
                case 5: # out
                    combo_op = self.get_operand(self.program[self.ptr + 1])
                    outputs.append(combo_op % 8)
                case 6: # bdv
                    num = self.registers[0]
                    combo_op = self.get_operand(self.program[self.ptr + 1])
                    den = 2 ** combo_op
                    self.registers[1] = num // den
                case 7: # cdv
                    num = self.registers[0]
                    combo_op = self.get_operand(self.program[self.ptr + 1])
                    den = 2 ** combo_op
                    self.registers[2] = num // den

            self.ptr += 2

        return ",".join(str(x) for x in outputs)

def part1(input: str) -> int:
    computer = Intcode(input)
    outputs = computer.run()

    return outputs

def part2(input: str) -> int:
    lower = 0
    upper = 10**20
    mid = (lower + upper) // 2

    while True:
        computer = Intcode(input)
        computer.registers[0] = mid
        program = ",".join(str(x) for x in computer.program)
        outputs = computer.run()
        curr = int(outputs[::-1].replace(",", ""))
        curr2 = int(program[::-1].replace(",", ""))

        if curr > curr2:
            upper = mid
            mid = (lower + upper) // 2
            if mid not in [lower, upper]:
                continue
        elif curr < curr2:
            lower = mid
            mid = (lower + upper) // 2
            if mid not in [lower, upper]:
                continue

        i = lower

        while True:
            diff = 0
            computer = Intcode(input)
            computer.registers[0] = i
            program = ",".join(str(x) for x in computer.program)
            outputs = computer.run()

            curr = int(outputs[::-1].replace(",", ""))
            curr2 = int(program[::-1].replace(",", ""))
            diff = abs(curr - curr2)

            if outputs == program:
                break

            if diff > 100_000_000_000:
                i += 100_000_000
            elif diff > 100_000_000:
                i += 1_000_000
            elif diff > 100_000:
                i += 1_000
            else:
                i += 1
        else:
            continue
        break

    return i

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))
















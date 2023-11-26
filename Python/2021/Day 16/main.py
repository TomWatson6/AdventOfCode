

def calculate(values, outer_id):
    if outer_id in [5, 6, 7]:
        assert len(values) == 2

    if outer_id == 0:
        return sum(values)
    elif outer_id == 1:
        product = 1
        for value in values:
            product *= value
        return product
    elif outer_id == 2:
        return min(values)
    elif outer_id == 3:
        return max(values)
    elif outer_id == 5:
        greater = 1 if values[0] > values[1] else 0
        return greater
    elif outer_id == 6:
        less = 1 if values[0] < values[1] else 0
        return less
    elif outer_id == 7:
        equal = 1 if values[0] == values[1] else 0
        return equal
    else:
        assert False
        return -1
    

def decode(binary, outer_id, termination_length):
    version_total = 0
    values = []
    num_to_collect = termination_length 
    packets_remaining = termination_length 

    while len(binary) > 7:
        version = int(binary[:3], 2)
        binary = binary[3:]
        version_total += version

        type_id = int(binary[:3], 2)
        binary = binary[3:]

        if type_id == 4:
            value = ""
            while True:
                segment = binary[:5]
                binary = binary[5:]
                value += segment[1:]
                if segment[0] == '0':
                    break
            values.append(int(value, 2))
        else:
            length_type_id = int(binary[0])
            binary = binary[1:]
            if length_type_id == 0:
                length = int(binary[:15], 2)
                binary = binary[15:]
                version_value, outcome, b = decode(binary[:length], type_id, 0)
                version_total += version_value
                values.append(outcome)
                binary = binary[length:]
            else:
                amount = int(binary[:11], 2)
                binary = binary[11:]
                version_value, outcome, b = decode(binary, type_id, amount)
                version_total += version_value
                values.append(outcome)
                binary = b
                

        if packets_remaining > 0:
            packets_remaining -= 1

        if packets_remaining == 0 and num_to_collect > 0:
            assert len(values) >= num_to_collect
            break

    return (version_total, calculate(values, outer_id), binary)


def p1(output):
    print("Part 1:", output)

def p2(output):
    print("Part 2:", output)

with open("input.txt") as f:
    hexadecimal = f.read().strip()

binary = (bin(int(hexadecimal, 16))[2:]).zfill(len(hexadecimal) * 4)

version_total, outcome, remainder = decode(binary, 0, 0)

p1(version_total)

p2(outcome)



def get_input(path):
    with open(path, "rb") as f:
        new_line = False
        byte_count = 0
        bs = f.read(1)
        while bs:
            curr = bs.decode("utf-8")
            if new_line and curr == "\"":
                bs = f.read(2)
                bs = f.read(1)
                new_line = False
                continue
            elif not new_line and curr == "\"":
                bs = f.read(1)
                new_line = True
                continue

            output = bs.decode("utf-8")
            if curr == "\\":
                bs = f.read(1)
                output += bs.decode("utf-8")
                if bs.decode("utf-8") == "x":
                    bs = f.read(2)
                    output += bs.decode("utf-8")
            byte_count += 1
            bs = f.read(1)
    
    with open(path) as f:
        input = [x.strip() for x in f.readlines()]

    actual_count = 0

    for line in input:
        actual_count += len(line)

    return actual_count - byte_count

def get_input2(path):
    with open(path, "rb") as f:
        bs = f.read(1)
        encoded_count = 0

        while bs:
            b = bs.decode("utf-8")
            
            if b in ["\r", "\n"]:
                bs = f.read(1)
                continue

            if b in ["\\", "\""]:
                encoded_count += 1

            encoded_count += 1
            bs = f.read(1)
            
    
    with open(path) as f:
        input = [x.strip() for x in f.readlines()]

    actual_count = 0
    line_count = len(input)

    for line in input:
        actual_count += len(line)

    return (len(input) * 2) + (encoded_count - actual_count)

def count(s):
    counter = 0

    i = 0
    while i < len(s):
        if s[i] == "\\":
            if s[i + 1] == "x":
                i += 3
            else:
                i += 1
        counter += 1
        i += 1

    return counter


total = get_input("input.txt")
total2 = get_input2("input.txt")

print("Part 1:", total)
print("Part 2:", total2)
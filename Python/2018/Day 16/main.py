

with open("input.txt") as f:
    chunks = [x.strip() for x in f.read().split("\n\n") if x != ""]

T = chunks[:-1]
I = chunks[-1].split("\n")

print(T)
print(I)




























# Read the input file and store the numbers in a list
with open("simple_input.txt") as f:
    numbers = [int(line.strip()) for line in f]

# Mix the numbers
for i, n in enumerate(numbers):
    new_index = (i + n) % len(numbers)
    numbers[i], numbers[new_index] = numbers[new_index], numbers[i]

# Find the 1000th, 2000th, and 3000th numbers after 0
grove_coordinates = []
index = numbers.index(0)
for i in range(1000, 3001, 1000):
    index = (index + i) % len(numbers)
    grove_coordinates.append(numbers[index])

# Calculate the sum of the grove coordinates
result = sum(grove_coordinates)
print(result)


with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

def part1(passphrases):
    valid_count = 0
    for passphrase in passphrases:
        words = passphrase.split()
        if len(words) == len(set(words)):  # No duplicate words
            valid_count += 1
    return valid_count

def part2(passphrases):
    valid_count = 0
    for passphrase in passphrases:
        words = [''.join(sorted(word)) for word in passphrase.split()]  # Sort each word's letters
        if len(words) == len(set(words)):  # No two words are anagrams
            valid_count += 1
    return valid_count

print("Part 1:", part1(lines))
print("Part 2:", part2(lines))














class Folder:
    def __init__(self, parent):
        self.sub_dirs = []
        self.parent: Folder = parent
        self.value = 0


def write_file():
    with open("input.txt") as file:
        commands = list(i.split(" ") for i in filter(lambda x: x != "$ ls" and x[:3] != "dir", file.read().split("\n")))

    drive = Folder(None)
    cur_dir = drive

    for command in commands:
        if command[0] == "$":
            if command[-1] == "..":
                cur_dir.parent.value += cur_dir.value
                cur_dir = cur_dir.parent
            else:
                cur_dir.sub_dirs.append(Folder(cur_dir))
                cur_dir = cur_dir.sub_dirs[-1]
        else:
            cur_dir.value += int(command[0])
    while cur_dir != drive:
        cur_dir.parent.value += cur_dir.value
        cur_dir = cur_dir.parent
    return drive


def part1():
    def dfs(directory):
        for sub_dir in directory.sub_dirs:
            dfs(sub_dir)
        output[0] += directory.value * (directory.value < 100000)
    output = [0]
    drive = write_file()
    dfs(drive)
    return output[0]


def part2():
    def dfs(directory):
        for sub_dir in directory.sub_dirs:
            dfs(sub_dir)
        output[0] += (directory.value - output[0]) * (output[1] < directory.value < output[0])

    drive = write_file()
    output = [drive.value, drive.value - 40000000]
    dfs(drive)
    return output[0]


print(f"Part 1: {part1()}\nPart 2: {part2()}")

# from collections import defaultdict as dd
# import sys

# sys.setrecursionlimit(9999999)


# class directory:
#     # def __init__(self, name, parent):
#     #     self.name = name
#     #     self.parent = parent
#     #     self.files = {}
#     #     self.directories = {}
    
#     def __init__(self, name):
#         self.name = name
#         self.dir = []
#         self.files = []

#     def process(self, lines):
#         for line in lines:
#             parts = line.split(" ")


#     def navigate(self, name):
#         if self.name == name:
#             return self
        
#         for dir in self.directories.values():
#             if dir.name == name:
#                 return dir

#             found = dir.navigate(name)
#             if found is not None:
#                 return found

#     def calc_dir_sizes(self, sizes):
#         for file in self.files.values():
#             sizes[self.name] += file[1]

#         for dir in self.directories.values():
#             dir.calc_dir_sizes(sizes)
#             sizes[self.name] += sizes[dir.name]

# def map_file_system(lines):
#     root = directory("root", ".")
#     curr = root

#     for i, line in enumerate(lines):
#         print(i, line)
#         parts = line.split(" ")

#         if parts[0] == "$":
#             if parts[1] == "cd":
#                 if parts[2] == "/":
#                     curr = root
#                 elif parts[2] == "..":
#                     curr = curr.parent
#                     # curr = root.navigate(curr.parent)
#                 else:
#                     curr = curr.navigate(parts[2])
#             else:
#                 continue
#         else:
#             if parts[0] == "dir":
#                 curr.directories[parts[1]] = directory(parts[1], curr)
#             else:
#                 curr.files[parts[1]] = (parts[1], int(parts[0]))

#     return root

# with open("input.txt") as f:
#     lines = [x.strip() for x in f.readlines()]

# file_system = directory(lines, "root")

# file_system = map_file_system(lines)

# print(file_system)

# sizes = dd(lambda: 0)
# file_system.calc_dir_sizes(sizes)

# print(sum([x for x in sizes.values() if x <= 100000]))

# def calc_dir_sizes(curr, parents, children, files, sizes):
#     for child in children[curr]:
#         sizes[curr] += sum([f[1] for f in files[child]])
#         calc_dir_sizes(child, parents, children, files, sizes)

#     for file in files[curr]:
#         sizes[curr] += file[1]


    # for file in files.values():
    #     sizes[self.name] += file[1]

    # for dir in self.directories.values():
    #     dir.calc_dir_sizes(sizes)
    #     sizes[self.name] += sizes[dir.name]

# with open("input.txt") as f:
#     lines = [x.strip() for x in f.readlines()]

# children = dd(lambda: [])
# parents = {}
# files = dd(lambda: [])

# curr = "root"

# for line in lines:
#     parts = line.split(" ")

#     if parts[0] == "$":
#         if parts[1] == "cd":
#             if parts[2] == "/":
#                 curr = "root"
#             elif parts[2] == "..":
#                 curr = parents[curr]
#             else:
#                 curr = parts[2]
#         else:
#             continue
#     else:
#         if parts[0] == "dir":
#             children[curr].append(parts[1])
#             if parts[1] in parents:
#                 print("HOLY SHIT THIS IS INSANE!!")
#             parents[parts[1]] = curr
#         else:
#             files[curr].append((parts[1], int(parts[0])))

# # print(parents, children, files)

# sizes = dd(lambda: 0)
# calc_dir_sizes("root", parents, children, files, sizes)
# print("Some random bullshit")

# # print(sizes)

# total = 0

# for size in sizes.values():
#     if size <= 100000:
#         total += size

# print(total)






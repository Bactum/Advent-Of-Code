import os

file = os.path.join("./data", "input2.txt")

horizontal = 0
horizontal_2 = 0
depth = 0
depth_2 = 0
aim = 0
part1 = 0
part2 = 0

with open(file) as read:
    for line in read:
        line = line.split(" ")
        if "forward" in line:
            horizontal += int(line[1])
            horizontal_2 += int(line[1])
            depth_2 += aim * int(line[1])
        if "up" in line:
            depth += int(line[1])
            aim -= int(line[1])
        if "down" in line:
            depth -= int(line[1])
            aim += int(line[1])
    part1 = horizontal * depth
    part2 = horizontal_2 * depth_2
    print(f"Day 2 Part 1: {abs(part1)}\nDay 2 Part 2: {abs(part2)}")

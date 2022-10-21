import os

file = os.path.join("./data", "input3.txt")
data = []
bit = ["", "", "", "", "", "", "", "", "", "", "", ""]
gamma = ""
epsilon = ""


def sorting():
    for line in read:
        data.append(line)
        for i in range(0, 12):
            bit[i] += line[i]


def part_1():
    global gamma
    global epsilon
    for a in range(0, 12):
        if bit[a].count("0") > bit[a].count("1"):
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    print(int(gamma, 2) * int(epsilon, 2))


def part_2():
    global bit
    oxygen_generator_rating = ""
    CO2_scrubber_rating = ""
    for b in data:
        if bit[b].count("0") > bit[b].count("1"):
            if data[b][b] == "1":
                data.remove(b)
            elif data[b][b] == "0":
                data.remove(b)
    life_support_rating = int(oxygen_generator_rating, 2) * int(CO2_scrubber_rating, 2)


print(data)


with open(file) as read:
    sorting()
    part_1()
    #    print(gamma)
    part_2()

file = 'C:\\Users\\daniel.weigel\\Documents\\Visual Studio 2022\\GIT\\Advent-Of-Code\\2022\\data\\day21.txt'

data = []
lines = []
numbers = {}
numbers2 = {}
human = 21973580688000
with open(file, 'r') as read:
    data = read.read().split('\n')
    for i in data:
        lines.append(i.split())
    for elements in lines:
        if elements[1].isdigit():
            numbers[elements[0]] = int(elements[1])
    while 'root:' not in numbers:
        for elements in lines:
            if len(elements) > 2:
                if str(elements[1] + ':') in numbers:
                    if str(elements[3] + ':') in numbers:
                        if elements[2] == '+':
                            numbers[elements[0]] = (numbers[elements[1] + ':'] + numbers[elements[3] + ':'])
                        elif elements[2] == '-':
                            numbers[elements[0]] = (numbers[elements[1] + ':'] - numbers[elements[3] + ':'])
                        elif elements[2] == '*':
                            numbers[elements[0]] = (numbers[elements[1] + ':'] * numbers[elements[3] + ':'])
                        elif elements[2] == '/':
                            numbers[elements[0]] = (numbers[elements[1] + ':'] // numbers[elements[3] + ':'])
            else:
                continue
    print(numbers['pttp:'])
        
    for elements in lines:
        if elements[1].isdigit():
            numbers2[elements[0]] = int(elements[1])
    while 'root:' not in numbers2 or numbers2['root:'] is False:
        print(human)
        for elements in lines:
            if elements[0] == 'root:':
                elements[2] = '='
            if elements[0] == 'humn:':
                    numbers2['humn:'] = human
            if len(elements) > 2:
                if str(elements[1] + ':') in numbers2:
                    if str(elements[3] + ':') in numbers2:
                        if elements[2] == '+':
                            numbers2[elements[0]] = (numbers2[elements[1] + ':'] + numbers2[elements[3] + ':'])
                        elif elements[2] == '-':
                            numbers2[elements[0]] = (numbers2[elements[1] + ':'] - numbers2[elements[3] + ':'])
                        elif elements[2] == '*':
                            numbers2[elements[0]] = (numbers2[elements[1] + ':'] * numbers2[elements[3] + ':'])
                        elif elements[2] == '/':
                            numbers2[elements[0]] = (numbers2[elements[1] + ':'] // numbers2[elements[3] + ':'])
                        elif elements[2] == '=':
                            numbers2[elements[0]] = (numbers2[elements[1] + ':'] == numbers2[elements[3] + ':'])
                            human += 1
            else:
                continue

    print(f"Part 1: {numbers['root:']}\nPart 2 : {human}")
            
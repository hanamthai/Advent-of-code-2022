file = "D:\Advent_of_code_2022\Day12\input.txt"
data = open(file).read().strip()
lines = [x for x in data.split('\n')]

r = len(lines)
c = len(lines[0])

for i in range(r):
    for j in range(c):
        if lines[i][j] == 'S':
            print(i, ' ', j)

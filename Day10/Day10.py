infile = "D:\Advent_of_code_2022\Day10\input.txt"
data = open(infile, "r").read().strip()
lines = [x for x in data.split('\n')]

cycle = 0
previous_cycle = 0
value = 1
previous_value = 1

check = 20

save_val_of_cycles = []  # cycles value of 20, 60, 100, 140, 180, 220

for i in lines:
    line = i.split(' ')

    previous_cycle = cycle
    previous_value = value

    if line[0] == 'noop':
        cycle += 1
    elif line[0] == 'addx':
        cycle += 2
        value += int(line[1])

    if cycle >= check:
        save_val_of_cycles.append(previous_value*check)
        check += 40

    if cycle > 220:
        break


print(sum(save_val_of_cycles))

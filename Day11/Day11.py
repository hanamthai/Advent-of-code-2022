from collections import Counter

file = "D:\Advent_of_code_2022\Day11\input.txt"
data = open(file).read().strip()
lines = [x for x in data.split('\n\n')]

lst_monkeys = []

for i in lines:
    monkey = i.split('\n')

    items = [int(i) for i in monkey[1][18:].split(',')]
    operation = monkey[2][13:]
    test = int(monkey[3][21:])
    true = int(monkey[4][29:])
    false = int(monkey[5][30:])
    lst_monkeys.append((items, operation, test, true, false))

turn = 0
m = 0
counts = Counter()

while True:
    for i in range(len(lst_monkeys)):
        items, operation, test, true, false = lst_monkeys[i]
        for _ in range(len(items)):
            counts[i] += 1
            item = items[0]
            parts = operation.split()
            if parts[-1].isnumeric():
                a = int(parts[-1])
            else:
                a = item

            if parts[-2] == "*":
                items[0] = items[0] * a
            elif parts[-2] == "+":
                items[0] = items[0] + a
            items[0] = items[0] // 3

            if items[0] % test == 0:
                lst_monkeys[true][0].append(lst_monkeys[i][0].pop(0))
            else:
                lst_monkeys[false][0].append(lst_monkeys[i][0].pop(0))

    turn += 1

    for m in lst_monkeys:
        print(m[0])

    if turn == 20:
        break

a = list(sorted(counts.values()))
print(a)

print(a[-1]*a[-2])

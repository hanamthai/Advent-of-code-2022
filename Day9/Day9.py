# Ý tưởng: Cho ba biến đếm:
# Một để lưu vị trí hiện tại của H
# Hai là để lưu vị trí trước đó của H
# Ba là để lưu vị trí của T

# Đầu tiên ta cho chạy từng line của step:
# cộng trừ tương ứng với từng U,D,L,R cho row and col của H

# Lấy trị tuyệt đối của row H trừ row T bằng với 2 hoặc trị tuyệt đối của column H - column T bằng 2
# thì ta gán giá trị row, col của T cho vị trí trước đó của H.


infile = "D:\Advent_of_code_2022\Day9\input.txt"
data = open(infile, "r").read().strip()
lines = [x for x in data.split('\n')]

cols, rows = 1000, 1000   # chọn đại một cái lưới cho lớn lớn.

grid = [['.' for i in range(cols)] for j in range(rows)]

row_H = 0
column_H = 0

privious_row_H = 0
privious_column_H = 0

row_T = 0
column_T = 0

# đánh dấu vị trí đầu tiên của T trước khi vào vòng lặp
grid[0][0] = '#'            # grid[row][column]


def calculate_step(col_H, r_H):
    global column_H, column_T, row_H, row_T, privious_column_H, privious_row_H
    for i in range(1, int(step[2:])+1):
        if col_H == 1:
            column_H += 1
        elif col_H == -1:
            column_H -= 1
        elif r_H == 1:
            row_H += 1
        elif r_H == -1:
            row_H -= 1
        if abs(column_H - column_T) == 2 or abs(row_H - row_T) == 2:
            row_T = privious_row_H
            column_T = privious_column_H
            grid[row_T][column_T] = '#'

        privious_column_H = column_H
        privious_row_H = row_H


for step in lines:
    if step[0] == 'R':
        calculate_step(1, 0)

    elif step[0] == 'L':
        calculate_step(-1, 0)

    elif step[0] == 'U':
        calculate_step(0, 1)

    elif step[0] == 'D':
        calculate_step(0, -1)


count_T = 0
for i in grid:
    count_T += i.count('#')
print(count_T)

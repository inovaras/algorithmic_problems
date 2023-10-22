from enum import Enum

ort = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def step_forward(x, y, dxy):
    return x + dxy[0], y + dxy[1]

def change_direction(dir):
    return (dir + 1) % 4

n = 7
m = 10
matrix = [[0 for j in range(m)] for i in range(n)]
matrix[0][0] = 1
i, j = 0, 0
num = 2
dir = 0
while num <= n * m:
    if i + ort[dir][0] < n and j + ort[dir][1] < m and matrix[i+ort[dir][0]][j+ort[dir][1]] == 0:
        matrix[i+ort[dir][0]][j+ort[dir][1]] = num
        i, j = step_forward(i, j, ort[dir])
        num += 1
    else:
        dir = change_direction(dir)

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end='\t')
    print()
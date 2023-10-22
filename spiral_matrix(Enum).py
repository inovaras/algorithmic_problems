from enum import Enum


class Ort(Enum):
    right = (0, 1)
    down = (1, 0)
    left = (0, -1)
    up = (-1, 0)


m = 5
n = 5
num = 1
matrix = [[0 for j in range(m)] for i in range(n)]


def step_forward(i, j, dxy):
    return i + dxy[0], j + dxy[1]


def next_direction(direction):
    if direction == Ort.right:
        return Ort.down
    elif direction == Ort.down:
        return Ort.left
    elif direction == Ort.left:
        return Ort.up
    else:
        return Ort.right


dir = Ort.right

i, j = 0, 0
matrix[i][j] = 1
num = 2
while num <= m * n:

    if i + dir.value[0] < n and j + dir.value[1] < m and matrix[i + dir.value[0]][j + dir.value[1]] == 0:
        matrix[i + dir.value[0]][j + dir.value[1]] = num
        i, j = step_forward(i, j, dir.value)
        num += 1
    else:
        dir = next_direction(dir)


for s in matrix:
    for d in s:
        print(d, end='\t')
    print()

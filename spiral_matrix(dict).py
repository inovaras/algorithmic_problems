ort = {'right': (0, 1), 'down': (1, 0), 'left': (0, -1), 'up': (-1, 0)}


def step_forward(x, y, dxy):
    return x + dxy[0], y + dxy[1]


def change_direction(dir):
    if dir == 'right':
        return 'down'
    elif dir == 'down':
        return 'left'
    elif dir == 'left':
        return 'up'
    else:
        return 'right'


n = 5
m = 15
matrix = [[0 for j in range(m)] for i in range(n)]
i, j = 0, 0
matrix[0][0] = 1
num = 2
dir = 'right'
while num <= n * m:
    if i + ort[dir][0] < n and j + ort[dir][1] < m and matrix[i + ort[dir][0]][j + ort[dir][1]] == 0:
        matrix[i + ort[dir][0]][j + ort[dir][1]] = num
        i, j = step_forward(i, j, ort[dir])
        num += 1
    else:
        dir = change_direction(dir)


for i in range(n):
    for j in range(m):
        print(matrix[i][j], end='\t')
    print()


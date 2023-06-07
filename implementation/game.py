n,m = map(int, input().split())
x, y, d = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

d = [[0] * m for _ in range(n)]
d[x][y] = 1

# N E S W
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt_move = 1
cnt_turn = 0

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

# start simulation
while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]
    if arr[nx][ny] == 0 and d[nx][ny] == 0:
        x = nx
        y = ny
        d[x][y] = 1
        cnt_move += 1
        cnt_turn = 0
        continue
    else:
        cnt_turn += 1
    if cnt_turn == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if arr[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        cnt_turn = 0
print(cnt_move)
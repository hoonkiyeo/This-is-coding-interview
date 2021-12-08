import sys

n,m = map(int, input().split())
check_array = [[0] * m for _ in range(n)]
x,y,direction = map(int, input().split())

#current location
check_array[x][y] = 1

#input array
array = []
for i in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))
array[x][y] = 1

#north -> east -> south -> west
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global direction
    direction = direction -1
    if direction == -1:
        direction = 3

cnt_move = 1
cnt_turn = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if array[nx][ny] == 0 and check_array[nx][ny] == 0:
        check_array[nx][ny] = 1
        x = nx
        y = ny
        cnt_move += 1
        cnt_turn = 0
        continue
    else:
        cnt_turn += 1

    if cnt_turn == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        cnt_turn = 0

print(cnt_move)

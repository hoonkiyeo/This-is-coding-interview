import sys
import time

n = int(input())
steps = list(input().split())
x,y = 1,1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def range_check(x,y,n):
    if x < 1:
        x += 1
    elif x > n:
        x -= 1
    elif y < 1:
        y += 1
    elif y > n:
        y -= 1
    return x, y

for step in steps:
    x, y = range_check(x,y,n)
    if step == 'L':
        x += dx[0]
        y += dy[0]
    elif step == 'R':
        x += dx[1]
        y += dy[1]
    elif step == 'U':
        x += dx[2]
        y += dx[2]
    elif step == 'D':
        x += dx[3]
        y += dy[3]

print(x,y)
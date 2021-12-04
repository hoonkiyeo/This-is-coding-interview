import sys
import time

n = int(sys.stdin.readline())
move = input().split()
x,y = 1, #start coordinates


for d in move:
    if d == "L":
        y -= 1
        if y < 1 or y > n:
            y += 1
            continue
    elif d == "R":
        y += 1
        if y < 1 or y > n:
            y += 1
            continue
    elif d == "U":
        x -= 1
        if x < 1 or x > n:
            x += 1
            continue
    elif d == "D":
        x += 1
        if x < 1 or x > n:
            x += 1
            continue

print(x,y, end = " ")

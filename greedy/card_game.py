import sys
import time


N,M = map(int, input().split())
board = [] #empty board
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split()))) #N*M board with input lists

max_min = 0
for row in board:
    if max_min < min(row):
        max_min = min(row)
        
print(max_min)

#Time complexity = O(N)

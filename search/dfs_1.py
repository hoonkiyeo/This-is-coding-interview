import sys

n,m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().strip())))
result = 0

def dfs(x,y):
    if x < 0 or y < 0 or x > n-1 or y > m-1:
        return False
    if arr[x][y] == 0:
        arr[x][y] = 1
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x, y-1)
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)
import sys

N,M,K = map(int, sys.stdin.readline().split()) # M <= 10,000
num_list = list(map(int, sys.stdin.readline().split()))

num_list.sort()
sum = 0
cnt = 0

for i in range(M):
    if cnt == K:
        sum += num_list[-2]
        cnt = 0
        continue
    sum += num_list[-1]
    cnt += 1

print(sum)

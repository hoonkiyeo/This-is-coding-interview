
N, M, K = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

cnt = 0
tot = 0

for i in range(M):
    if cnt == K:
        tot += num_list[-2]
        cnt = 0
    else:
        tot += num_list[-1]
        cnt += 1
print(tot)

#Time complexity = O(M)

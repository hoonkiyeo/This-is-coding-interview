import sys

if __name__ == "__main__":
    n,k = map(int, sys.stdin.readline().split())
    step_cnt = 0

    while True:
        if n == 1:
            break
        elif n % k == 0:
            n = n // k
            step_cnt += 1
        else:
            step_cnt += n % k
            n = n - (n % k)
    print(step_cnt)





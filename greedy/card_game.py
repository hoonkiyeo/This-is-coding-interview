import sys
import time


if __name__ == "__main__":
    n,m = map(int, sys.stdin.readline().split())
    result = 0
    start = time.time()
    for _ in range(n):
        arr = list(map(int, sys.stdin.readline().split()))
        min_val = 10001
        for num in arr:
            min_val = min(num, min_val)

        result = max(result, min_val)
    end = time.time()
    print(end - start)
    print(result)


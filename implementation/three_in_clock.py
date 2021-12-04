import sys


if __name__ == "__main__":
    hour = int(input())
    cnt = 0

    for i in range(hour+1):
        for j in range(60):
            for k in range(60):
                if "3" in str(i) or "3" in str(j) or "3" in str(k):
                    cnt += 1

    print(cnt)
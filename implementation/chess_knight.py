import sys

if __name__ == "__main__":

    location = input()
    if len(location) != 2:
        print("wrong input")

    dic = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}
    steps = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (-1,2), (1, -2), (-1,-2)]
    x,y = int(dic[location[0]]), int(location[1])
    cnt = 0

    for step in steps:
        x += step[0]
        y += step[1]
        if x >=1 and x <= 8 and y >=1 and y <= 8:
            cnt += 1
        x, y = int(dic[location[0]]), int(location[1])
        continue

    print(cnt)









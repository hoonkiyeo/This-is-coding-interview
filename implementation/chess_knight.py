if __name__ == "__main__":

    loc = input()
    row = int(loc[1])
    col = int(ord(loc[0])) - int(ord("a")) + 1

    steps = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (-1,2), (1, -2), (-1,-2)]
    cnt = 0

    for step in steps:
        new_row = row + step[0]
        new_col = col + step[1]
        if new_row >=1 and new_row <= 8 and new_col >=1 and new_col <= 8:
            cnt += 1
        continue

    print(cnt)








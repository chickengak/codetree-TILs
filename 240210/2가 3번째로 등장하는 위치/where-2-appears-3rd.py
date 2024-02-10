garbage = input()
cnt = 0
for idx, num in enumerate(list(map(int, input().split()))):
    if num == 2:
        if cnt == 2:
            print(idx+1)
            break
        cnt += 1
for idx in range(len(l:=list(map(int, input().split())))):
    if l[idx]%3 == 0:
        print(l[idx-1])
        break
loop = 6
while loop:=loop-1:
    if (n:=int(input()))%3:
        print(0)
        break
else:
    print(1)
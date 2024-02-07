temp = None
for n in list(map(int, input().split())):
    if n%3:
        temp = n
    else:
        print(temp)
        break
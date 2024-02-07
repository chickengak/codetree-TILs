num = 0
for i in range(n:=int(input())):
    if i%2 == 0:
        print(' '.join([str(i) for i in range(num+1, num+1+n)]))
        num = num + n
    else:
        print(' '.join([str(i) for i in range(num+2, num+1+2*n, 2)]))
        num = num + 2*n
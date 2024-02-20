d = dict()
for i in range(36):
    if i < 10:
        d[str(i)] = i
    else:
        d[chr(i+55)] = i

n, A = list(input().split())
A = int(A)

num = 0
for i in range(len(n)):
    num += d[n[len(n)-i-1]] * (A**i)

print(num)
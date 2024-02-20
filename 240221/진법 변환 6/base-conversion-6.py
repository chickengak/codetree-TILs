d = dict()
for i in range(36):
    if i < 10:
        d[str(i)] = i
        d[i] = str(i)
    else:
        d[chr(i+87)] = i
        d[i] = chr(i+87)

A, n, B = list(input().split())
A, B = int(A), int(B)


num = 0
for i in range(len(n)):
    num += d[n[len(n)-i-1]] * (A**i)

res = []
exp = 1
while num:
    share, remainder = divmod(num, (B**exp))
    res.append(remainder)
    num = share
    exp += 1

print(''.join([d[r] for r in res[::-1]]))
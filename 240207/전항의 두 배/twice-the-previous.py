l = list(map(int, input().split()))
for idx in range(8):
    l.append(l[idx]*2 + l[idx+1])
print(' '.join(map(str, l)))
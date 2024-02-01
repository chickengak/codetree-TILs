a, b = list(map(int, input().split()))
if a%2: a+=1
print(' '.join(str(n) for n in range(a, b+1, 2)))
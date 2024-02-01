a, b = list(map(int, input().split()))
print(' '.join(map(str, [n for n in range(a, b+1) if n%2])))
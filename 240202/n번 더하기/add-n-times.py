a, n = list(map(int, input().split()))
print('\n'.join(map(str, [a:=a+n for _ in range(n)])))
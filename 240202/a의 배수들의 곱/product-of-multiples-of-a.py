a, b = list(map(int, input().split()))
ans = 1
for n in range(a, b+1, a):
    ans *= n
print(ans)
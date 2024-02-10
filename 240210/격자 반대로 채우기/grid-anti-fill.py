n = int(input())

mat = [list(range(r*n+1, (r+1)*n+1)) if r%2 else list(range((r+1)*n, r*n, -1)) for r in range(n)]
for r in range(n):
    for c in range(n-1, -1, -1):
        print(mat[c][r], end=' ')
    print()
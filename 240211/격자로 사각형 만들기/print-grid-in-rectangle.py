n = int(input())
mat = [[1]*n]
for _ in range(n-1):
    mat.append([1]*n)
for r in range(1, n):
    for c in range(n):
        if c == 0:
            continue
        mat[r][c] = mat[r][c-1] + mat[r-1][c] + mat[r-1][c-1]

print(*[' '.join(map(str, r)) for r in mat], sep='\n')
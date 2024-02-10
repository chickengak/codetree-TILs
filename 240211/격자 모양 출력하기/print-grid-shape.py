n, dots = list(map(int, input().split()))
mat = [[0]*n for _ in range(n)]
for _ in range(dots):
    r, c = list(map(int, input().split()))
    mat[r-1][c-1] = r*c
print(*[' '.join(map(str, r)) for r in mat], sep='\n')
n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
if n > 1:
    for i in range(1, n):
        mat[0][i] = min(mat[0][i - 1], mat[0][i])

for row in range(1, n - 1):
    for col in range(0, n):
        if col == 0:
            mat[row][0] = min(mat[row - 1][0], mat[row][0])
        else:
            mat[row][col] = min((mat[row - 1][col]), (mat[row][col - 1]), mat[row][col])
if n > 1:
    for i in range(n):
        mat[-1][i] = min(mat[-1][i], mat[-2][i])
print(max(mat[-1]))
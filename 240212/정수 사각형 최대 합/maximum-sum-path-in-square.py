n = int(input())
mat = [ list(map(int, input().split())) for _ in range(n)]
for i in range(1, n):
    mat[0][i] += mat[0][i-1]

for row in range(1, n):
    for col in range(0, n):
        if col == 0:
            mat[row][0] += mat[row-1][0]
        else:
            mat[row][col] += max((mat[row-1][col]), (mat[row][col-1]))
print(max(mat[-1]))
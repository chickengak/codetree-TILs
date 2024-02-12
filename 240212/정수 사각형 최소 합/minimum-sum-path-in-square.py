n = int(input())
mat = [ list(map(int, input().split())) for _ in range(n)]
for i in range(n-2,-1,-1):
    mat[0][i] += mat[0][i+1]

for row in range(1, n):
    for col in range(n-1, -1, -1):
        if col == n-1:
            mat[row][col] += mat[row-1][col]
        else:
            mat[row][col] += min((mat[row-1][col]), (mat[row][col+1]))
print(mat[-1][0])
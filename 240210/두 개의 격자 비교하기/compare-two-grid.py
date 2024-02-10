row, col = list(map(int, input().split()))

mat1 = [list(map(int, input().split())) for _ in range(row)]
mat2 = [list(map(int, input().split())) for _ in range(row)]
print('\n'.join([ ' '.join(['0' if mat1[r][c] == mat2[r][c] else '1' for c in range(col)]) for r in range(row)]))
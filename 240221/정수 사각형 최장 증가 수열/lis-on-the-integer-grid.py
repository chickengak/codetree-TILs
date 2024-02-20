n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
bfs = [[0]*n for _ in range(n)]

mins = []
minimum = 500
for r in range(n):
    for c in range(n):
        if mat[r][c] == minimum:
            mins.append((r, c))
        elif mat[r][c] < minimum:
            minimum = mat[r][c]
            mins = [(r, c)]

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
cnt = 1
while mins:
    cnt += 1
    nexts = []

    for m in mins:
        for d in dirs:
            r = m[0] + d[0]
            c = m[1] + d[1]

            if  0 <= r < n and 0 <= c < n:
                if mat[r][c] > mat[m[0]][m[1]]:
                    bfs[r][c] = cnt
                    nexts.append((r, c))
    mins = nexts

print(cnt-1)
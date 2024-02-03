n = int(input())
print('\n'.join([' '.join([str(col) for col in range(n*row, 0, -row)]) for row in range(1, n+1)]))
a, b = list(map(int, input().split()))
print('\n'.join([' / '.join([f"{col} * {row} = {col*row}" for col in range(b, a-1, -1)]) for row in range(2, 9, 2)]))
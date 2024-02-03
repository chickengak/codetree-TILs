n = int(input())
print('\n'.join([' '.join([str(i) for i in range(n, 0, -1)]) for _ in range(n)]))
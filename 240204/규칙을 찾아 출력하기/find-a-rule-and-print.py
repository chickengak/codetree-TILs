n = int(input())
print('\n'.join([' '.join('*'*n)] + ['* '*i + '  '*(n-i-1) + '*' for i in range(1, n)]))
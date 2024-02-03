n = int(input())
print('\n\n'.join((temp:=['*'*i for i in range(1, n)])+['*'*n]+temp[::-1]))
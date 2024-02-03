n = int(input())
print('\n'.join([(temp:= '*'*(n-i) + ' '*i) + temp[::-1] for i in range(n)]))
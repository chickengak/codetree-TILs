n = int(input())
print('\n'.join((temp:= [' '*(n-i) + '* '*i for i in range(1, n+1)]) + temp[:len(temp)-1][::-1]))
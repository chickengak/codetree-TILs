string = '987654321'*(((n:=int(input()))*n)//9 +1)
print('\n'.join([string[i*n:i*n +n] for i in range(n)]))
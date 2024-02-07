num = -1  # A 65  Z 90
print('\n'.join(['  '*row + ' '.join([chr( (num:= (num+1)%26)+65)  for _ in range(n-row)]) for row in range(n)]) if (n:=int(input())) else None)
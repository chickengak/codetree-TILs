from math import gcd

a, b = list(map(int, input().split()))
print(1 if gcd(a, b)>1 else 0)
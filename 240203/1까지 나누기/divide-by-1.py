n = int(input())
t = 1
while n > 1:
    n /= t
    t += 1
print(t-1)
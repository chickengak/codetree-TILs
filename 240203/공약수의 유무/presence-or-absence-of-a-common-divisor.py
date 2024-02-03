cd = [1]
for n in range(2, int(1920**0.5)+1):
    if 1920%n==0 and 2880%n==0:
        cd += [n, 1920//n]

a, b = list(map(int, input().split()))
for n in range(a, b+1):
    if n in cd:
        print(1)
        break
else:
    print(0)
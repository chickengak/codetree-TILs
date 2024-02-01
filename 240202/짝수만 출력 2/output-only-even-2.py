b, a = list(map(int, input().split()))
while b >= a:
    if not b%2:
        print(b, end=' ')
    b -= 1
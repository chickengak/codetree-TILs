ans = 0
cnt = 0
while (n:= int(input())):
    if n > 29 or n < 20:
        break
    ans += n
    cnt += 1
print(f"{ans/cnt:.2f}")
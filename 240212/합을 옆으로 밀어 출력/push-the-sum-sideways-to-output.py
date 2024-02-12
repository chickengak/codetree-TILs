total = 0
for _ in range(int(input())):
    total += int(input())
print(str(total)[1:] + str(total)[0])
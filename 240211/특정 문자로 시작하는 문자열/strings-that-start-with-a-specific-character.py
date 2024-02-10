n = int(input())
strings = [input() for _ in range(n)]
c = input()
cnt, total = 0, 0
for string in strings:
    if c == string[0]:
        cnt += 1
        total += len(string)
print(f"{cnt} {total/cnt:.2f}")
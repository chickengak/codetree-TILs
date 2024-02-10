from collections import defaultdict

res = defaultdict(lambda : 0)
a, b = list(map(int, input().split()))
while a > 1:
    a, remainder = divmod(a, b)
    res[remainder] += 1

print(sum([v**2 for v in res.values()]))
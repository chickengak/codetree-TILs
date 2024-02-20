from math import ceil, floor

nums = list(map(float, input().split()))
print(ceil(nums.pop(nums.index(max(nums)))), end = ' ')
print(floor(nums.pop(nums.index(min(nums)))), end = ' ')
print(round(nums.pop()))
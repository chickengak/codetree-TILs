from math import ceil, floor

nums = list(map(float, input().split()))
nums[nums.index(temp)] = ceil((temp:=max(nums)))
nums[nums.index(temp)] = floor((temp:=min(nums)))
print(*[n if isinstance(n, int) else round(n) for n in nums ])
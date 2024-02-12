from collections import deque

s1 = deque(input())
s2 = deque(input())
for i in range(len(s1)):
    if s1 == s2:
        print(i)
        break
    s1.appendleft(s1.pop())
else:
    print(-1)
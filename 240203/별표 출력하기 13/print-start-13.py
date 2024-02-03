nlist = list(range(1, int(input())+1))
popback = True
ans = []
while nlist:
    ans.append('* ' * nlist.pop() if popback else '* ' * nlist.pop(0))
    popback = not popback
print('\n'.join(ans + ans[::-1]))
trash = input()
minimum = 100
for i in range(len((l:=list(map(int, input().split()))))-1):
    if minimum > (dif:=l[i+1]-l[i]):
        minimum = dif
print(minimum)
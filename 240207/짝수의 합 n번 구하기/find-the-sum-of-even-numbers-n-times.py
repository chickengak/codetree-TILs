for _ in range((tcase:=int(input()))):
    a, b = [temp[0]+1, temp[1]] if (temp := list(map(int, input().split())))[0]%2 else temp
    print(sum([i for i in range(a, b+1, 2)]))
print(a if (a:=(a+3 if (a:=int(input()))%2 else a))%3 else a//3)
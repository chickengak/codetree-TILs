for age, sex in [temp:=input().split(), temp:=input().split()]:
    if int(age) >= 19 and sex == 'M':
        print(1)
        break
else:
    print(0)
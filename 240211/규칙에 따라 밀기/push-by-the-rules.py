string = input()
commands = input()
r = commands.count('L')
print((string+string)[(t:=(2*r-len(commands))%len(string)):t+len(string)])
n = input()
scores = []
for _ in range(4):
    scores.append(sum(list(map(int, input().split()[1:]))))

for i, score in enumerate(scores):
    print(chr(i+65), '-', score)
print(f"Class {chr(scores.index(max(scores))+65)} is winner!")
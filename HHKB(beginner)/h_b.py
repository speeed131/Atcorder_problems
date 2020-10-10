h, w = map(int, input().split())
s = [input() for i in range(h)]


count = 0

for i in range(h):
    for j in range(w):
        if j == w-1:
            break
        if s[i][j] == '.' and s[i][j+1] == '.':
            count += 1
        
        
for i in range(h):
    if i == h-1:
        break
    for j in range(w):
        if s[i][j] == '.' and s[i+1][j]  == '.':
            count += 1



print(count)
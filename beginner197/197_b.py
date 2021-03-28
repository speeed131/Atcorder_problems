h, w, x, y = map(int, input().split())

koma = [input() for i in range(h)]

# print(koma)

count = 0

for i in range(x-1):
  if koma[i][y-1] == '.':
    count += 1

print(count)
t = int(input())
xy = [map(int, input().split()) for _ in range(t)]
x, y = [list(i) for i in zip(*xy)]

# print(x, y)
# [2, 0, 1000000, 12345, 0] [6, 0, 1000000, 67890, 1000000]

for i in range(t):
  field = [a for a in range(x[i], y[i]+1)]
  print(field)
  # diff = y[t] - x[t]

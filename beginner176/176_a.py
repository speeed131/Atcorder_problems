import math
n, x, t = map(int, input().split())

k = math.ceil(n / x)

print(k * t)


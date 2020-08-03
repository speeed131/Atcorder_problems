import math
import decimal
N, D = map(int,input().split())
x = []
for i in range(N):
    a,b=input().split()
    x.append([int(a), int(b)])

count = 0


for i in range(N):
    a = math.sqrt(x[i][0]**2 + x[i][1]**2)
    # ans = math.sqrt((x[i][0])^2 + (x[i][1])^2)
    if a <= D:
        count += 1

print(count)
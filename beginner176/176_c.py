n = int(input())
a = list(map(int, input().split()))

count = 0
for i in range(1, n):
    if a[i] < a[i-1]:
        dif = a[i-1] - a[i]
        count += dif
        a[i] += dif

print(int(count))
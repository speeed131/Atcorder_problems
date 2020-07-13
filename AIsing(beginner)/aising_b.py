N = int(input())
a = list(map(int, input().split()))

count = 0

for i in range(1, N + 1):
    if i % 2 != 0:
        if a[i - 1] % 2 !=0:
            count += 1

print(count)


#_______こっちのほうがきれい
# for i in range(0, N, 2):
#     if a[i] % 2 == 1:
#         count += 1

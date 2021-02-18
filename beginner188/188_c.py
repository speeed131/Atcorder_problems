import copy

n = int(input())
A = list(map(int, input().split()))
a = copy.deepcopy(A)
count = 2**n // 2
ans_num = 0

for j in range(n):
    for i in range(count):
        print(i)
        if a[2*i+1] > a[2*i]:
            a.pop(2*i)
        else:
            a.pop(2*i+1)

    count = count // 2

    if j == n-2:
        print(a)
        if a[0] > a[1]:
            ans_num = a[1]
        else:
            ans_num = a[0]
        break

print(A.index(ans_num) + 1)
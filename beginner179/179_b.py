n = int(input())

count = 0
for i in range(n):
    a, b = map(int, input().split())


    if count == 3:
        continue
    else:
        if a == b:
            count+=1
        else:
            count = 0



if count == 3:
    print('Yes')
else:
    print('No')
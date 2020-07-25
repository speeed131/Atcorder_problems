A, B, C = map(int,input().split())

K = int(input())

flag = False

for i in range(0, K+1):
    for j in range(0, K+1):
        for k in range(0, K+1):
            x = A * 2**i
            y = B * 2**j
            z = C * 2**k
            # print(x, y, z)

            if x < y < z and i + j + k <= K:
                flag = True


if flag == True:
    print('Yes')
else:
    print('No')
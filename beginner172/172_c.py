N, M, K = map(int,input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

maxcount = N + M


sum_money = []

for i in range(maxcount):
    if sum(sum_money) > K:
        break
    else:
        if not A:
            sum_money.append(B[0])
            B.pop(0)
        elif not B:
            sum_money.append(A[0])
            A.pop(0)
        else:
            if  A[0] > B[0]:
                sum_money.append(B[0])
                B.pop(0)

            elif A[0] < B[0]:
                sum_money.append(A[0])
                A.pop(0)

if not A and not B:
    print(len(sum_money))
elif len(sum_money) == 0:
    print(0)
else:
    print(len(sum_money) - 1)
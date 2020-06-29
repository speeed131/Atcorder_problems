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


#     a0 =0, a1 = A1, a2 = A1+A2, a3 = A1+A2+A3, . . . , aN = A1+. . .+AN とします。b0, b1, . . . , bM も同様に定義します。これらの値をプログラムで求める際は、a1 = a0+A1, a2 = a1+A2, a3 = a2+A3, . . .
# などとします (毎回 A1 から足していくと時間切れになります)。すると、机 A から i 冊、机 B から
# j 冊読むことを考えれば、問題は次のように言い換えられます。
# ✓ ✏
# 整数 i, j (0 ≤ i ≤ N, 0 ≤ j ≤ M) を ai + bj ≤ K となるように選ぶとき、i + j がとりうる最
# 大の値を求めよ。
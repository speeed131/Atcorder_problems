'''
M個調べる
A1 + A2
B1 + B2
C1 + C2
D1 + D2
すべての？[i]で １０以上、さらに
'''

N, M, X = map(int, input().split())

C = []
A = []
for i in range(N):
    t = list(map(int, input().split()))
    C.append(t[0])
    A.append(t[1:]) # 1から最後まで

result = -1

# << は 左への bit シフト。 シフトした分、１０進数で2^N分増える
#全検索
for i in range(2 << N):
    # t 
    t = [0] * M 
    c = 0

    for j in range(N):
        #以下フラグが立っていなかったら、
        if (i >> j) & 1 == 0:
            continue #以下処理を飛ばしてforに戻る
        # cに金額を足している
        c += C[j]
        for k in range(N):
            t[k] += A[j][k]
    if all(x >= X for x in t):
        if result == -1:
            result = c
        else:
            result = min(result, c)
print(result)
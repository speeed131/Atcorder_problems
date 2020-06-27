# 操作回数の最小値

S = input() #ここで標準入力
T = input() #ここで標準入力

length = len(S)
count = 0

for i in range(length):
    if S[i] != T[i]:
        count += 1

print(count)

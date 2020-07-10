
# def changeMin(a, b):
#     if a > b:
#         a = b

# def changeMax(a, b):
#     if a < b:
#         a = b

# １，DP配列全体を「DPの種類に応じた初期値」で初期化

# ２，初期条件を入力

# ３，ループを回す

# ４，テーブルから解を得て出力



N = int(input())
h = list(map(int, input().split()))


#dp[i] = カエルが足場iへと移動するのに必要な最小コスト
dp = []

dp.append(0)

#飛んだ対象をiとする
''' 
i-2 や i-1から飛んでくるが、
【[i-2]や[i-1]までの最適な進み方はわかっている】
という前提で進める。
'''
# [i-1] から遷移した場合、 [i-2]から遷移した場合
# dp[i-1] + abs(h[i] - h[i-1])
# dp[i-2] + abs(h[i] - h[i-2])
# これらの低い法をdp[i]に入れていく。


# print(dp)

# [0]の要素を*10する
dp = [0] * N

dp[1] = abs(h[1] - h[0])
for i in range(2, N):
    # [i-1] から遷移した場合、 [i-2]から遷移した場合
    # dp[i-1] + abs(h[i] - h[i-1])
    # dp[i-2] + abs(h[i] - h[i-2])
    # これらの低い法をdp[i]に入れていく。
    dp[i] = min(dp[i-1] + abs(h[i] - h[i-1]), dp[i-2] + abs(h[i] - h[i-2]))

#ゴール地点の最小値を出す
print(dp[-1])





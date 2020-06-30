'''
a = a1 + a2 + a3 ・・・ai
b = b1 + b2 + b3 ・・・bj
a + b <= K なれば良い
そして、本の数の最大数を求めるから、
つまり、i + j の最大の値を求める

１，まず、考えられる解法が全検索である。
しかし、N=M=200000 の場合には間に合わない。

２，次にiについてのみ考える。
i = 0,1・・・N
そして、bj <= K-ai
であるようなjの最大値を求める。

i=0 のときのjの最大値は、 j = M, M-1 
このように降順に走査すると、最初に bj <= K-ai 左の式が成立したjを求める。
このjをbest0とする

i=1 のときに選択可能なjの最大値を求める。
この最大値はbest0以下であるため、ｊ＝best0から始めることができる
'''
N, M, K = map(int,input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

#リストだと、0から始まるため、i + jの最初を０にしている
a, b = [0], [0]
#足していった合計をリストに足している
for i in range(N):
    a.append(a[i] + A[i])
for i in range(M):
    b.append(b[i] + B[i])


ans, j = 0, M

'''
aのリストは低い数字からみて、bのリストは高い数字から見る
i=0 のときのjの最大値は、 j = M, M-1 
このように降順に走査すると、最初に bj <= K-ai 左の式が成立したjを求める。
このjをbest0とする

i=1 のときに選択可能なjの最大値を求める。
この最大値はbest0以下であるため、ｊ＝best0から始めることができる
'''
# N + 1 している理由は、0がリストの最初にあるため。
#そして、0から始まる

for i in range(N+1):
    if a[i] > K:
        break
    # print(a[i])
    while b[j] > K -a[i]:
        #降順なので−１している
        j -= 1
        print(b[j])
    #ansにi+jの最大値を返している
    ans = max(ans, i + j)
print(ans)




'''
n 個の正の整数 a[0],a[1],…,a[n−1] と正の整数 A が与えられる。これらの整数から何個かの整数を選んで総和が A になるようにすることが可能か判定せよ。可能ならば "YES" と出力し、不可能ならば "NO" と出力せよ。
【制約】 ・1≤n≤100 ・1≤a[i]≤1000 ・1≤A≤10000
【数値例】 1) 　n=3 　a=(7,5,3) 　A=10 　答え: YES (7 と 3 を選べばよいです)

2) 　n = 2 　a=(9,7) 　A=6 　答え: NO
'''



'''
for i in range(5):     # i は０〜４
    bitshift = 1 << i
    print(bitshift)
    print(bin(bitshift)) # (1 << i) は i ビット目に1を立てるという意味でもある
'''

N = int(input()) #ここで標準入力
a = list(map(int, input().split()))
A = int(input()) #ここで標準入力
j = 0

for bit in range(1 << N):
    sum = 0
    for j in range(j < N):
        if (bit & (1 << j)):
            sum += a[j]
            print(sum)
        
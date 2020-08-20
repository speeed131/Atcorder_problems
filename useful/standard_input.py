'''
標準入力を受け取る方法まとめ
'''

#___文字列や数値をそのままほしい場合___#

# 文字列 １行１つ
s = input()

# 文字列 １行２つ
s, t = input().split()

# 整数 １行１つ
s = int(input())

# 整数 １行２つ
n, m = map(int, input().split())

# 整数 複数行
import sys
a = []
for l in sys.stdin:
    a.append(int(l))



#___リストでほしい場合___#

# リスト 文字列 １行
a = input().split()

# リスト 整数   １行
a = list(map(int, input().split()))

# リスト 文字列 nが指定行
a = [input() for i in range(n)]

# リスト 整数 nが指定行
a = [int(input()) for i in range(n)]

#___二次元配列でほしい場合___#

#２次元配列 文字列 nが指定行 空白区切りで複数行列
a = [input().split() for l in range(n)]







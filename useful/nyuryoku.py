'''
標準入力を受け取る方法まとめ
'''

#____文字列や数値をそのまま___#

# 文字列 １行１つ
s = input()

# 文字列 １行２つ
s, t = input().split()

# 文字列 複数行 １つ

# 文字列 複数行 ２つ

# 整数 １行１つ
s = int(input())

# 整数 １行２つ
n, m = map(int, input().split())

import sys
a = []
for l in sys.stdin:
    a.append(int(l))



#____リストでほしい場合____#

# リスト 文字列 １行
a = input().split()

# リスト 整数   １行
a = list(map(int, input().split()))

# リスト 文字列 nが指定行
a = [input() for i in range(n)]

# リスト 整数 nが指定行
a = [int(input()) for i in range(n)]


#２次元配列 複数行複数列 
a = [input().split() for l in range(n)]




##
#1文字の標準入力
##

#Stringの場合
S = input() #ここで標準入力
print (type(S), S)
#<class 'str'> atcoder

#intの場合
N = int(input()) #ここで標準入力
print (type(N), N) 
#<class 'int'> 20

##
#2文字の標準入力
##

#Stringの場合
X, Y = input().split()
print(type(X), X, Y)
# <class 'str'> 12 34

#intの場合
X, Y = map(int,input().split())
print(type(X), X, Y)
# <class 'int'> 12 34


###
# Listの標準入力
##

# Stringの場合
hoge = input().split() 
print(type(hoge),hoge)
#<class 'list'> ['12','34']
print(type(hoge[0]),hoge[0])
# <class 'str'> 12

#intの場合
A = list(map(int, input().split()))
print(type(A), A)
# <class 'list'> [12, 34]
print(type(A[0]), A[0])
# <class 'int'> 12

# 複数行複合
list = []
for i in range(N):
    a,b=input().split()
    list.append((int(a), b))

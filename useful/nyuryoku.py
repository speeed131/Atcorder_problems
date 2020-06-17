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
# 復習が必要
N, M, X = map(int,input().split())


# list = []
# for i in range(N):
#     a,b=input().split()
#     list.append((int(a), b))

C = []
A = []

for i in range(N):
    t = list(map(int, input().split()))
    C.append(t[0])
    A.append(t[1:])

result = -1



N, K = map(int,input().split())
A = []
for _ in range(K):
    d = input()
    A += list(map(int, input().split()))


#集合にして、重複を除き、数を引く
print(N - len(set(A)))
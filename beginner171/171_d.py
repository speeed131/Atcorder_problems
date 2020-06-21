N = int(input()) #ここで標準入力
A = list(map(int, input().split()))
Q= int(input()) #ここで標準入力


list = []
for i in range(Q):
    a,b=input().split()
    list.append((int(a), int(b)))

for k in range(Q):
    for j in range(N):
        if list[k][0] == A[j]:
            while list[k][0] in A :
                A.remove(list[k][0])
                A.append(list[k][1])
        
    print(sum(A))


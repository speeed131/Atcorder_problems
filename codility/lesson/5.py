A = []
A[0] = 2
A[1] = 3
A[2] = 1
A[3] = 5

for i in range(len(A)):
    if len(A)-1 == i:
        return 0
    
    if A[i]+1 != A[i+1]:
        return A[i] + 1


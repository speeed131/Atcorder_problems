# A = list(map(int, input().split()))
A, B, C = map(int,input().split())

K = int(input())





for i in range(K):
    A = A * 2

    for j in range(K-i):
        B = B * 2

        for k in range(K-i-j):
            C = C * 2
            # if C > B > A:
            #     print('Yes')
            #     break
            print(A, B, C)

# if not C < B < A:
#     print('No')

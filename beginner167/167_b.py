A, B, C, K = map(int,input().split())

if K - A - B > 0:
    print(1 * A - (K - A - B) * 1)

elif K - A < 0:
    print(1 * K)

elif K - A - B <= 0:
    print(1 * A)











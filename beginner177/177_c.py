import math
n = int(input())
a = list(map(int, input().split()))
mod = 1000000007


ans = 0

for i in range(n):
    
    # for j in range(i + 1, n):
        ans += (a[i] * a[j]) % mod
ans = ans % mod

print(ans)
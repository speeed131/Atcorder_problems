n = int(input())
a = list(map(int, input().split()))
ans = 0
j = n-1

for i in range(n):
  # for j in range(i+1, n):
  ans += (a[i] -a[j-i])**2


print(ans)
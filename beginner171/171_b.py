N, K = map(int,input().split())

p = list(map(int, input().split()))

total = []

for i in range(K):
    total.append(min(p))
    p.remove(min(p))

print(sum(total))

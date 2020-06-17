X, N = map(int,input().split())
p = list(map(int, input().split()))

# <要素> in <要素>
# <要素> not in <集合>
p = set(p)
for i in range(101):
    if X - i not in p:
        print(X - i)
        break
    if X + i not in p:
        print(X + i)
        break

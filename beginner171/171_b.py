
N, K = map(int,input().split())

p = list(map(int, input().split()))

total = []

for i in range(K):
    total.append(min(p))
    p.remove(min(p))

print(sum(total))

# https://note.nkmk.me/python-list-sort-sorted/
# sortedを使ったほうが早い
# 下記は、sortedでpを昇順（低い順）にして新しいリストを作り、:Kでスライスしている。（[:K]の意味は、最初は0からｋ-1までの値を取得しているという意味。そしてsumで合計を出している。
# print(sum(sorted(p)[:K]))
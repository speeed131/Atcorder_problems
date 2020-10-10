n = int(input())
p = list(map(int, input().split()))

# kyounoslit = [i for i in range(200001)]

kara = set()

num = 0

for j in range(n):
    kara.add(p[j])

    for i in range (num, 200001):
        if i in kara:
            continue
        else:
            print(i)
            num = i
            break
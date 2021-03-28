n = int(input())
a = list(map(int, input().split()))

a = [bin(a) for a in a]

print(a)
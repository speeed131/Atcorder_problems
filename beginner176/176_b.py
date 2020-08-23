s = input()

n = 0
for i in range(len(s)):
    n += int(s[i])


if n % 9 == 0:
    print('Yes')
else:
    print('No')
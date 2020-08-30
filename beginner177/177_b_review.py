s = input()
t = input()

s_len =len(s)
t_len =len(t)
count = 0
ans = []



for i in range(s_len - t_len + 1):
    for j in range(t_len):
        if s[i:t_len + i][j] != t[j]:
            count += 1
    ans.append(count)
    count = 0

min_ans = min(ans)
print(min_ans)


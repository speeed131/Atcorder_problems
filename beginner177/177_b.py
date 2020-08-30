s = input()
t = input()

# print(t[0: 0])


# for i in reversed(range(len(t)+1)):
#     if t[0:i] in s:
#         print(len(t)-i)
#         break

# if t[0] not in s:
#     print(0)

len_t = len(t)
# print(len_t)

times = len(s) - len(t) + 1
# count = []

# for j in reversed(range(len_t+1)):
#     for i in range(times):
#         if t[0:j] in s[i:len_t+i]:
#             print(len_t - j-1 )
#             break
#     else:
#         continue
#     break

for i in range(len_t):
    for j in reversed(range(1, len_t+1)):
        if t[i:j] in s:
            if j-i -1 > 0:
                print(j-i -1)
            else:
                print(len_t - 1)
            break
    else:
        continue
    break


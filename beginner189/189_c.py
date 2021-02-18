# 1:33

# import collections

# n = int(input())
# a = list(map(int, input().split()))
# ans_list = []
# constNum = a[0]


# for i in range(n):
#   if constNum > a[i]:
#     ans_list.append(ans)
#     constNum = a[i]
#   elif  n-1 == i:
#     ans = constNum * (i+1)
#     ans_list.append(ans)
#     constNum = a[i]
#   constNum += constNum



# print(ans_list)


N = int(input())
a = list(map(int, input().split()))

max_count = 0

for i in range(N):
  t_max_count = a[i]
  # print(t_max_count)
  for j in range(i, N):
    if a[j] < t_max_count:
      t_max_count = a[j]
    c = t_max_count * (j - i + 1)
    print(t_max_count)
    print(c)
    if c > t_max_count:
      t_max_count = c
  if t_max_count > max_count:
    max_count = t_max_count
print(max_count)





# counter_dict = collections.Counter(a)

# for key, value in counter_dict.items():
#   num = key * value




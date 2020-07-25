from operator import mul
from functools import reduce

N, K = map(int,input().split())
A = list(map(int, input().split()))

hyouten_count = N - K

result_list = []

result = 1
result_before = 1

for i in range(K-1, N):
    result = 1
    # print(num)
    # result = 1
    num = i-K+1
    result = reduce(mul, A[num:i+1])
    # for j in range(K):
    #     result = result * A[i - j]
    # print(result)
    # print(result)
    # result_list.append(result)
    if result_before == 1:
        pass
    elif result > result_before:
        print('Yes')
    else:
        print('No')
    result_before = result


# for n in range(1, len(result_list)):
#     if result_list[n] > result_list[n-1]:
#         print('Yes')
#     else:
#         print('No')
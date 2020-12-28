A = [9, 3, 9, 3, 9, 7, 9]

## 計算量と、１つの問題違い
# ans = 0
# for i in range(len(A)):
#     if A.count(A[i]) == 1:
#         ans = A[i]


# return ans
# print(ans)


A.sort()
for i in range (0, len(A), 2):
    if A[i] != A[i+1]:
        return A[i]
    
return A[len(A)-1]
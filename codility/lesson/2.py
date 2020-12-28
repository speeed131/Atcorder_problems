# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
A = [3, 8, 9, 7, 6]
K = 3

#テストでは、適当に値をおいておけばよき。
def solution(A, K):
    # write your code in Python 3.6
    len_A = len(A)
    new_array = [0 for i in range (len_A)]


    for i in range (len_A):
        array_location = (i + K) % len_A
        new_array[array_location] = A[i]

    return new_array


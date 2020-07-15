##___データが昇順 or 降順に並んでいる必要がある。
def binary_search(data_list, value):
    left  = 0
    right = len(data_list) - 1
    while left <= right:
        mid = (left + right)// 2
        if data_list[mid] == value:
            # 中央の値と一致した場合はリストの位置を返す
            return mid
        elif data_list[mid] < value:
            # 中央の値より小さい場合は、大きい探索範囲にするため、左端を変える
            left  = mid + 1
        elif data_list[mid] > value:
            # 中央の値より大きい場合は、小さい探索範囲にするため、右端を変える
            right = mid - 1
    return -1

data_list = [1, 2, 3, 4, 5, 6, 7, 8]

print(binary_search(data_list, 4))


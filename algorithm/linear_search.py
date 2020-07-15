a = [1, 2, 3, 4, 5]

for i in a:
    print(i)

for j in range(len(a)):
    print(j)

def linear_search(data_list, value):
    for data in data_list:
        if data == value:
            return data
    return -1

data_list = [1, 4, 5, 7, 9, 13]
print(linear_search(data_list, 8))



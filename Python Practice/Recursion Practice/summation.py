def sum(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum(list[1:])

num_list = (1, 2, 3, 4, 5)
result = sum(num_list)
print(result)

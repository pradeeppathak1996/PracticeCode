arr = [1,2,3,4,6,7]
arr1 = [1,2,3,4,5,8]

hash_map = {}
unique_arr = []

for i in arr:
    hash_map[i] = 1

for i in arr1:
    hash_map[i] = 1

for key in hash_map:
    unique_arr += [key]

print(unique_arr)

# [1, 2, 3, 4, 6, 7, 5, 8]
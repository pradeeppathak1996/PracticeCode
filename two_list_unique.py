arr = [1,2,3,4,6,7]
arr1 = [1,2,3,4,5,8]

unique_arr = []
hash_map = {}

for i in range(len(arr)):
    hash_map[arr[i]] = 1
for i in range(len(arr1)):
    hash_map[arr1[i]] = 1
    
for key in hash_map:
    unique_arr = unique_arr + [key]
    
print(unique_arr)
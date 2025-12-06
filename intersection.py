arr = [1,2,2,3,4,6,8,7]
arr1 = [1,2,2,3,4,5,8,12]

hash_map = {}
intersection = []

for i in arr:
    hash_map[i] = 1

for i in arr1:
     if i in hash_map:
          intersection += [i]

print(intersection)

# [1, 2, 2, 3, 4, 8]
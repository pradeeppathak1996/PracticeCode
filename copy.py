import copy

arr = [[1,2,3],[4,5,6]]

shallow = copy.copy(arr)
deep = copy.deepcopy(arr)

arr[0][0] = 100

print("Shallow:", shallow)
print("Deep:", deep)


# OUTPUT =

# Shallow:   [[100, 2, 3], [4, 5, 6]].  Only the outer object is copied, while the inner objects are shared.
# Deep:      [[1, 2, 3], [4, 5, 6]].    A completely independent copy is created, including all nested objects, with no sharing.
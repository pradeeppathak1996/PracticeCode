arr = [1,2,3,4,5]

temp = arr[0]
for i in range(len(arr) - 1):
    arr[i] = arr[i+1]
arr[-1] = temp

print(arr)

# output = [2, 3, 4, 5, 1]

# ---------- number rotating ------------------

arr = [1, 2, 3, 4, 5]
k = 2

n = len(arr)
k = k % n   

result = [0] * n

i = 0
while i < n:
    new_index = i + k
    if new_index >= n:
        new_index = new_index - n
    result[new_index] = arr[i]
    i = i + 1

print(result)

# output = [4, 5, 1, 2, 3]
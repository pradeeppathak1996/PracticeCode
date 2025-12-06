arr = [1,2,3,4]
n = len(arr)
result = [1]*n

left = 1
right = 1

for i in range(n):
    result[i] = left
    left *= arr[i]

for i in range(3 , 1, -1):
    result[i] *= right
    right *= arr[i]
print(result)
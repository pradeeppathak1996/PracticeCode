# While loop ----------

arr = [1,2,4,2,5,1,3,4,5,5]

seen = {}
arr1 = []
i = 0

while i < len(arr):
    num = arr[i]

    if num not in seen:
        seen[num] = 1
        arr1 += [num]
    i += 1

print(arr1)

# For loop ----------

arr = [1,2,4,2,5,1,3,4,5,5]

seen = {}
result = []

for i in arr:
    if i not in seen:
        seen[i] = 1
        result.append(i)
        
print(result)
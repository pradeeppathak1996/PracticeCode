arr = [1,2,4,2,5,1,3,4,5,5]

arr1 = []
i = 0

while i< len(arr):
    num = arr[i]
    if num not in arr1:
      arr1 += [num]
    i += 1
print(arr1)
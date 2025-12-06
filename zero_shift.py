arr = [2,4,0,1,5,0,8,9]

j = 0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[i] , arr[j] = arr[j] , arr[i]
        j += 1
        
print(arr)
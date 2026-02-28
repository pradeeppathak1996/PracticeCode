arr = [2,6,0,2,4,9]
num = 9
index = -1

for i in range(len(arr)):
    if arr[i] == num:
        index = i
        break
    
print(index)
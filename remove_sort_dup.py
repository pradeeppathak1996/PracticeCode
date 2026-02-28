arr = [1,1,2,2,3,3,3,4,4,5]

prev = 0
arr1 = []

for i in arr:
    if i != prev:    
        arr1 += [i]
        prev = i
print(arr1)
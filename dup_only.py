arr = [1,2,4,2,5,1,3,4,5,5,8]

i = 0

arr1 = []
dup = []

while i < len(arr):
    num = arr[i]
    if num not in arr1:
        arr1 +=[num]
    elif num not in dup:
        dup += [num]
    i += 1  

print(dup)
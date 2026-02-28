arr = [1,3,3,1,8]
unique = 0
i = 0
while i < len(arr):
    unique = unique ^ arr[i]
    i += 1
print(unique)

# --------------------------

arr = [2,5,9,1,3,5,9,0,2,6]

freq = {}
i = 0

while i < len(arr):
    num = arr[i]
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
    i += 1
    
unique = []
j = 0
while j < len(arr):
    if freq[arr[j]] == 1:
        unique += [arr[j]]
    j += 1
print(unique)
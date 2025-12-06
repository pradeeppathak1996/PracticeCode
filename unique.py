arr = [1,3,2,5,2,1]
unique = 0
i = 0
while i < len(arr):
    unique = unique^ arr[i]
    i += 1
print(unique)

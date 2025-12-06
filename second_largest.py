# Largest value -----------------------------

arr = [2,6,3,8,0,1]
largest = 0
for i in range(len(arr)):
    if arr[i] > largest:
        largest = arr[i]
print(largest)

# Second largest value -----------------------

arr = [2,6,3,8,0,1]   
largest = 0
second_largest = 0

for i in range(len(arr)): 
    if largest < arr[i]:
        second_largest = largest
        largest = arr[i]
    elif arr[i]< largest and arr[i] > second_largest:
             second_largest= arr[i]
print(second_largest)

# Third largest value ------------------------

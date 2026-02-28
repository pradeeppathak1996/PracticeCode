# Largest value ------------------

arr = [2,6,3,8,0,1]
largest = 0
for i in range(len(arr)):
    if arr[i] > largest:
        largest = arr[i]
print(largest)

# Second largest value ------------------

arr = [2,6,3,8,0,1]  

largest = 0
second_largest = 0

for i in range(len(arr)): 
    if largest < arr[i]:
        second_largest = largest
        largest = arr[i]
    elif arr[i] < largest and arr[i] > second_largest:
             second_largest= arr[i]

print(second_largest)

# Second lowest value -------------------

arr = [2,6,3,8,0,1]

smallest = arr[0]
second_smallest = arr[0]

for i in range(1, len(arr)):
    if arr[i] < smallest:
        second_smallest = smallest
        smallest = arr[i]
    elif arr[i] > smallest and arr[i] < second_smallest:
        second_smallest = arr[i]

print(second_smallest)

# Third highest value ---------------

arr = [2,6,3,8,0,1]

largest = 0
second_largest = 0
third_largest = 0

for i in range(len(arr)):
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]
    elif largest > arr[i] and arr[i] > second_largest and arr[i] > third_largest:
        third_largest = arr[i]
        
print(third_largest)

# Highes value based on 2nd element ---------------

s = [[2,50] , [3,90] , [1, 40] , [4,30]]

max_value = s[0][1]
max_list = s[0]

for i in range(len(s)):
    if s[i][1] > max_value:
        max_value = s[i][1]
        max_list = s[i]
        
print(max_list)

# ----------------------------

arr = [2,4,5,7,9,1,3,-9,-9]

largest = 0
second_largest = 0
small = 0
second_small = 0

for i in range(len(arr)):
    if largest < arr[i]:
        second_largest = largest
        largest = arr[i]
        
    elif largest > arr[i] and second_largest < arr[i]:
        second_largest = arr[i]
        
    elif small > arr[i]:
        second_small = small
        small = arr[i]
        
    elif small <= arr[i] and second_small >= arr[i]:
        second_small = arr[i]
        
print(largest*second_largest)
print(small*second_small)


# <= , >=
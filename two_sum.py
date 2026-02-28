arr = [1, 3, 2, 3, 4, 4, 5, 7, 2]

target = 6
i = 0
map = {}

while i < len(arr):
    num = arr[i]
    look = target - num
    if look in map:
        print([map[look] , i])      
    map[num] = i
    i += 1
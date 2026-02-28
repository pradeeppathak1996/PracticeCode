arr = [1, 3, 2, 3, 4, 4, 5, 7, 2, 6]

target = 7

for i in range(len(arr)):
    num1 = arr[i]
    new_target = target - num1
    
    map = {}
    for j in range(i+1 , len(arr)):
        num2 = arr[j]
        num3 = new_target - num2
        if num3 in map:
            print([i , map[num3] , j])
        map[num2] = j
        j += 1
    i += 1
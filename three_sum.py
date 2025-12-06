arr = [1, 3, 2, 3, 4, 5, 7, 2]
target = 7

for i in range(len(arr)):        
    num1 = arr[i]
    new_target = target - num1  
    
    map = {}    
    for j in range(i + 1, len(arr)):
        num2 = arr[j]
        look = new_target - num2

        if look in map:
            print(num1, look, num2)
        map[num2] = j
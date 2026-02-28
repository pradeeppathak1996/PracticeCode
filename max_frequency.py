arr = [1, 1, 2, 3, 3, 3, 4]

freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

max_count = 0
max_element = None
for key in freq:
    if freq[key] > max_count:
        max_count = freq[key]
        # max_element = freq[key]   
        max_element = key
print(max_element,":",max_count)
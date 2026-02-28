arr = [-2,1,-3,4,-1,2,1,-5,4]

max_sum = arr[0]
curr_sum = arr[0]
i = 1

while i < len(arr):
    if curr_sum + arr[i] > arr[i]:
        curr_sum = curr_sum + arr[i]
    else:
        curr_sum = arr[i]

    if curr_sum > max_sum:
        max_sum = curr_sum

    i += 1

print(max_sum)

# Output → 6 ([4,-1,2,1])
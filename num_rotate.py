# ---------- 2 elements rotating ---------------

arr = [1,2,3,4,5]
n = 2

# step 1: reverse first n elements
i = 0
j = n - 1
while i < j:
    arr[i], arr[j] = arr[j], arr[i]
    i = i + 1
    j = j - 1

# step 2: reverse remaining elements
i = n
j = len(arr) - 1
while i < j:
    arr[i], arr[j] = arr[j], arr[i]
    i = i + 1
    j = j - 1

# step 3: reverse whole array
i = 0
j = len(arr) - 1
while i < j:
    arr[i], arr[j] = arr[j], arr[i]
    i = i + 1
    j = j - 1

print(arr)

# Output = [3, 4, 5, 1, 2]

# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------


arr = [1,2,3,4,5]
n = 2

length = len(arr)

# convert right rotation to left rotation
n = n % length
n = length - n

# -------------------------------
# step 1: reverse first n elements
i = 0
j = n - 1
while i < j:
    arr[i], arr[j] = arr[j], arr[i]
    i = i + 1
    j = j - 1

# -------------------------------
# step 2: reverse remaining elements
i = n
j = length - 1
while i < j:
    arr[i], arr[j] = arr[j], arr[i]
    i = i + 1
    j = j - 1

# -------------------------------
# step 3: reverse whole array
i = 0
j = length - 1
while i < j:
    arr[i], arr[j] = arr[j], arr[i]
    i = i + 1
    j = j - 1

print(arr)

# Output = [4, 5, 1, 2, 3]
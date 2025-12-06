arr = [1,2,3,4,6]

n = max(arr)

xor_arr = 0
xor_all = 0

for i in range(1,n+1):
    xor_all ^= i
for i in arr:
    xor_arr ^=  i
    
missing = xor_arr^xor_all
print(missing)
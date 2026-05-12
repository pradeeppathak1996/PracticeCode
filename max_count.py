arr = [1,0,1,1,0,1,1,1,1,0]

max_count = 0
count = 0

for i in arr:
    if i == 1:
        count += 1
        if  count > max_count:
            max_count = count
            
    else:
        count = 0
print(max_count)

# In string ----------------------

arr = "aaaabbbc"

freq = {}
max_char = None
max_count = 0

for ch in arr:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1
        
    if freq[ch] > max_count:
        max_count = freq[ch]
        max_char = ch

print(f"{max_char}:{max_count}")

# output a:4
s = "abcabcbb"    # change input here

char_index = {}   # to store last index of character
left = 0
right = 0
max_len = 0

# manually calculate length of string

n = 0
for _ in s:
    n += 1

while right < n:
    ch = s[right]

    # if character already seen and inside window

    if ch in char_index and char_index[ch] >= left:
        left = char_index[ch] + 1

    char_index[ch] = right
    curr_len = right - left + 1

    if curr_len > max_len:
        max_len = curr_len

    right += 1
    
print(max_len)

# output = 3 (abc)
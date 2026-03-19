s = "abcabcbb"

seen = {}
start = 0
max_len = 0
i = 0

while i < len(s):
    ch = s[i]

    if ch in seen and seen[ch] >= start:
        start = seen[ch] + 1

    seen[ch] = i
    current_len = i - start + 1

    if current_len > max_len:
        max_len = current_len
    i = i + 1

print(max_len)
arr = ["ate" , "eat", "tea", "tan", "nat", "bat"]

freq = {}

for word in arr:
    key = "".join(sorted(word))

    if key in freq:
        freq[key] += [word]
    else:
        freq[key] = [word]

print(list(freq.values()))

# t
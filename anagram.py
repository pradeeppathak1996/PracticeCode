arr = ["ate" , "eat", "tea", "tan", "nat", "bat"]

freq = {}

for word in arr:
    key = "".join(sorted(word))

    if key in freq:
        freq[key] += [word]
    else:
        freq[key] = [word]

print(list(freq.values()))  

# output.    [['aet', 'eat', 'tea'], ['ant', 'nat'], ['abt']]


arr = ["ate" , "eat", "tea", "tan", "nat", "bat"]

freq = {}

for word in arr:
    key = "".join(sorted(word))
    if key in freq:
        freq[key].append(word)
    else:
        freq[key] = [key]

print(freq)

# output.   {'aet': ['aet', 'eat', 'tea'], 'ant': ['ant', 'nat'], 'abt': ['abt']}
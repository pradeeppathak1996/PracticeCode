s = "welcome to the channelsoft"

count = 0
target = "n"
i = 0

while i < len(s):
    if s[i] == target:
        count += 1
    i += 1
    
print(count)
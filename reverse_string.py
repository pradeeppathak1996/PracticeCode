s = "my name is pradeep"

res = ""
word = ""
i = 0
while i < len(s):
    if s[i] != " ":
        word = s[i] + word
    else:
        res += word + " "
        word = ""
    i += 1 
    
res += word
print(res)

# output -> "ym eman si peedarp"

# ------------------------

s = "hello world"

rev = ""
sp = s.split()

for i in sp:
    rev = i+ " " +rev

print(rev)

# output ->  "world hello"

# without inbuilt function ---

s = "hello world"

rev = ""
word = ""
i = 0

while i < len(s):
    if s[i] != " ":
        word = word + s[i]
    else:
        if rev == "":
            rev = word
        else:
            rev = word + " " + rev
        word = ""
    i = i + 1

# last word add karo
if rev == "":
    rev = word
else:
    rev = word + " " + rev
print(rev)

# output -> "world hello"


# First Non-Repeating Character (WITHOUT in-built) --

s = "swiss"

freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for ch in s:
    if freq[ch] == 1:
       print(ch)
       break

# output -> w
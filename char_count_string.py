s = "welcome to the channelsoft"

count = 0
target = "n"
i = 0

while i < len(s):
    if s[i] == target:
        count += 1
    i += 1
    
print(count)

# Vowels and Consonants count -------------

s = "welcome to the channelsoft"

vowels= "aeiouAEIOU"
cons = 0
vowel = 0

for i in s:
    if i in vowels:
        vowel += 1
    else:
        cons += 1
    
print("vowel", vowel)
print("cons", cons)
        
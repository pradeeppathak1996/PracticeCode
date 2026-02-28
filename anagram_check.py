def is_anagram(str1 , str2):
    if len(str1) != len(str2):
        return False
    
    count = {}
    for ch in str1:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
    for ch in str2:
        if ch in count:
            count[ch] -= 1
        else:
            return False
    for val in count.values():
        if val != 0:
            return False
        return True
    
print(is_anagram("tea" , "ate"))
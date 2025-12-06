s = "dad"

is_palindrome = True

for i in range(len(s) // 2):
    if s[i] != s[-(i+1)]:
        is_palindrome = False
        break
if is_palindrome:
    
    print(s , "is a Palindrome")
else:
    print(s , "is not a Palindrome")
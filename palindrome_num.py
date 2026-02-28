num = 1216

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse*10 + digit
    num = num//10

if original == reverse:
    print("Palindrome number")
else:
    print("Not a Palindrome number")
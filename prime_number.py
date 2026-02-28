num = 23
if num > 1:
    for i in range(2 , num):
        if num%i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")

# prime numbers between 1 and 100 --------------------------------

for num in range(2,101):
    for j in range(2 , num):
        if num%j == 0:
            break
    else:
        print(num)

# UPPER CLOSE PRIME NUMBER -------------------------------

num = int(input("Enter number: "))

candidate = num

while True:
    if candidate < 2:
        is_prime = 0
    else:
        is_prime = 1
        i = 2
        while i < candidate:
            if candidate % i == 0:
                is_prime = 0
                break
            i = i + 1

    if is_prime == 1:
        print("Result:", candidate)
        break

    candidate = candidate + 1
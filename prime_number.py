num = 23
if num > 1:
    for i in range(2 , num):
        if num%i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")

# prime numbers between 1 and 100 --------------------------------

for i in range(2,101):
    for j in range(2 , i):
        if i%j == 0:
            break
    else:
        print(i)
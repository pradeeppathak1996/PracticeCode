num = 10

a = 0       
b = 1 

for i in range(1, num + 1):
    a , b = b , a+b
    
print(b)

# recursion -----

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

n = 7
i = 0
while i < n:
    print(fib(i), end=" ")
    i = i + 1
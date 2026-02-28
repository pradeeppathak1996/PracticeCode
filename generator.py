def my_generator(n):
    for i in range(n):
        yield i

gen = my_generator(10)
print(next(gen))
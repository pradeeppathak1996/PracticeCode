# Function Decorator1 ------------

def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()

# Function Decorator2 --------------------

def my_deco(addition):
    def wrapper():
        result = addition()
        d = 10
        return result + d
    return wrapper

@my_deco
def addition():
    a = 8
    b = 7
    c = a+b
    return c
print(addition())

# Decorator With Arguments ------------

def repeat(n):
    def decorator(hello):
        def wrapper():
            for i in range(n):
                hello()
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("Hi")

hello()

# Class-Based Decorator ------------

class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Before")
        self.func()
        print("After")

@MyDecorator
def greet():
    print("Hello")

greet()

# Method Decorators (Inside Class) ----------

# @staticmethod------

class A:
    @staticmethod
    def add(a, b):
        return a + b

print(A.add(5, 3))

# @classmethod------

class A:
    name = "Pradeep"

    @classmethod
    def change_name(cls):
        cls.name = "Kumar"

A.change_name()
print(A.name)


# -- Decorator issues --


def int_check_decorator(addition):
    def wrapper(num1, num2):
        if type(num1) == int and type(num2) == int:
            return addition(num1, num2)
        else:
            return None
    return wrapper

@int_check_decorator
def addition(num1, num2):
    return num1 + num2

print(addition(10, 20))     # 30
print(addition(10, "20"))   # None
print(addition(5.5, 2))    # None

# Number of arguments Unknown -----

def valid(func):
    i = 0
    def wrapper(*args):
        if i < len(args):
            return func(*args)
        return None
    return wrapper

@valid
def addition(*nums):
    total = 0
    i = 0
    while i < len(nums):
        total += nums[i]
        i += 1
    return total

print(addition(10, 20))        # 30
print(addition(10, 20, 30))    # 60
print(addition(5, 2, 8, 1))    # 16
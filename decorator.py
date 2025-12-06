# Function Decorator -------------------------

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

# Decorator With Arguments ------------------

def repeat(n):
    def decorator(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return decorator

@repeat(3)
def hello():
    print("Hi")

hello()

# Class-Based Decorator ---------------------------

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

# Method Decorators (Inside Class) ----------------------------------- 

# @staticmethod

class A:
    @staticmethod
    def add(a, b):
        return a + b

print(A.add(5, 3))

# @classmethod

class A:
    name = "Pradeep"

    @classmethod
    def change_name(cls):
        cls.name = "Kumar"

A.change_name()
print(A.name)
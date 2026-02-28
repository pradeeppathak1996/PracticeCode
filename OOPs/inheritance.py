# ------------- INHERITANCE -------------

# --SINGLE inheritance--

class A:
    def show(self):
        print("print A")
class B(A):
   pass

obj = B()
obj.show()

# MULTILEVEL Inheritance --

class GrandParent:
    def show1(self):
        print("GrandParent")
class Parent(GrandParent):
    def show2(self):
        print("Parent")
class Child(Parent):
    def show3(self):
        print("child")

obj = Child()
obj.show1()
obj.show2()
obj.show3()

# MULTIPLE Inheritance --

class GrandFather:
    def show1(self):
        print("GrandFather")
class Parent:
    def show2(self):
        print("Parent")
class Child(GrandFather , Parent):
    pass

obj = Child()
obj.show1()
obj.show2()

# -- Hierarchical Inheritance -- (one parent multiple child)

class Parent:
    def show(self):
        print("Parent")
class Child1(Parent):
    pass
class Child2(Parent):
    pass

obj1 = Child1()
obj1.show()
obj2 = Child2()
obj2.show()
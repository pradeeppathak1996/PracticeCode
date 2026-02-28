def add(a,b):
    
    if type(a) != int or type(b) != int:
        return "Datatype Error"
    else:
        return a+b
        
print(add(10, 20))
print(add(10, "20"))
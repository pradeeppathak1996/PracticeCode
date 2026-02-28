# --------args-------------

def add_argumanets(*args):
    total = 0
    for n in args:
        total += n
    print(total)

add_argumanets(4,5,7)
add_argumanets(5, 10, 15, 20)


# --------- kwargs ----------------------

def show_details(**kwargs):
    
    for key , value in kwargs.items():
        print(key , ":" , value)

show_details(name = "pradeep" , role = "backend developer" , empID = 12335)
class Bank:
    def __init__(self):
        self.__balance = 10000

    def get_balance(self):
        return self.__balance
    
    def add_money(self , amout):
        self.__balance += amout

b = Bank()
print(b.get_balance())
b.add_money(500)
print(b.get_balance())
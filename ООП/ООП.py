class ATM:
    def __init__(self, balance, pin):
        self.balance = balance
        self.pin = pin
    def check_balance(self,pin):
        if pin == self.pin:
            return self.balance
        else:
            return 'Wrong pin'
    def withdraw_balance(self, pin, amount):
        if pin == self.pin:
            if amount > self.balance:
                return 'Insufficient funds'
            self.balance  -= amount
            return self.balance
        else:
            return 'Wrong pin'

    def deposit_balance(self, pin, amount):
        if pin == self.pin:
            self.balance += amount
            return self.balance
        else:
            return 'Wrong pin'
my_atm = ATM(1000, 1234)

print(my_atm.balance)
print(my_atm.pin)
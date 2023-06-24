class bankaccnount:
    #private fields
    __account_number = ''
    __balance = 0

    #public field 
    account_holder = ''
    #static field: all object are in the same staic field. 

    bank_name = 'mybank'

    def  ___init__(self, account_number, balance, account_holder):
        self.__account_number = account_number
        self.__balance = balance
        self.account_holder = account_holder

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, amount):
        self.__account_number = amount

    def deposit(self, amount):
        self.__balance += amount

    @staticmethod
    def get_bank_name():
        return bankaccnount.bank_name
    
    def __str__(self):
        return "account holder is" + self.account_holder
    
account1 = bankaccnount("123456789", 1000,"Alice")
account1.__account_number = "456"
print(account1.get_account_number())
account1.account_holder = 'Alex'
print(account1.account_holder)
print(bankaccnount.get_bank_name())
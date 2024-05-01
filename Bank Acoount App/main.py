from functools import wraps
import datetime

class NotEnoughBalance(Exception):
    """Raised when withdrawal amoount is greater than balance"""
    pass

    

class Account:
    def __init__(self, name, ac_no):
        self.account_no = ac_no
        self.user_name = name
        self.balance = 1000

    
    def log_balance(func):

        import logging
        logging.basicConfig(filename="C:/Musfique's Folder/Python/Self-tought-projects/Bank Acoount App/transaction.log", level=logging.INFO)


        @wraps(func)
        def wrapper(self, amount):
            logging.info(
                f"Transaction time: {datetime.datetime.now()}; Account no:{self.account_no}; Transaction type: {func.__name__.title()}; Balance: {self.balance}"
            )

            print(f"\n{datetime.datetime.now()}:\nAttempting {func.__name__} of {amount} BDT")
            value = func(self, amount)
            print(f"Current Balance: {self.balance}")
            return value
        return wrapper
    
    
    @log_balance
    def deposit(self, amount):
        self.amount = amount
        self.balance += amount

    @log_balance
    def withdraw(self, amount):
        self.amount = amount
        try:
            if (self.balance < amount):
                raise NotEnoughBalance("Transaction Stopped!!! \nYour withdrawal amount exceded current balance.")
        except NotEnoughBalance as neb:
            print(neb)
        else:
            self.balance -= amount







ac_1 = Account("Anik", "0152330101")
# ac_1.deposit(50000)
# ac_1.withdraw(50000)
# ac_1.withdraw(2000)
# ac_1.withdraw(1000)

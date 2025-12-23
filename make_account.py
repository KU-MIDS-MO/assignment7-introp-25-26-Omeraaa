def make_account(initial_balance):
    balance = initial_balance
    
    def deposit(amount):
        nonlocal balance
        if amount < 0:
            raise ValueError("Negative Number")
        balance += amount
        balance_after_deposit = balance
        return balance_after_deposit

    def withdraw(amount):
        nonlocal balance
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > balance:
            raise ValueError("Not Enough Money")
        balance -= amount
        balance_after_withdraw = balance
        return balance_after_withdraw

    
    return deposit, withdraw
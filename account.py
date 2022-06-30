def show_balance(balance):
    print(f"Current balance:{balance}$")


def deposit(balance):
    amount = float(input("Enter an amount to deposit: $"))
    if amount <= 0:
        print("Your deposit has to be superior than 0")
    else:
        balance += float(amount)
        return balance


def withdraw(balance):
    amount = float(input("Enter an amount to withdraw: $"))
    if amount > balance:
        print("Insufficient funds")
    else:
        balance -= float(amount)
        return balance


def logout(name):
    print(f"Goodbye {name}")
    pass

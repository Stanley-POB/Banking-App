from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")

    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


while True:
    print("          === Automated Teller Machine ===          ")
    print("")
    name = input("Enter name to register: ")
    print("")
    balance = 0

    if not name.isalpha():
        print("Name must contain only alphabetical characters\n")
        continue

    elif len(name) not in range(1, 10):
        print("Name must be minimum 1 character and maximum 10 characters.")
        continue

    else:
        break

while True:
    pin = (input("Choose a 4-digit pin: "))
    print("")

    if not pin.isdigit():
        print("Pin can only contain numbers\n")

    elif len(pin) != 4:
        print("Pin must be 4 digits")

    else:
        print(f"{name} has registered with a starting balance of {balance}$")
        print("")
        break


while True:
    print("LOGIN")
    name_to_validate = input("Enter name: ")
    pin_to_vaidate = (input("Enter PIN: "))

    if name_to_validate == name and pin_to_vaidate == pin:
        print("LOGIN successful!")
        break

    else:
        print("Invalid Credentials!")

while True:
    atm_menu(name)
    option = input("Choose an option: ")

    if option == "1":
        account.show_balance(balance)

    elif option == "2":
        balance = account.deposit(balance)
        account.show_balance(balance)

    elif option == "3":
        balance = account.withdraw(balance)
        account.show_balance(balance)

    else:
        account.logout(name)
        break

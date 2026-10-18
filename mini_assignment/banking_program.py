# Python Banking Program

def show_balance(balance):
    print("---------------------------------------")
    print(f"Your balance is ${balance:.2f}")
    print("---------------------------------------")

def deposite():
    print("---------------------------------------")
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print("That's not valid amount")
        print("---------------------------------------")
        return 0
    else:
        print(f"You deposited successfully!")
        print("---------------------------------------")
        return amount
        
    
    

def withdraw(balance):
    print("---------------------------------------")
    amount = float(input("Enter amount to be withdrawn: "))

    if amount < 0:
        print("That's not valid amount")
        print("---------------------------------------")
        return 0
    elif amount > balance:
        print("Insufficient Funds")
        print("---------------------------------------")
        return 0
    else:
        print("Money withdrawn Succesfully!")
        print("---------------------------------------")
        return amount


def main():

    print()
    print("---------------------------------------")
    print("                WELCOME                ")
    print("---------------------------------------")
    print()
    print("1.Check Balance")
    print("2.Deposite")
    print("3.Withdraw")
    print("4.Exist")
    print()
    print("---------------------------------------")
    print()

    balance = 0
    error = 0
    is_running = True

    while is_running:

        choice = input("Enter your Choice (1-4): ")
        print()
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposite()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("---------------------------------------")
            print("Invalid Choice!")
            print()
            error += 1
            if error == 2:
                is_running = False
            else:
                print("               Try Again!             ")
                print()   
                print("---------------------------------------")         
    print("---------------------------------------")
    print("               Thank You!              ")
    print("---------------------------------------")

if __name__ == '__main__':
    main()



        
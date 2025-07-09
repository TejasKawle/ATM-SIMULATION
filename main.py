from datetime import datetime
from datetime import date

AMOUNT = 1000
PIN = 1234
PIN_ATTEMPT = 3

def intro():
    print("""
          Hey! Welcome to ATM simulation
          (Below commands are used to operate it)
          Withdraw           ---> press 1
          Deposit            ---> press 2
          Balance            ---> press 3
          PIN change         ---> press 4
          History            ---> press 5
          EXIT               ---> press 6
""")

def storeHistory(his):
    with open("history.txt", "a") as f:
        f.write(his)

def showHistory():
    try:
        with open("history.txt", "r") as f:
            data = f.read()
            if data:
                print("\n--- Transaction History ---")
                print(data)
            else:
                print("No transactions yet.")
    except FileNotFoundError:
        print("No transaction history found.")

def withdraw(amt):
    global AMOUNT
    global PIN_ATTEMPT
    pin = int(input("Enter pin : "))
    if pin == PIN:
        if amt <= AMOUNT:
            AMOUNT -= amt
            print(f"{amt}rs is withdrawn from your account. Press 3 to check available balance.")
            now = datetime.now()
            storeHistory(f"Withdrawn: {amt} Rs on {date.today()} at {now.strftime('%H:%M:%S')}\n")
        else:
            print("Insufficient Balance !!!")
    else:
        PIN_ATTEMPT -= 1
        print(f"Incorrect PIN! {PIN_ATTEMPT} attempt(s) left.")

def deposite(amt):
    global AMOUNT
    global PIN_ATTEMPT
    pin = int(input("Enter pin : "))
    if pin == PIN:
        AMOUNT += amt
        print(f"{amt}rs is deposited to your account. Press 3 to check available balance.")
        now = datetime.now()
        storeHistory(f"Deposited: {amt} Rs on {date.today()} at {now.strftime('%H:%M:%S')}\n")
    else:
        PIN_ATTEMPT -= 1
        print(f"Incorrect PIN! {PIN_ATTEMPT} attempt(s) left.")

def balance():
    global PIN_ATTEMPT
    pin = int(input("Enter pin : "))
    if pin == PIN:
        print(f"Balance : {AMOUNT}")
        now = datetime.now()
        storeHistory(f"Checked balance on {date.today()} at {now.strftime('%H:%M:%S')}\n")
    else:
        PIN_ATTEMPT -= 1
        print(f"Incorrect PIN! {PIN_ATTEMPT} attempt(s) left.")

def changePIN():
    global PIN
    global PIN_ATTEMPT
    prevPIN = int(input("Enter previous PIN : "))
    if prevPIN == PIN:
        newPIN = int(input("Enter new PIN : "))
        PIN = newPIN
        print("Your PIN has successfully changed !!!")
        now = datetime.now()
        storeHistory(f"PIN changed on {date.today()} at {now.strftime('%H:%M:%S')}\n")
    else:
        PIN_ATTEMPT -= 1
        print(f"Incorrect PIN! {PIN_ATTEMPT} attempt(s) left.")

if __name__ == "__main__":
    intro()

    while True:
        if PIN_ATTEMPT == 0:
            print("Too many incorrect PIN attempts. Your account is locked!")
            break

        try:
            option = int(input("Enter option : "))
            match option:
                case 1:
                    amt = int(input("Enter Amount : "))
                    withdraw(amt)
                case 2:
                    amt = int(input("Enter Amount : "))
                    deposite(amt)
                case 3:
                    balance()
                case 4:
                    changePIN()
                case 5:
                    showHistory()  
                case 6:
                    print("Exiting... Thank you for using the ATM.")
                    break
                case _:
                    print("Enter valid option !!")
        except Exception as e:
            print("Invalid input detected! Please use only numbers for options and amounts.")

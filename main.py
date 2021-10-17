import time
# global variable balance
balance = 10000

def ATM():
    print("WELCOME TO El Banco Corrupto Grande™")
    print("Enter your option")
    print("1: Withdraw money")
    print("2: Deposit money")
    print("3: Check balance")
    print("4: Exit")
    
    # method to withdraw money
    def out():
        global balance
        m = float(input("Enter money you want to withdraw: "))
        if(m>balance):
            print("insufficient balance")
        else:
            balance-=m
            print("Collect your cash. Available balance: "+str(balance))
        time.sleep(2)
        ATM()
    
    # method to deposit money
    def put():
        global balance
        m = float(input("Enter money you want to deposit: "))
        balance+=m
        print("New balance: "+str(balance))
        time.sleep(2)
        ATM()
    
    # method to show balance
    def show():
        global balance
        print("Your current balance is : "+str(balance))
        time.sleep(2)
        ATM()
    
    # adios amigos
    def exit():
        print("See you soon!!")
        time.sleep(2)
        print("Transaction ended")

    option=int(input());
    
    if(option == 1):
        out()
    elif(option == 2):
        put()
    elif(option == 3):
        show()
    elif(option == 4):
        exit()
    else:
        exit()
        
if __name__ == "__main__":
    ATM()

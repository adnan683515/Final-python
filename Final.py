

import time

class person:
    
    def __init__(self,name,email,address,account_type):
        
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.id = time.time()
        

class Bank:
    
    isbankdrupt = True
    isloandrupt = True
    print("_____________________________________Datch Bangla Bank Limited_________________________________________")
    Bank_history = { } #{email:obj}
    Bank_tk = 10000
    # withdraw_history = { } #email : tk
    withdraw_history = [ ]
    loan_amount = 0
    
    def __init__(self):
        self.cnt = 0
        self.__code = 1010 #Admin code,just Adnin know about this code.
        self.__code2 = 1111 #all user code
        
    def get_code (self):
        return self.__code
    def get_code2(self):
        return self.__code2
    def create(self,person):
        if person.email in self.Bank_history:
            print("\t\tAlready Account created")
        else:
            self.Bank_history[person.email] = person
            print("\t\tSuccessfullY")
    
    def deposit(self,amount,email):
        if email in self.Bank_history:
            
            self.Bank_history[email].balance += amount
            self.Bank_tk += amount
            print("\t\t-------->Deposit Done<----------")
        else:
            print("\tUnknown Account")
        
    def withdraw(self,amount,email):
        
        if self.isbankdrupt == True:
            if email in self.Bank_history and amount < self.Bank_history[email].balance:
                self.Bank_history[email].balance -= amount
                self.Bank_tk -= amount
                # self.withdraw_history[email] = amount
            
                self.withdraw_history.append([email,amount])
                print("\t\t..............>Withdraw Done<..................")
            else:
                print("--->Sorry.Unknown Account<-----")
        else : 
            print("\t\tBank Drupt off!Now you can't withdraw")
    def check_balance (self,email):
        if email not in self.Bank_history or self.Bank_history[email].balance == 0 :
            print("\t\t--->Your Balance is Empty<-----")
        else:
            print(self.Bank_history[email].balance)

    def transection_history(self):
        if len(self.withdraw_history) == 0:
            print("\t\tEmpty List")
        else:
                print("Email\tAmmount")
                for i in self.withdraw_history:
                    print(i)
    def loan(self,amount,email):
        if self.isloandrupt == True:
                if email in self.Bank_history and amount < self.Bank_tk and self.cnt < 2:
                    self.cnt +=1
                    self.Bank_history[email].balance += amount
                    self.Bank_tk -= amount
                    self.loan_amount += amount
                else:
                    print("\t-->Your can't take loan This Bank<---")
        else :
            print("\t\tLoan feature off!Now You can't take loan This bank.You can tell Admin panel!")  
            
    def transfer(self,amount,from_email,to_email):
        if to_email in self.Bank_history and amount < self.Bank_history[from_email].balance:
            self.Bank_history[to_email].balance += amount
            self.Bank_history[from_email].balance -= amount
        else:
            print("\t\tUnknown Account")
            
    def delete_account(self,email):
        if email in self.Bank_history:
            self.Bank_history.pop(email)
            print("\t\tAccount Deleted")
        else:
            print("\t\tUnknown Account")
    
    def bank_balance(self):
        if self.Bank_tk == 0:
            print("\t\tBank Amount is Empty")
        else:
            print("Bank Ammount: ",self.Bank_tk)
    
    def view_account(self):
        if len(self.Bank_history) ==0 :
            print("\t\tEmpty Account")
        else:
            print("Name\tEmail   \tAddress")
            for key,val in self.Bank_history.items():
                print(val.name,key,val.address)
    def ln_ammount(self):
        if self.loan_amount == 0:
            print("\t\tKew loan nei nai")
        else:
            print("\t\tTotal Loan Tk: ",self.loan_amount)
            
            
bk = Bank()

while True:
    print("\t1.Are You Admin")
    print("\t2.Are You user ")
    print("\t3.Exit")
    option = int(input("\tEnter OPtions: "))
    if option == 3 :
        break
    code = int(input("Enter Your User\Admin code: "))
    
    if option == 1 and code == bk.get_code():
        print("_____________Admin______________")
        while True:
            print("\t1.create an account ")
            print("\t2.delete any user account ")
            print('\t3.see all user accounts list  ')
            print('\t4.check the total available balance of the bank')
            print('\t5.check the total loan amount')
            print('\t6.on or off the BankDrupt feature of the bank')
            print("\t7.Loan feature on/off")
            print("\t8.Home")
            op = int(input("Enter Options: "))
            if op == 1:
                print(f"\n\tNo logged in user: ")
                option = input("Login?Registration(L/R): ")
                if option == 'R':
                    name = input("\tEnter Your Name : ")
                    email = input("\tEnter Your Email : ")
                    address = input("\tEnter Your Address : ")
                    account_type = input("\tEnter Your Account Type : ")
                    pk = person(name,email,address,account_type)
                    bk.create(pk)
                    currentUser = pk
                elif option == 'L':
                    email = input("\tEnter Your Email: ")
                    
                    if email in bk.Bank_history.keys():
                        currentUser = bk.Bank_history[email]
                        print('\tAlredy Axits')
                    else:
                        print("\tuser not found")
            elif op == 2:
                email = input("\tEnter Your Email : ")
                bk.delete_account(email)       
            elif op == 3:
                bk.view_account()
            elif op == 4:
                bk.bank_balance()
        
            elif op == 5:
                bk.ln_ammount()
            elif op== 6:
                print("\t1.Bank Drupt on")
                print("\t2.Bank Drupt off")
                op = int(input("Enter Options: "))
                if op==1:
                    bk.isbankdrupt= True #bank theke akhn tk tulte parbe
                elif op==2 :
                    bk.isbankdrupt=False #bank theke tk tulte parbe na
            elif op==7:
                print("\t1.Bank loan Drupt on")
                print("\t2.Bank loan Drupt off")
                op = int(input("Enter Options: "))
                if op==1:
                    bk.isloandrupt= True #bank theke akhn tk tulte parbe
                elif op==2 :
                    bk.isbankdrupt=False #bank theke tk tulte parbe na
            elif op==8:
                break 
            else:
                print("\t\tUnknow options") 
        
    elif  option == 2 and code==bk.get_code2():
            print("______________User_______________")
            while True:
                print("Enter Your Options: ")
                print("\t1.Create Account")
                print("\t2.Deposit Amount")
                print("\t3.Withdraw Amount")
                print("\t4.Cheack Available Balance")
                print('\t5.View Transection History')
                print("\t6.Take Loan")
                print("\t7.Transfer amount")
                print('\t8.Home')
                
                op  = int(input("Enter Your OPtions: "))
                
                if op == 1:
                    name = input("\tEnter Your Name : ")
                    email = input("\tEnter Your Email : ")
                    address = input("\tEnter Your Address : ")
                    account_type = input("\tEnter Your Account Type : ")
                    pk = person(name,email,address,account_type)
                    bk.create(pk)
                    
                elif op == 2:
                    amount = int(input("\tEnter Your Amount: "))
                    email = input("\tEnter Your Email: ")
                    bk.deposit(amount,email)
                
                    
                elif op==3:
                    amount = int(input("\tEnter Your Amount: "))
                    email = input("\tEnter Your Email: ")
                    bk.withdraw(amount,email)
            
                elif op==4:
                    email = input("\tEnter Your Email: ")
                    bk.check_balance(email)
                elif op==5:
                    bk.transection_history()
                elif op == 6:
                    amount = int(input("\tEnter Your Amount: "))
                    email = input("\tEnter Your Email: ")
                    bk.loan(amount,email)
                elif op == 7:
                    amount = int(input("\tEnter Your Amount: "))
                    from_email = input("\tEnter Your Email: ")
                    to_email = input("\tEnter Transfer Email: ")
                    bk.transfer(amount,from_email,to_email)
                else:
                    break
    elif option==3 :
        break
    else:
        print("\tUnknow options")

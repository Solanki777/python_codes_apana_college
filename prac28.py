class bank:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account=acc
        print("Hi",self.account, "your account balance is ",self.balance)

    def debit(self,amount):
        self.balance-=amount
        print(amount, "is debited remaining balance is ",self.balance)

    def credited(self,amount):
        self.balance+=amount
        print(amount, "is credited remaining balance is ",self.balance)

    def money_show(self):
        return self.balance

ac1=bank(20000,659)
c=1
while c==1:
    print("press 1 for checking balance")
    print("press 2 for debit money from account")
    print("press 3 for credit money from account")
    k=int(input("enter your choice:"))
          
    if k==1 : 
        print("money is your account is ",ac1.money_show())

    elif k==2 :
        m=int(input("enter amount you want to debit:"))
        ac1.debit(m)

    elif k==3 :
        m=int(input("enter amount you want to credit:"))
        ac1.credited(m)

    else : print("you press wrong key")
    c=int(input("press 1 for continue :"))
        
        
    


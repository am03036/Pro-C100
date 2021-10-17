class Atm(object):
    def __init__(self,cardNum,pinNum,initialBalance):
        self.cardNum = cardNum
        self.pinNum = pinNum
        self.initialBalance = initialBalance
    
    def balance(self):
        print('Current balance is ',self.initialBalance)
    
    def cashWithdrawal(self):
        amt = int(input('Enter amount to be withdrawed: '))
        self.initialBalance-=amt
        print('Amout withdrawn is ',amt)
        print('Current balance is ',self.initialBalance)
    
    def cashDeposit(self):
        amt = int(input('Enter the amount to be deposited: '))
        self.initialBalance+=amt
        print('Amout deposited is ',amt)
        print('Current balance is ',self.initialBalance)

card1 = Atm("01234","9876",1234567)
card1.balance()
card1.cashWithdrawal()
card1.cashDeposit()
